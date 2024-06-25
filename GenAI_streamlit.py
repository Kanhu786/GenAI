import streamlit as st
from PIL import Image
import google.generativeai as genai
import pyttsx3
from googletrans import Translator
api_key ="AIzaSyD_QaYjwjbIQY4pBMOdzEs6F7DeF6OHKJA"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')

# Streamlit app
st.title("AI Image Description & Translation")
st.write("Upload an image and enter a prompt. The model will generate a description based on your prompt.")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img)
    user_prompt = st.text_input("Enter your prompt:", value="")
    if st.button('Response'):
        response = model.generate_content([user_prompt, img])
        st.write(response.text)
    # genAI streamlit App
    
