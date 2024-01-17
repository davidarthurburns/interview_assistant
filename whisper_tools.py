from openai import OpenAI
from docx import Document

client = OpenAI()

def transcribe_audio(path):
	with open(path, "rb") as audio_file:
		transcription = client.audio.transcriptions.create(
			model="whisper-1", 
			file=audio_file,
			response_format="text")
	return transcription