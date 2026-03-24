import os
import google.generativeai as genai
from dotenv import load_dotenv
#load the api key from .env file
load_dotenv()
#set up the gemini client using the api key stored .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel('gemini-2.5-flash')   #this is the gemini model using
#send the user message to the gemini and get a response back
def queryapi(prompt):
    try:
        response=model.generate_content(prompt)
        return response.text     #return the text part of the response
    except Exception as e:
        return f"Error: {str(e)}" #if something goes wrong print the error instead of crashing
if __name__ == "__main__":
    userprompt=input("Enter your prompt: ")
    print("Querying API...")
    result=queryapi(userprompt)
    print("Response:\n" + result)