import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100

def record_audio(duration = 5):
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    write("ignore\\recording.wav", freq, recording) 