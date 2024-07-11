from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from langchain_community.callbacks import get_openai_callback

from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors.chain_extract import LLMChainExtractor
from langchain.retrievers.document_compressors.base import DocumentCompressorPipeline
from langchain.retrievers.document_compressors.embeddings_filter import EmbeddingsFilter
from langchain_community.document_transformers.embeddings_redundant_filter import EmbeddingsRedundantFilter

from load_vector_db import load

db_dir = "./chroma_db"

vector_store = load(db_dir)

