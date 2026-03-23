import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel('gemini-2.5-flash')

def queryapi(prompt):
    try:
        response=model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
if __name__ == "__main__":
    userprompt=input("Enter your prompt: ")
    print("Querying API...")
    result=queryapi(userprompt)
    print("Response:\n" + result)