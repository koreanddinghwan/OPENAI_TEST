import os
import openai
from dotenv import load_dotenv
from openai.api_resources import completion

load_dotenv()

openai.api_key = os.getenv('GPT_API_KEY')
completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "user",
                "content" : "GPT가 뭔지 설명해줘"
            }
        ]
    )

print(completion.choices[0].message.content)
