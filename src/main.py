import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": ""},
        {"role": "user", "content": "Say 'Hello world'"}
    ],
    temperature=0.7,
    max_tokens=150,
)

response_message = response["choices"][0]["message"]
print(response_message)

# Path: building-apps-with-ai-tools-chatgpt-semantic-kernel-langchain-4469616/src/main.py