from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import get_openai_callback

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", streaming=False)

prompt_text = """
   Answer the following question truthfully. If you do not know the answer, say I don't know.

   Question: {input}
"""

prompt = PromptTemplate.from_template(prompt_text)

text = "What is salvation by faith? Support your answer with verses from the Bible. Answer in traditional Chinese"

result = llm.invoke(prompt.format(input=text))

print(f'Your question: {text}\n')
print(f'Answer: {result.content}')
