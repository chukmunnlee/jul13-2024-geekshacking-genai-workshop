from pydantic.v1 import ValidationError
from typing_extensions import Optional
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import get_openai_callback
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field

"""
PROMPTS
Who is Satoshi, Ash Ketchem
Bulbasaur, Charmander stats
What are Bulbasaur's evolution stages 
Which pokemon is considered the most powerful? Get the stats of that pokemon
"""

class Pokemon(BaseModel):
   """ Pokemon character statistics and description """

   description: str = Field(description="Description")
   name: Optional[str] = Field(description="The Pokemon's name")
   hp: Optional[str] = Field(description="hp")
   defense: Optional[str] = Field(description="defense")
   special_attack: Optional[str] = Field(description="special attack")
   special_defense: Optional[str] = Field(description="special defense")
   speed: Optional[str] = Field(description="Speed")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)
llm_structured = llm.with_structured_output(Pokemon)

prompt = ChatPromptTemplate.from_messages([
   ('system', """
      You are a Satoshi. You can know everything there is to know about Pokemons.
      If the question is not about Pokemon, say 'Please ask Pokemon related questions'.
   """),
   ('human', '{input}')
])

with get_openai_callback() as cb:
   text = input('Question? ')

   prompt_text = prompt.invoke({ 'input': text })
   try:
      response = llm_structured.invoke(prompt_text)
      print('\n----------------\n')
      print(response)
   except ValidationError as err:
      print(f'Error: {err}')
      
   print('\n----------------\n')
   print(cb)
