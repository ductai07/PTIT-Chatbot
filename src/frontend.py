import streamlit as st
import requests
import json

# URL của API FastAPI
API_URL = "http://127.0.0.1:6060/answer/"

st.title(" 🤖 PTIT Chatbot")

st.write("A simple chatbot for PTIT students built by DucTaiTran.")

question = st.text_input("Xin chào, tôi có thể giúp gì cho bạn?")


if st.button("Gửi"):
    if question:
        # Gửi yêu cầu POST đến API FastAPI
        response = requests.post(API_URL, json={"question": question})
        
        if response.status_code == 200:
            # Hiển thị câu trả lời từ chatbot
            answer = response.json().get("answer")
            st.write(f"Câu trả lời: {answer}")
        else:
            st.write("Đã xảy ra lỗi khi gọi API.")
    else:
        st.write("Vui lòng nhập câu hỏi.")


# python -m streamlit run frontend.py
