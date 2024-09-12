import streamlit as st
import pyshorteners

# 제목 설정
st.title("URL 줄이기 앱")

# URL 입력 받기
url = st.text_input("긴 URL을 입력하세요:")

# 버튼을 누르면 URL 줄이기 실행
if st.button("URL 줄이기"):
    if url:
        # URL 줄이기
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        st.success(f"짧은 URL: {short_url}")
    else:
        st.error("URL을 입력하세요.")
