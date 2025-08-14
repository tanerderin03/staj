import os, google.generativeai as genai
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(env_path) 
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model=genai.GenerativeModel("gemini-1.5-flash")

users_input=input()

answer=model.generate_content("shortly answer: "+users_input)

print(answer.text)