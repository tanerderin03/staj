import os
from dotenv import load_dotenv
import google.generativeai as genai 


load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-flash")


with open("haber.txt") as f:
    text=f.read()



response=model.generate_content("haberi özetle max5 cümle: "+text)


print(response.text)