import streamlit as st
import google.generativeai as genai
from docx import Document

st.set_page_config(page_title="Synthium FAQ Bot")

api_key = st.secrets["AQ.Ab8RN6IS_9spA6jIrdIzDCqRSiIOfAFF6fs2rne_PGTEwRlQGA"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def load_document():
    doc = Document("Synthium_FAQ_Bot_Document.docx")
    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text

DOCUMENTATION = load_document()

st.title("🤖 Synthium FAQ Bot")

question = st.text_input("Ask a question about Synthium")

if question:

    prompt = f"""
    You are the official FAQ assistant for Synthium.

    Answer ONLY from the provided documentation.

    If the answer is not available in the documentation,
    reply:

    "I couldn't find that information in the Synthium documentation."

    Documentation:
    {DOCUMENTATION}

    User Question:
    {question}
    """

    response = model.generate_content(prompt)

    st.write(response.text)
