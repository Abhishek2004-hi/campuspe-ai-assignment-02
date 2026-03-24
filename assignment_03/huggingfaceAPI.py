import os
import requests
from dotenv import load_dotenv
#load the api key from .env file
load_dotenv()
#this is the huggingface api the endpoint is sending our request t
API_URL="https://router.huggingface.co/v1/chat/completions"
headers={
    "Authorization":f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}",  #secret key
    "Content-Type":"application/json",  #the sending and receiving json data
}
def queryapi(user_prompt):
    payload = {
        "model":"meta-llama/Llama-3.1-8B-Instruct:cerebras",  #the AI model using from Hugging Face
        "messages": [
            {"role": "user", "content": user_prompt}  #the user's prompt as a message
        ]
    }
    #send the request to Hugging Face`
    response = requests.post(API_URL, headers=headers, json=payload)
    #Send back the response as a JSON object
    response.raise_for_status()
    return response.json()
if __name__ == "__main__":
    userprompt=input("Enter your prompt: ")
    print("Querying from HuggingFace API ..... ")
    result=queryapi(userprompt)
    if "choices" in result and len(result["choices"]) > 0:
        print("Response:\n" + result["choices"][0]["message"]["content"])
    else:
        print("Unexpected response format:\n", result)