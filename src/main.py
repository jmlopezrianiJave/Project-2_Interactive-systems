# play_test.py
import time
from audioManager import AudioManager

a = AudioManager()
fname = "src/sounds/creak_loop.wav"  # pick any .wav you have
print("Loading", fname)
try:
    snd = a.load(fname)
except Exception as e:
    print("Failed to load:", e)
    raise SystemExit(1)

print("Playing (3s)...")
snd.set_looping(False)
snd.play()

# block so the sound can be heard
time.sleep(3)

print("Done — closing audio.")
a.close()
