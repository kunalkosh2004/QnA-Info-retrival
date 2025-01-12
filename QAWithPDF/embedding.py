from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import Settings

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import MyException
from logger import logging

def download_gemini_embedding(model,data):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        gemini_embed_model = GeminiEmbedding(model_name = "models/embedding-001")
        
        logging.info("Embeddings generated.")
        service_settings = Settings
        service_settings.llm = model
        service_settings.embed_model = gemini_embed_model
        service_settings.chunk_size = 800
        service_settings.chunk_overlap = 20
        logging.info("Service Settings Done.")
        
        index = VectorStoreIndex.from_documents(data,service_setting=service_settings)
        logging.info("Index Generated from document")
        
        index.storage_context.persist()
        
        query_engine=index.as_query_engine()
        logging.info("query engine made.")
        return query_engine
    except Exception as e:
        raise MyException(e,sys)