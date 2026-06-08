import streamlit as st
import google.generativeai as genai
from docx import Document

# Page Configuration
st.set_page_config(
    page_title="Synthium FAQ Bot",
    page_icon="🤖"
)

# Gemini API Key from Streamlit Secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Read Documentation
@st.cache_data
def load_document():
    doc = Document("Synthium_FAQ_Bot_Document.docx")

    text = ""

    for para in doc.paragraphs:
        if para.text.strip():
            text += para.text + "\n"

    return text

DOCUMENTATION = load_document()

# UI
st.title("🤖 Synthium FAQ Bot")
st.write("Ask any question about Synthium Creative Suite.")

question = st.text_input(
    "Enter your question:",
    placeholder="Example: How do I create a new document?"
)

if question:

    with st.spinner("Searching documentation..."):

        prompt = f"""
You are the official FAQ Assistant for Synthium Creative Suite.

IMPORTANT RULES:
1. Answer ONLY using the provided documentation.
2. Do NOT make up information.
3. Do NOT assume anything not present in the documentation.
4. If the answer is not found, respond exactly:

I couldn't find that information in the Synthium documentation.

Documentation:
{DOCUMENTATION}

User Question:
{question}
"""

        try:
            response = model.generate_content(prompt)

            st.success("Answer")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {str(e)}")
