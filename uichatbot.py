import streamlit as st
import ollama
st.title("chat Bot rafeqha")
st.session_state.messages = [] #msg save ai-me
user_input = st.text_input("You:")
if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    response = ollama.chat(
        model = "gemma3:1b", 
        messages = st.session_state.messages
    )
    reply = response["message"]["content"]  
    st.session_state.messages.append({"role":"assistant","content":reply})
    st.write("Bot: ",reply)

     