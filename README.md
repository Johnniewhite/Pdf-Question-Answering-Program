```markdown
# PDF Question Answering

This project is a Streamlit application that allows users to upload a PDF file and ask questions related to its content. The application uses LangChain and Cohere for question answering and document processing.

## Features

- Upload PDF files
- Split PDF content into smaller chunks
- Create a vector store for efficient document retrieval
- Ask questions related to the PDF content
- Display the answer and relevant source documents

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/pdf-question-answering.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Set up the Cohere API key as an environment variable:

```
export COHERE_API_KEY="your_cohere_api_key"
```

Replace `"your_cohere_api_key"` with your actual Cohere API key.

## Usage

1. Run the Streamlit application:

```
streamlit run main.py
```

2. Upload a PDF file using the file uploader in the Streamlit interface.

3. Enter your question in the text input field.

4. The application will display the answer and relevant source documents from the PDF.

5. You can optionally toggle the "Show source documents" checkbox to view the source documents used to generate the answer.

## Project Structure

- `main.py`: The entry point of the application, handles the Streamlit UI and orchestrates the other modules.
- `pdf_loader.py`: Handles the loading of PDF files from the uploaded file.
- `pdf_splitter.py`: Handles the text splitting of the loaded documents.
- `vector_store.py`: Handles the creation of the vector store using the Qdrant library and CohereEmbeddings.
- `question_answering.py`: Handles the question answering pipeline and the display of results.

## Dependencies

The project relies on the following dependencies:

- Streamlit
- LangChain
- Cohere
- PyPDF2

You can find the complete list of dependencies and their versions in the `requirements.txt` file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

This `README.md` file provides an overview of the project, its features, installation instructions, usage guidelines, project structure, dependencies, and information on contributing and licensing.

Feel free to customize the content according to your specific project requirements or add any additional sections you deem necessary.