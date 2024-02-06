from openai import OpenAI
from docx import Document

client = OpenAI()

def transcribe_audio(path):
	with open(path, "rb") as audio_file:
		transcription = client.audio.transcriptions.create(
			model="whisper-1", 
			file=audio_file,
			response_format="text"
        )
	return transcription
    
def generate_audio(path):
    with open(path, "r") as text_file:
        response = client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            input = text_file
        )
    
    filename = tempfile.mktemp(prefix='delme_rec_unlimited_', suffix='.wav', dir='ignore')
    response.stream_to_file(filename)
    return filename