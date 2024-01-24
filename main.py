import os
from openai import OpenAI
from whisper_tools import transcribe_audio

client = OpenAI()

response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
				{"role": "system", "content": """You are an interviewer trying to ascertain whether the user would be a good fit for a job as a data scientist. The expectations of this position include: Leading a cross-functional team in the design and deployment of machine learning models, reporting results and breakthroughs to management and executive groups, and staying abreast of current global trends in machine learning and AI. Minimum requirements for this position include: over five years experience in a data scientist role, a Masters in a related STEM field, and the ability to work in the US. After hearing the user's answers, you ask new questions."""},
				{"role": "assistant", "content": """Why do you believe you would be a good fit for this position?"""},
                {"role": "user", "content": transcribe_audio("ignore\\test.mp3")}
                ],
            temperature=0.6
            )

print(response.choices[0].message.content)
