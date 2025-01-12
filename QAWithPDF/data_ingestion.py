from llama_index.core import SimpleDirectoryReader
import sys
from logger import logging
from exception import MyException


def load_data(data):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        logging.info("data loading started...")
        loader = SimpleDirectoryReader("data")
        document = loader.load_data()
        logging.info("data loading completed...")
        return document
    except Exception as e:
        raise MyException(e,sys)