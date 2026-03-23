import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))
def queryapi(prompt):
    """Query the Groq API with a prompt"""
    try:
        response=client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
if __name__ == "__main__":
    userprompt=input("Enter your prompt: ")
    print("Querying Groq...")
    result = queryapi(userprompt)
    print("Response:")
    print(result)