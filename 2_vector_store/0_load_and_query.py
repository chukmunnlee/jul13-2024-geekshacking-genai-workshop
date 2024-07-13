from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from langchain_community.document_loaders import UnstructuredEPubLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# load the the book
content = UnstructuredEPubLoader('../ebooks/monkeys_paw.epub').load()

# split the document
text_splitter = RecursiveCharacterTextSplitter(
   chunk_size=1500, chunk_overlap=50, separators=['.', ';', ' ']
)
splits = text_splitter.split_documents(content)

# Load into vector database, Chroma
# create an embedding model
embed_model = OpenAIEmbeddings()
# load the splits into the database
vector_store = Chroma.from_documents(documents=splits, embedding=embed_model)

#values = embed_model.embed_documents(['cat', 'hello, world', 'big black bug bleeds black blood'])
#print(len(values))
#print(len(values[0]))
#print(len(values[1]))
#print(len(values[2]))

# perform a similarity search
results = vector_store.similarity_search_with_score(
   query="what was the last wish", k=5)

for i, r in enumerate(results):
   print('\n---------------')
   #print(f'{r[i].page_content}')
   print(r)