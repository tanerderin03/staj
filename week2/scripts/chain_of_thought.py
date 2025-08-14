import os
from dotenv import load_dotenv
import google.generativeai as genai
env_path = os.path.join(os.path.dirname(__file__), '..','..', '.env')
load_dotenv(env_path) 



genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = genai.GenerativeModel("gemma-3-4b-it")

system="Soruyu içten içe adım adım değerlendir ama adımları ASLA yazma. Çıktı yalnızca iki satır olsun:\nFinal Answer: <cevap>\nReason: <tek cümlelik kısa gerekçe>"



user=input()

response=MODEL.generate_content(system+user)
print(response.text)
