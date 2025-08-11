import requests
from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}


def summarize(text):
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": 100,
            "min_length": 25,
            "do_sample": False
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"Hata: {response.status_code} - {response.text}")
        return None

    try:
        data = response.json()
        return data[0]["summary_text"]
    except Exception as e:
        print("JSON parse hatası! Ham yanıt:", response.text)
        return None


# Test metni
metin = """
Türkiye, Asya ile Avrupa kıtaları arasında yer alan bir ülkedir. Başkenti Ankara’dır.
Coğrafi konumu ve tarihi mirası ile önemli bir turizm merkezidir. Ayrıca kültürel çeşitliliği, 
mutfağı ve doğal güzellikleri ile tanınır.
"""

ozet = summarize(metin)
print("Özet:", ozet)
