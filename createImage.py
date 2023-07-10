import os
import openai
from createQuery import generatePrompt
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
PROMPT = generatePrompt()

def generateImageURL():
    
    response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size="256x256",
    )
    print(response["data"][0]["url"])
    return response["data"][0]["url"]
