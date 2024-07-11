from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import create_retriever_tool
from langchain_openai import ChatOpenAI

from langchain.memory import ConversationBufferMemory

from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent

"""
PROMPT

tell me about the book that you are currently reading

are there movie adaptations of the book

who wrote the book

who was the last child that the selfish giant met

what other books did the author wrote
"""


# Create agent
def create_agent(retriever) -> AgentExecutor:
   llm = ChatOpenAI(temperature=0.2, model='gpt-3.5-turbo', streaming=False)

   prompt_search_query = ChatPromptTemplate.from_messages([
      ('system', """
            You are an able assistant. You are here to help the humans with their questions.
            If you don't know the answer, say 'I do not know the answer to that question'"""
      ),
      ('user', """
            Given the following question
               {input}
            look up information relevant to the query"""
      ),
      MessagesPlaceholder(variable_name="chat_history")
   ])

   tools_list = [
      create_retriever_tool(
         retriever= retriever,
         name = "story-search",
         description="Search the Selfish Giant story. Always use this tool if the question pertains to the Selfish Giant",
         document_prompt=prompt_search_query
      )
   ]
   tool_names = [ 'ddg-search', 'wikipedia', 'llm-math' ]

   tools = load_tools(llm=llm, tool_names=tool_names, tools=tools_list)

   memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
   memory.save_context(
      { 'input': 'What are you doing?' },
      { 'output': 'I am reading a story called "The Selfish Giant"' },
   )

   prompt_react = hub.pull('hwchase17/react-chat')

   agent = create_react_agent(llm=llm, tools=tools, prompt=prompt_react)
   executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, memory=memory, 
         verbose=True, handle_parsing_errors=True)

   return executor

