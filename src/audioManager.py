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
        self._ambient = None

    def load(self, filename: str):
        p = Path(filename)
        if not p.exists():
            raise FileNotFoundError(f"Audio file not found: {filename}")
        sound = oalOpen(str(p))
        self._sounds[str(p)] = sound
        return sound
    def _get_sound(self, filename: str):
        """Get a already loaded sound or load it if not available."""
        key = str(Path(filename))
        snd = self._sounds.get(key)
        if snd is None:
            snd = self.load(filename)
        return snd
    def play_effect(self, filename: str, position: tuple[float, float, float] = (0, 0, 0), gain: float = 4.0):
        snd = self._get_sound(filename)
        snd.set_looping(False)
        snd.set_position(position)
        snd.set_gain(gain)   
        snd.play()

    def play_ambient(self, filename: str, position: tuple[float, float, float] = (0, 0, 0), gain: float = 3.0):
        """
        Play a looping ambient sound at an optional 3D position.
        Stops the previous ambient track if one is active.
        (0,0,0) -> center
        (1,0,0) -> right
        (-1,0,0) -> left
        (0,0,1) -> front
        (0,0,-1) -> behind
        (0,1,0) -> above
        (0,-1,0) -> below
        (2,0,0) -> far right
        (-2,0,0) -> far left
        (0,0,5) -> far front
        (0,0,-5) -> far behind        
        """
        if self._ambient is not None:
            self._ambient.stop()
        snd = self._get_sound(filename)
        snd.set_looping(True)
        snd.set_position(position)
        snd.set_gain(gain)   
        snd.play()
        self._ambient = snd
    def stop_ambient(self):
        """Stop the current ambient sound if active."""
        if self._ambient is not None:
            self._ambient.stop()
            self._ambient = None

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
