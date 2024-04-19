import PyPDF2
from langchain.document_loaders import PyPDFLoader
import os
import tempfile

def load_pdf(uploaded_file):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_file_path = temp_file.name

    # Load PDF file
    pdf_loader = PyPDFLoader(temp_file_path)
    documents = pdf_loader.load()

    # Remove the temporary file
    os.remove(temp_file_path)

    return documents