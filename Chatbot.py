import streamlit as st

st.title("💬 Pistis GPT")
st.caption("🚀 How can I help you")

st.chat_message("assistant").write("이름을 입력해주세요!")

prompt = st.chat_input()

if prompt != None:
    st.chat_message("user").write(prompt)

if prompt != None:
    st.chat_message("assistant").write(prompt)