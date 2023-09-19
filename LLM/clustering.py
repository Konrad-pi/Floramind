import os
import openai

API_KEY = open("API_KEY", "r").read()

import openai

openai.api_key = API_KEY

completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0.8,
  max_tokens = 2000,
  messages = [
    {"role": "user", "content": "Write a short poem for programmers."}
  ]
)
print(completion.choices[0].message.content)