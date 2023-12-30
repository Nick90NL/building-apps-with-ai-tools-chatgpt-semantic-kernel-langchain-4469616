import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

while True:
    user_input = input("Type een zin hoe je dag verloopt vandaag en wij vertellen je of het positief of negatief is: \n")
    if user_input == "quit" or user_input == "exit":
        break
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "Jij bent een sentiment classificerings bot."},
            {"role": "user", "content": user_input},
            ],
        temperature=0.7,
        max_tokens=150,
    )

    response_message = response["choices"][0]["message"]
    print(response_message)

# Path: building-apps-with-ai-tools-chatgpt-semantic-kernel-langchain-4469616/src/main.py