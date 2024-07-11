from os import path

from langchain_core.vectorstores import VectorStore

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from langchain_community.document_loaders import DirectoryLoader, UnstructuredEPubLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Utility to load Chroma
def load(db_path = './chroma_db', load_dir = '../ebooks') -> VectorStore:
   pass
