import os
from dotenv import load_dotenv
import google.generativeai as genai 
import streamlit as st
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel("gemini-1.5-flash")
st.title("Haber özeti")
st.write("Haberi yaz")
def get_response(txt,mdl):
    response=mdl.generate_content("haberi özetle max3 cümle: "+txt)
    return response.text


with st.form("form1"):
    text = st.text_area(" ")
    submitted = st.form_submit_button("Gönder") 


if submitted:
    if not text.strip(): 
        st.error("Lütfen önce bir haber girin!")
    else:
        st.success(get_response(text, model))

