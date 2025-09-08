# game/audio.py
from openal import oalOpen, oalQuit
from pathlib import Path
from typing import Dict

class AudioManager:
    """
    Simple wrapper for playing short sounds using python-openal.
    It keeps loaded sounds in a small cache so repeated plays are fast.
    """

    def __init__(self):
        self._sounds: Dict[str, object] = {}

    def load(self, filename: str):
        p = Path(filename)
        if not p.exists():
            raise FileNotFoundError(f"Audio file not found: {filename}")
        sound = oalOpen(str(p))
        self._sounds[str(p)] = sound
        return sound

    def play(self, filename: str):
        """
        Play the given file. Will load it on demand.
        Non-blocking: play() returns immediately while sound plays.
        """
        key = str(Path(filename))
        snd = self._sounds.get(key)
        if snd is None:
            snd = self.load(filename)
        snd.play()

    def stop_all(self):
        for snd in self._sounds.values():
            try:
                snd.stop()
            except Exception:
                pass

    def close(self):
        # stop and release OpenAL
        self.stop_all()
        try:
            oalQuit()
        except Exception:
            pass
