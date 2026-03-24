import requests
import json
#no api key needed here ollama runs locally on your own machine
def query_api(prompt):
    url="http://localhost:11434/api/generate"  #this is the local address of ollama is running on computer
    payload={
        "model":"llama2",   #pulled model locally via ollama run llama2
        "prompt":prompt,    #this is the actual question or message from the user
        "stream":False      #it gives full response at once not word by word
    }
    try:
        #send the prompt to ollama running on our machine and wait for the reply
        response=requests.post(url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        return f"Error: {str(e)}"
if __name__ == "__main__":
    userprompt=input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(userprompt)
    print("Response:\n" + result)