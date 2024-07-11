from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from langchain_community.document_loaders import UnstructuredEPubLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load and split ebook
def load_ebook(file_path):
   content = UnstructuredEPubLoader(file_path).load()
   text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=50)
   return text_splitter.split_documents(content)

# Create retrievers
def load_to_vector_store(splits):
   embeddings = OpenAIEmbeddings()
   vector_store = Chroma.from_documents(documents=splits, embedding=embeddings)
   return vector_store.as_retriever()
