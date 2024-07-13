from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.callbacks import get_openai_callback

# set the environment variable key OPENAI_API_KEY

# create a LLM
llm = ChatOpenAI(name="gpt-3.5-turbo", temperature=.8)

# create a prompt
prompt = PromptTemplate.from_template("""
   Tell me {count} jokes on {topic}

   Rate the jokes between 1 and 10
""")
prompt_text = prompt.invoke({ 'count': 3, 'topic': 'chicken crossing the road'})

prompt = PromptTemplate.from_template("""
   Answer the following question. If you do not know the answer say I don't know.
   {question}
""")

while True:
   text = input("\n\n Question: ")
   if not bool(text):
      break

   # Instantiate the prompt
   prompt_text = prompt.invoke({ 'question': text })

   with get_openai_callback() as cb:
      # Invoke the LLM
      response = llm.invoke(prompt_text)

      # print the response
      print(response.content)

      # print the stats for the LLM invocation
      print('\n', cb)