from langchain_openai import ChatOpenAI

from langchain.prompts import PromptTemplate
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors.chain_extract import LLMChainExtractor

from langchain_community.callbacks import get_openai_callback

from load_vector_db import load

db_dir = "./chroma_db"

