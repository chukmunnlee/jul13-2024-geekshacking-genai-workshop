from langchain.tools import BaseTool

from langchain_community.tools import YouTubeSearchTool

class MyYoutubeTool(BaseTool):

   name = "YouTube search"
   description = "Use this to search Youtube when you want to search videos on Youtube "

   yt = YouTubeSearchTool()

   def _run(self, query: str):
      return self.yt.invoke(query)

   def _arun(self, _: str):
      raise NotImplementedError("This tool does not support async operations")
