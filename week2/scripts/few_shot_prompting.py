import os
from dotenv import load_dotenv
import google.generativeai as genai
env_path = os.path.join(os.path.dirname(__file__), '..','..', '.env')
load_dotenv(env_path) 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = genai.GenerativeModel("gemma-3-4b-it")

system="""
soru=6-1
cevap=5

soru=6x5
cevap=30
böyle cevap ver sadece cevabı yaz

"""

print("İşlemi girin:")
user=input()

response=MODEL.generate_content(system+user)
print(response.text)
