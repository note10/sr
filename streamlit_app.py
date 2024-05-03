import streamlit as st

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

        if st.button("텍스트 수정"):
            processed_text = process_text(text)
            st.text_area("Processed Text", processed_text, height=300)

if __name__ == "__main__":
    main()
