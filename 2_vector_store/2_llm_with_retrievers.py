from langchain_openai import ChatOpenAI
from load_vector_db import load

from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors.chain_extract import LLMChainExtractor

from langchain_community.callbacks import get_openai_callback

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain


db_dir = "./chroma_db"

vector_store = load(db_dir)

