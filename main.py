import os
from openai import OpenAI
from whisper_tools import transcribe_audio

client = OpenAI()

response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
				{"role": "system", "content": """You are an advanced novel-writing individual. Please take this small piece of writing and add words before and after to form a complete segment of a story."""},
                {"role": "user", "content": transcribe_audio("ignore\\vlc-record.mp3")}
                ],
            temperature=0.6
            )

print(response.choices[0].message.content)
