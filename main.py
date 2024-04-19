import streamlit as st
from pdf_loader import load_pdf
from pdf_splitter import split_text
from vector_store import create_vector_store
from question_answering import get_answer, display_result

def main():
    # Set page configuration
    st.set_page_config(page_title="PDF Question Answering")

    # Upload PDF file
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file:
        # Load PDF file
        documents = load_pdf(uploaded_file)

        # Text splitting
        all_splits = split_text(documents)

        # Set up the vector store
        db = create_vector_store(all_splits)

        # Get user input
        query = st.text_input("Enter your question:")

        if query:
            # Get answer and display result
            display_result(query, db)

if __name__ == "__main__":
    main()