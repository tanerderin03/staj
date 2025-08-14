import google.generativeai as genai
from dotenv import load_dotenv
import os

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(env_path)

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model=genai.GenerativeModel("gemini-1.5-flash")


metin = """
Türkiye, Asya ile Avrupa kıtaları arasında yer alan bir ülkedir. Başkenti Ankara’dır.
Coğrafi konumu ve tarihi mirası ile önemli bir turizm merkezidir. Ayrıca kültürel çeşitliliği, 
mutfağı ve doğal güzellikleri ile tanınır.
"""

response=model.generate_content("özetle"+metin)
print(response.text)