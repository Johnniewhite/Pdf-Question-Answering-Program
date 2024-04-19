import streamlit as st
import PyPDF2
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.vectorstores import Qdrant
from langchain.llms import Cohere
from langchain.chains import RetrievalQA
import langchain
import os
import tempfile

# Set page configuration
st.set_page_config(page_title="PDF Question Answering")

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_file_path = temp_file.name

    # Load PDF file
    pdf_loader = PyPDFLoader(temp_file_path)
    documents = pdf_loader.load()

    # Remove the temporary file
    os.remove(temp_file_path)

    # Text splitting
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(documents)

    # Set up the vector store
    api_key = os.getenv('COHERE_API_KEY')
    embeddings = CohereEmbeddings(model="multilingual-22-12", cohere_api_key=api_key)
    db = Qdrant.from_documents(all_splits, embeddings, location=":memory:", collection_name="all_splits", distance_func="Dot")

    # Set up Question Answering pipeline
    llm = Cohere(model="command", temperature=0.9, cohere_api_key=api_key)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever(), return_source_documents=True)

    # Get user input
    query = st.text_input("Enter your question:")

    if query:
        # Get answer
        result = qa({"query": query})
        st.write(f"Answer: {result['result']}")

        # Display source documents
        if st.checkbox("Show source documents"):
            for doc in result["source_documents"]:
                st.write(doc.page_content)