import os
from openai import OpenAI
from whisper_tools import transcribe_audio
from completion_tools import summarize_listing

client = OpenAI()

response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
				{"role": "system", "content": """You are an assistant capable of conducting efficient job interviews with candidates.
					Generate ten questions that will determine whether an applicant fills the requirements and desired competencies described here."""},
				{"role": "system", "content": summarize_listing("ignore\\listing1.txt")}
                ],
            temperature=0.6
            )

print(response.choices[0].message.content)
