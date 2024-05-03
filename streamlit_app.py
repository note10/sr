import streamlit as st

def remove_newlines(text):
    return text.replace('\n', ' ')

def main():
    st.title("줄바꿈 제거 애플리케이션")
    
    # 파일 업로드
    uploaded_file = st.file_uploader("텍스트 파일 업로드", type=['txt'])
    
    if uploaded_file is not None:
        # 업로드된 파일 읽기
        text = uploaded_file.getvalue().decode("utf-8")
        
        # 줄바꿈 제거
        output_text = remove_newlines(text)
        
        # 결과 출력
        st.subheader("줄바꿈 제거 결과:")
        st.text_area("결과", output_text, height=300)

if __name__ == "__main__":
    main()
