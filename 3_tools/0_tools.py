from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool, BaseTool
from langchain_openai import ChatOpenAI

from langchain_community.agent_toolkits.load_tools import load_tools

from langchain_community.callbacks.manager import get_openai_callback

from langchain.agents import AgentExecutor, create_react_agent

llm = ChatOpenAI(name="gpt-3.5-turbo", temperature=0.1, verbose=True)
tool_names = [ 'llm-math', 'ddg-search' ]
tool_names = [ 'ddg-search', 'wikipedia', 'arxiv', 'stackexchange', 'llm-math' ]
tool_names = [ 'wikipedia', 'arxiv', 'stackexchange', 'llm-math' ]

tools = load_tools(tool_names=tool_names, llm=llm)

prompt_template_text = '''
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}'''

prompt = PromptTemplate.from_template(prompt_template_text)

agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, 
      max_iterations=4, verbose=True, handle_parsing_errors=True)

with get_openai_callback() as cb:
   while True:
      print('============================\n')
      try:
         question = input('Question: ')
         if not bool(question):
            break
         result = executor.invoke({ 'input': question })
         print(result['output'])

      except ValueError as err:
         print(f'ERROR: {err}')

      print('\n\n---------------\n', cb)


