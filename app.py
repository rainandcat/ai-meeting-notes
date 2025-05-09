import streamlit as st
import openai
import fitz
import pandas as pd

# OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Meeting Summary Tool", layout="centered")
st.title("AI Meeting Summarizer")

uploaded_file = st.file_uploader("Upload a meeting file (PDF / TXT / CSV)", type=["pdf", "txt", "csv"])

def read_file(file):
    if file.name.endswith(".pdf"):
        text = ""
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".csv"):
        df = pd.read_csv(file)
        return df.to_csv(index=False)
    else:
        return None

def summarize_with_gpt(content):
    response = openai.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You are an assistant that summarizes meeting notes."},
            {"role": "user", "content": f"Please summarize the following content:\n\n{content}"}
        ]
    )
    return response.choices[0].message.content.strip()

if uploaded_file is not None:
    file_content = read_file(uploaded_file)
    if file_content:
        with st.spinner("Summarizing with GPT..."):
            summary = summarize_with_gpt(file_content)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.error("Unsupported file type.")
