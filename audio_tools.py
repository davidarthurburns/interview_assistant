import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import queue
import tempfile
from openai import OpenAI
import sys

freq = 44100
q = queue.Queue()
client = OpenAI()


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())


def record_audio():
    filename = tempfile.mktemp(prefix='user_response_',
                               suffix='.wav', dir='ignore')
    try:
        with sf.SoundFile(filename, mode='x', samplerate=freq, channels=2) as file:
            with sd.InputStream(samplerate=freq, channels=2, callback=callback):
                print("#" * 80)
                print("Press Ctrl+C to stop the recording")
                print("#" * 80)
                while True:
                    file.write(q.get())
    except KeyboardInterrupt:
        print('\nRecording finished: ')
    return filename


def play_audio(filename):
    data, fs = sf.read(filename)
    sd.play(data, fs)
    status = sd.wait()
