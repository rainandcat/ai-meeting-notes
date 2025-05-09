# Meeting Summary Assistant 📝🤖

An AI-powered assistant that summarizes meeting transcripts, performs sentiment analysis, and provides basic visualizations using GPT-4 and Streamlit.

## Features

- Upload `.txt` meeting transcripts
- Generate concise summaries using OpenAI GPT-4
- Perform sentiment analysis on the content
- Visualize sentiment trends with matplotlib
- Easy-to-use Streamlit web interface

## Project Structure

.
├── app.py # Main Streamlit app
├── summarizer.py # Handles GPT-based summarization
├── sentiment.py # Performs sentiment analysis
├── visualizer.py # Plots results with matplotlib
├── utils.py # Helper functions (e.g., file reading)
├── requirements.txt # Project dependencies
└── README.md # This file

## How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/rainandcat/ai-meeting-notes.git
cd meeting-summary-assistant
```

2. **Install dependencies**

```
pip install -r requirements.txt
```

3. **Set up your OpenAI API key**

Set your API key as an environment variable:

```
export OPENAI_API_KEY="your_openai_api_key"
```

4. Start the app

```
streamlit run app.py
```

## 🌐Live Demo

Link: https://ai-meeting-notes-b0uc.onrender.com

## 📦Requirements

- Python 3.9+

- openai

- streamlit

- matplotlib

- nltk

## 📄 License

MIT License
