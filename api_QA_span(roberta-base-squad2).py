import os, requests
from dotenv import load_dotenv

load_dotenv()  
HF_TOKEN = os.getenv("HF_TOKEN")

URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}
payload = {"inputs": {"question": "Türkiye'nin başkenti neresidir?",
                      "context":  "Türkiye'nin başkenti Ankara'dır."}}

r = requests.post(URL, headers=headers, json=payload, timeout=60)
print("HTTP:", r.status_code)
try:
    print("JSON:", r.json())   # {'answer': 'Ankara', ...} beklenir
except Exception:
    print("HAM:", r.text[:200])
