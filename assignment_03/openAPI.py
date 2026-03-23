import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv() 
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def queryapi(prompt):
    try:
        response=client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
if __name__ == "__main__":
    userprompt=input("Enter your prompt: ")
    print("Querying OpenAI...")
    result=queryapi(userprompt)
    print("Response:\n", result)