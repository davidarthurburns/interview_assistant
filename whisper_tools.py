from openai import OpenAI
from docx import Document
import tempfile

client = OpenAI()


def transcribe_audio(path):
    with open(path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
    return transcription


def generate_audio(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=text
    )
    filename = tempfile.mktemp(prefix='assistant_response', suffix='.wav', dir='ignore')
    response.stream_to_file(filename)
    return filename
