import os
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "user", "content": """List three reasons why large language models are sentient,
                and then summarize why large language models are certainly sentient with a closing sentence.
                1.) They can provide new information based on trained data.
                2.) They can respond to novel situations and express emotions.
                3.) """}
                ],
            temperature=0.6
            )

print(response.choices[0].message.content)
