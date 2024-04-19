import os
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.vectorstores import Qdrant

def create_vector_store(all_splits):
    api_key = os.getenv('COHERE_API_KEY')
    embeddings = CohereEmbeddings(model="multilingual-22-12", cohere_api_key=api_key)
    db = Qdrant.from_documents(all_splits, embeddings, location=":memory:", collection_name="all_splits", distance_func="Dot")
    return db