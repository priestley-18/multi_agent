from langchain.tools import Tool
from tavily import TavilyClient
import os

class WebSearchTool:
    def __init__(self):
        self.tavily = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))
    
    def search(self, query: str, max_results: int = 5):
        """Perform web search using Tavily API"""
        try:
            results = self.tavily.search(
                query=query, 
                max_results=max_results,
                search_depth="advanced"
            )
            return "\n".join([
                f"Title: {result['title']}\nURL: {result['url']}\nContent: {result['content']}"
                for result in results['results']
            ])
        except Exception as e:
            return f"Search error: {str(e)}"

    def as_tool(self):
        """Convert to LangChain Tool"""
        return Tool(
            name="web_search",
            func=self.search,
            description="Perform advanced web searches to gather industry and company information"
        )