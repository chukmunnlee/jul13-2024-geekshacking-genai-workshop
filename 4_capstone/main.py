from utils import load_ebook, load_to_vector_store
from agent_utils import create_agent

from langchain_community.callbacks.manager import get_openai_callback

## Setup
split_text = load_ebook('../ebooks/the_happy_prince.epub')

vector_store_retriever = load_to_vector_store(split_text)

executor = create_agent(vector_store_retriever)

while True:
   text = input('Question? ')
   if not bool(text.strip()):
      print("Bye bye")
      break

   with get_openai_callback() as cb:
      try:
         result = executor.invoke({ 'input': text })
         print(f'{result["output"]}\n')
      except ValueError as err:
         print(f'ERROR: {err}')

   print(f'\n\n {cb}\n')


