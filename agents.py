from crewai import Agent
from tools.web_search_tool import WebSearchTool

class UseCaseGenerationAgents:
    def __init__(self, web_search_tool):
        self.web_search_tool = web_search_tool
    
    def industry_researcher(self):
        return Agent(
            role='Industry Research Specialist',
            goal='Conduct comprehensive research on the target company and industry',
            backstory='''You are an expert market researcher with deep knowledge of technological 
            trends and industry dynamics. Your mission is to uncover critical insights about 
            the company's market position, technological landscape, and potential AI transformation opportunities.''',
            verbose=True,
            allow_delegation=True,
            tools=[self.web_search_tool]
        )
    
    def market_analyst(self):
        return Agent(
            role='AI Market Analysis Expert',
            goal='Analyze AI and ML trends, benchmark against industry leaders',
            backstory='''You are a strategic technology analyst specializing in AI adoption 
            across industries. Your expertise lies in identifying technological gaps, 
            benchmarking innovation, and mapping out potential AI implementation strategies.''',
            verbose=True,
            allow_delegation=True,
            tools=[self.web_search_tool]
        )
    
    def use_case_generator(self):
        return Agent(
            role='AI Use Case Strategy Consultant',
            goal='Generate innovative and practical AI/ML use cases',
            backstory='''You are a creative problem solver with expertise in translating 
            technological capabilities into actionable business solutions. Your role is to 
            bridge the gap between cutting-edge AI technologies and practical business applications.''',
            verbose=True,
            allow_delegation=True,
            tools=[self.web_search_tool]
        )
    
    def resource_curator(self):
        return Agent(
            role='AI Resource and Dataset Curator',
            goal='Collect and validate relevant AI implementation resources',
            backstory='''You are a meticulous researcher specializing in finding and 
            validating AI and ML resources, datasets, and implementation guides across 
            various platforms and repositories.''',
            verbose=True,
            allow_delegation=True,
            tools=[self.web_search_tool]
        )