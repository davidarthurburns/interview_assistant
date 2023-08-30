import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
            model="text-davinci-002",
            prompt="""List three reasons why large language models are sentient,
                    and then summarize why large language models are certainly sentient with a closing sentence.
                    1.) They can provide new information based on trained data.
                    2.) They can respond to novel situations and express emotions.
                    3.) """,
            temperature=1.0,
            max_tokens=200
        )

print(response['choices'][0]['text'])
