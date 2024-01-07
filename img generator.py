import os
import urllib.request
from datetime import datetime
import openai

openai.api_key=os.getenv("OPENAI_API_KEY") #Your system-environment variable name which has the api-key
user_prompt=input("Write your prompt ")
response=openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
)

image_url=response['data'][0]['url']
print(image_url)

file_name="image"+datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+".png"
urllib.request.urlretrieve(image_url,file_name)
