# import google.generativeai as genai
# genai.configure(api_key="AIzaSyCt0nDBRDjV2dtZ7kLkRk3FzWLbwxd_NLw")

# models = genai.list_models()
# for m in models:
#     print(m.name, m.supported_generation_methods)

# model = genai.GenerativeModel("gemini-2.5-flash")
# response = model.generate_content("Write a haiku about sunrise")
# print(response.text)

import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyCt0nDBRDjV2dtZ7kLkRk3FzWLbwxd_NLw")

model = genai.GenerativeModel("gemini-2.5-flash")
# Initialize conversation history
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🤖 Gemini with KV")

# --- User input ---
user_input = st.text_input("You:")

if st.button("Send") and user_input:
    # Add user message
    st.session_state.history.append({"role": "user", "parts": [user_input]})

    # Generate bot response
    response = model.generate_content(user_input)

    # Add bot response with correct role
    st.session_state.history.append({"role": "model", "parts": [response.text]})

# --- Display conversation ---
for message in st.session_state.history:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['parts'][0]}")
    else:
        st.markdown(f"**Bot:** {message['parts'][0]}")