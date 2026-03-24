### AI API Integration Assignment

## What's this about?
So basically, this project connects to 5 different AI services — Groq, Ollama, Hugging Face, Google Gemini, and Cohere — using Python. Each one has its own script. You type something in, the AI responds. That's pretty much it.

## How to get it running
First things first:

* Clone the repo to your computer.
* Make sure Python is installed.
* Run this to install everything you need:
* pip install -r requirements.txt

If you're using Ollama, make sure it's already running on your machine before you try anything.

## Where to get the API keys
You'll need to sign up on each platform and grab a key:

* Groq – Go to https://console.groq.com/ and make a key.
* Ollama – No key needed. Just install it from https://ollama.ai/ and run a model like ollama run llama3.
* Hugging Face – Sign up at https://huggingface.co/, go to settings, and create a free Access Token.
* Google Gemini – Get your key from https://makersuite.google.com/app/apikey.
* Cohere – Sign up at https://dashboard.cohere.com/ and find your key there.

## Don't leak your keys
Create a .env file and put all your keys in there:

* OPENAI_API_KEY
* GROQ_API_KEY
* HUGGINGFACE_API_KEY
* GOOGLE_API_KEY
* COHERE_API_KEY

Then add .env to your .gitignore so it never gets pushed to GitHub by accident.

## Running the scripts

* Just open your terminal and run whichever script you want, like:python GeminiAPI.py

* It'll ask you to type something, and the AI's reply will show up right in the terminal. Nothing complicated.