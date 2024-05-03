import re
import streamlit as st

def sort_text(text):
    try:
        lines = text.strip().split('\n')
        sorted_lines = sorted(lines, key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else float('inf'))
        sorted_text = '\n'.join(sorted_lines)
        return sorted_text
    except Exception as e:
        st.error(f"오류 발생: {e}")

def main():
    st.title("텍스트 정렬 애플리케이션")
    
    # 파일 업로드
    uploaded_file = st.file_uploader("텍스트 파일 업로드", type=['txt'])
    
    if uploaded_file is not None:
        content = uploaded_file.getvalue().decode("utf-8")
        
        # 파일 내용 출력
        st.subheader("원본 텍스트:")
        st.text_area("입력", content, height=300)
        
        # 정렬된 결과 출력
        sorted_content = sort_text(content)
        if sorted_content:
            # 숫자로 시작하는 줄의 줄바꿈 제거
            lines = sorted_content.split('\n')
            for i, line in enumerate(lines):
                if re.match(r'^\d+\.', line):
                    lines[i] = line.rstrip()
            sorted_content = '\n'.join(lines)
            
            st.subheader("정렬된 텍스트:")
            st.text_area("결과", sorted_content, height=300)

if __name__ == "__main__":
    main()
