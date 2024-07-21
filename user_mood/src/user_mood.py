import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

while True:
    
    user_input = input("Enter a phrase and i will tell you if its happy or sad.\n")
    if user_input == "exit" or user_input == "quit":
        break
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "user mood classification bot, print out if user is happy or sad"},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=150,
    )

    response_message = response["choices"][0]["message"]
    print(response_message)
