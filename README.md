# Gemini Chatbot

A simple web-based chatbot built using **Google Gemini (Generative AI)** and **Streamlit**. Chat with Gemini models directly from your browser with conversation history.

---

## Features

- Uses **Google Gemini (GenAI)** models for natural language responses.
- Web interface with **Streamlit**.
- Maintains conversation context in session state.
- Simple setup using only an **API key** (no full Google Cloud setup required).

---

## Requirements

- Python 3.9+
- [Streamlit](https://streamlit.io/)
- [Google Generative AI Python SDK](https://pypi.org/project/google-generativeai/)

---

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
```
2.	Install dependencies:
```bash
pip install streamlit google-generativeai
```
3.	Get your Google API key from AI Studio.

## Usage
1.	Open app.py and replace:
```bash
genai.configure(api_key="YOUR_API_KEY_HERE")
```
with your API key.

2.	Run the chatbot:
```bash
streamlit run example.py
```
3.	A browser window will open. Type messages and chat with Gemini!

## Supported Models

•	The default model is "gemini-2.5-flash"

•	To see other available models:
```bash
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_HERE")
models = genai.list_models()
for m in models:
    print(m.name, m.supported_generation_methods)
```
## Notes
•	Only the roles "user" and "model" are valid.

•	Each message uses parts: [text] instead of content.

•	Conversation context is stored in st.session_state.history.

⸻
## License

MIT License

License

MIT License

