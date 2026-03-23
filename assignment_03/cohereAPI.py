import os
import cohere
from dotenv import load_dotenv
load_dotenv()
client=cohere.Client(os.getenv("COHERE_API_KEY"))
def queryapi(prompt):
    try:
        response=client.chat(
            message=prompt,
            model="command-a-03-2025" 
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    userprompt=input("Enter your prompt: ")
    print("Querying API...")
    result=queryapi(userprompt)
    print("Response:\n",result)
