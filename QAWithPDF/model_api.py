import os
import sys
from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
import google.generativeai as genai
from logger import logging
from exception import MyException

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key = GOOGLE_API_KEY)

def load_model():
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        model = Gemini(model_name = "models/gemini-pro",api_key = GOOGLE_API_KEY)
        return model
    except Exception as e:
        raise MyException(e,sys)
