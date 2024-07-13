from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.callbacks import get_openai_callback

# create the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=.2, verbose=True)

prompt = ChatPromptTemplate.from_messages([
   ('system', """
      You are a comedian. If the topic is offensive, crude or tasteless say 
      I am a G-rated comedian.
   """),
   ('human', 'Tell me me a joke on the {topic}')
])

topic = 'faeces'
prompt_text = prompt.invoke({ 'topic': topic })
result = llm.invoke(prompt_text)

print(result.content)
