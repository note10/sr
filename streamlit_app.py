import streamlit as st
from io import StringIO

def process_text(text):
    lines = []
    for line in text.split(". "):
        if line.strip().startswith("<"):
            number = line.strip()[1:].split(". ")[0]
            sentence = ". ".join(line.strip()[1:].split(". ")[1:]) + "."
            lines.append((int(number), sentence))

    lines.sort()
    processed_text = StringIO()
    for number, sentence in lines:
        processed_text.write(f"{number}. {sentence}\n")

    return processed_text.getvalue()

def main():
    st.title("Text Processor")

    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

    if uploaded_file is not None:
        text = StringIO(uploaded_file.getvalue().decode("utf-8")).read()

        if st.button("Process Text"):
            processed_text = process_text(text)
            st.text_area("Processed Text", processed_text, height=300)

if __name__ == "__main__":
    main()
