from openal import oalOpen, oalQuit
from pathlib import Path
from typing import Dict, Tuple

POSITION_PRESETS = {
    "center": (0.0, 0.0, 0.0),
    "right": (1.0, 0.0, 0.0),
    "left": (-1.0, 0.0, 0.0),
    "front": (0.0, 0.0, 1.0),
    "behind": (0.0, 0.0, -1.0),
    "above": (0.0, 1.0, 0.0),
    "below": (0.0, -1.0, 0.0),
    "far_right": (2.0, 0.0, 0.0),
    "far_left": (-2.0, 0.0, 0.0),
    "far_front": (0.0, 0.0, 5.0),
    "far_behind": (0.0, 0.0, -5.0)
}

def resolve_position(pos) -> Tuple[float, float, float]:
    if isinstance(pos, str):
        return POSITION_PRESETS.get(pos, POSITION_PRESETS["center"])
    if pos is None:
        return POSITION_PRESETS["center"]
    return tuple(pos)

class AudioManager:
    def __init__(self):
        self._sounds: Dict[str, object] = {}
        self._ambient = None

    def load(self, filename: str):
        path = Path(filename)
        key = str(path)
        if key in self._sounds:
            return self._sounds[key]
        src = oalOpen(key)
        self._sounds[key] = src
        return src

    def play_effect(self, filename: str, position=None):
        try:
            src = self.load(filename)
            pos = resolve_position(position)
            try:
                src.set_position(pos)
            except Exception:
                try:
                    src.position = pos
                except Exception:
                    pass
            try:
                src.play()
            except Exception:
                try:
                    src.resume()
                except Exception:
                    pass
        except Exception:
            pass

    def play_ambient(self, filename: str, position=None):
        try:
            if self._ambient:
                try:
                    self._ambient.stop()
                except Exception:
                    pass
            src = self.load(filename)
            pos = resolve_position(position)
            try:
                src.set_position(pos)
            except Exception:
                try:
                    src.position = pos
                except Exception:
                    pass
            try:
                src.set_looping(True)
            except Exception:
                try:
                    src.set_loop(True)
                except Exception:
                    try:
                        src.looping = True
                    except Exception:
                        pass
            try:
                src.play()
            except Exception:
                try:
                    src.resume()
                except Exception:
                    pass
            self._ambient = src
        except Exception:
            pass

    def stop_ambient(self):
        if self._ambient:
            try:
                self._ambient.stop()
            except Exception:
                pass
            self._ambient = None

    def stop_all(self):
        for snd in list(self._sounds.values()):
            try:
                snd.stop()
            except Exception:
                pass

    def close(self):
        self.stop_all()
        try:
            oalQuit()
        except Exception:
            pass
