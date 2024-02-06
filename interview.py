import os
from openai import OpenAI
from completion_tools import summarize_listing
from audio_tools import record_audio
from whisper_tools import transcribe_audio

client = OpenAI()

model_used = "gpt-3.5-turbo-1106"

ongoing_messages = [
	{"role": "system", "content": """You are an assistant capable of conducting efficient job interviews with candidates.
	Generate one new question at a time and answer the candidate's questions to determine if they meet the requirements and proficiencies described below."""},
	{"role": "system", "content": summarize_listing("ignore\\listing2.txt")}
    ]

while(1):
	assistant_response = client.chat.completions.create(
		model=model_used,
        messages=ongoing_messages,
        temperature=0.6,
    )

	print(assistant_response.choices[0].message.content)
	print()

	ongoing_messages.append({"role": "assistant", "content": assistant_response.choices[0].message.content})
	
	filename = record_audio()
	user_response = transcribe_audio(filename)
	print()

	ongoing_messages.append({"role": "user", "content": user_response})


