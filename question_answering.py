import os
from langchain.llms import Cohere
from langchain.chains import RetrievalQA
import streamlit as st

def get_answer(query, db):
    api_key = os.getenv('COHERE_API_KEY')
    llm = Cohere(model="command", temperature=0.9, cohere_api_key=api_key)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever(), return_source_documents=True)
    result = qa({"query": query})
    return result

def display_result(query, db):
    result = get_answer(query, db)
    st.write(f"Answer: {result['result']}")

    # Display source documents
    if st.checkbox("Show source documents"):
        for doc in result["source_documents"]:
            st.write(doc.page_content)