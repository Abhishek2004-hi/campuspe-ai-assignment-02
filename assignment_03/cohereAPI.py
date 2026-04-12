import os
import cohere
from dotenv import load_dotenv
#load the api key from .env file
load_dotenv()
#set up the cohere client using the api key stored .env
client=cohere.Client(os.getenv("COHERE_API_KEY"))
#send the user message to the cohere and get a response back
def queryapi(prompt):
    try:
        response=client.chat(
            message=prompt,
            model="command-a-03-2025"  #this is the cohere model using
        )
        #return the text part of the response
        return response.text
    except Exception as e:
         #if something goes wrong print the error instead of crashing
        return f"Error: {str(e)}"

if __name__ == "__main__":
    userprompt=input("Enter your prompt: ")
    print("Querying API...")
    result=queryapi(userprompt)
    print("Response:\n",result)
