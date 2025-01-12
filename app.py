import streamlit as st

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

def main():
    st.set_page_config("QA with documents")
    
    doc = st.file_uploader("Upload your document")
    
    st.header("QA with Documents(Information Retrieval)")
    
    user_question= st.text_input("Ask your question")
    
    if st.button("Submit & Process"):
        with st.spinner("Finding Your Answer..."):
            document = load_data(doc)
            model = load_model()
            query_engine = download_gemini_embedding(model,document)
            
            response = query_engine.query(user_question)
            
            st.write(response.response)
            
            
if __name__ == "__main__":
    main()