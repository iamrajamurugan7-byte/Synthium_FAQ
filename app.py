import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Synthium FAQ Bot")

api_key = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

DOCUMENTATION = """
PASTE YOUR SYNTHIUM DOCUMENTATION HERE
"""

st.title("🤖 Synthium FAQ Bot")

question = st.text_input("Ask a question about Synthium")

if question:

    prompt = f"""
    You are the official FAQ assistant for Synthium.

    Answer ONLY using the documentation below.

    If the answer is not present, say:
    'I couldn't find that information in the documentation.'

    Documentation:
    {DOCUMENTATION}

    User Question:
    {question}
    """

    response = model.generate_content(prompt)

    st.write(response.text)
