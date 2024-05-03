import streamlit as st
from io import BytesIO

def process_text(text):
    lines = []
    for line in text.split(". "):
        if line.strip().startswith("<"):
            number = line.strip()[1:].split(". ")[0]
            sentence = ". ".join(line.strip()[1:].split(". ")[1:]) + "."
            lines.append((int(number), sentence))

    lines.sort()
    processed_text = ""
    for number, sentence in lines:
        processed_text += f"{number}. {sentence}\n"

    return processed_text

def main():
    st.title("Text Processor")

    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

    if uploaded_file is not None:
        text = uploaded_file.getvalue().decode("utf-8")

        if st.button("Process Text"):
            processed_text = process_text(text)
            
            # 처리된 텍스트를 파일로 저장
            output_file = BytesIO(processed_text.encode("utf-8"))
            output_file.seek(0)  # 포인터를 파일 시작 부분으로 이동

            # 파일 다운로드 링크 생성
            st.download_button(
                label="Download Processed Text",
                data=output_file,
                file_name="processed_text.txt",
                mime="text/plain",
            )

if __name__ == "__main__":
    main()
