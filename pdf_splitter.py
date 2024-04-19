from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(documents):
    """
    Split the given documents into smaller chunks.

    Args:
        documents (List[Document]): A list of LangChain Document objects.

    Returns:
        List[Document]: A list of split LangChain Document objects.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(documents)
    return all_splits

__all__ = ['split_text']
