from openai import OpenAI
from docx import Document

client = OpenAI()


def summarize_listing(path):
    with open(path, "rt") as listing:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system",
                 "content": "You are an assistant capable of creating concise summaries of long documents."},
                {"role": "user", "content": """Please concisely list the key requirements and proficiencies being looked for
					in applicants for the job described in the following listing."""},
                {"role": "user", "content": listing.read()}
            ],
            temperature=0.6)
    return response.choices[0].message.content
