import streamlit as st
from summarizer import summarize_with_gpt
from sentiment import analyze_sentiment
from visualization import plot_sentiment_analysis
from utils import read_file

# 設定 Streamlit 頁面
st.set_page_config(page_title="Meeting Summary Tool", layout="centered")
st.title("AI Meeting Summarizer with Sentiment Analysis")

# 上傳檔案
uploaded_file = st.file_uploader("Upload a meeting file (PDF / TXT / CSV)", type=["pdf", "txt", "csv"])

if uploaded_file is not None:
    # 讀取檔案內容
    file_content = read_file(uploaded_file)
    
    if file_content:
        # 顯示檔案預覽
        st.subheader("Preview (first 300 characters):")
        st.code(file_content[:300] + "..." if len(file_content) > 300 else file_content, language="text")
        
        if st.button("Generate Summary"):
            with st.spinner("Summarizing with GPT..."):
                summary = summarize_with_gpt(file_content)
            st.subheader("Summary:")
            st.text_area("Summary Output", summary, height=300)

            # 情感分析
            sentiment = analyze_sentiment(file_content)
            sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
            sentiment_counts[sentiment] += 1
            
            st.subheader("🔍 Sentiment Analysis")
            st.write(f"The sentiment of this document is: {sentiment}")

            # 畫圓餅圖
            sentiment_plot = plot_sentiment_analysis(sentiment_counts)
            st.pyplot(sentiment_plot)
    else:
        st.error("Unsupported file type.")
