import config
import os
import openai

openai.organization = "org-mRQBmUYHKZKOcTfdAI7JUwa1"
openai.api_key = os.getenv(config.private_key)
openai.Model.list()

print(config.private_key)