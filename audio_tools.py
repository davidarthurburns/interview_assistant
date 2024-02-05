import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write

freq = 44100

def record_audio(duration = 5):
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    write("ignore\\recording.wav", freq, recording) 