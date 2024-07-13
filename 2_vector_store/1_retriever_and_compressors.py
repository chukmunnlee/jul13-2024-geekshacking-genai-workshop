from langchain_openai import ChatOpenAI

from langchain.prompts import PromptTemplate
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors.chain_extract import LLMChainExtractor

from langchain_community.callbacks import get_openai_callback

from load_vector_db import load

db_dir = "./chroma_db"

vector_store = load()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)

# Create custom compressor prompt
prompt = PromptTemplate.from_template("""
   Given the following question and context, summarise the context
   that is relevant to answer the question

   Question: {question}
   Context: 
   >>>
      {context}
   >>>
""")

# create context compressor
compressor = LLMChainExtractor.from_llm(llm=llm, prompt=prompt)

# compressor retriever
retriever = ContextualCompressionRetriever(
   base_retriever=vector_store.as_retriever(),
   base_compressor=compressor
)

with get_openai_callback() as cb:
   results = retriever.invoke(
      input='what was the last wish', k=3)

   for i, r in enumerate(results):
      print(r.page_content, r.metadata['source'])
      print()
