from crewai import Task

class UseCaseGenerationTasks:
    def __init__(self, agents, web_search_tool):
        self.agents = agents
        self.web_search_tool = web_search_tool
    
    def research_industry(self, company, industry):
        return Task(
            description=f'''Conduct an in-depth research on {company} in the {industry} sector.
            - Identify the company's current technological landscape
            - Analyze market position and strategic focus
            - Uncover potential areas for AI transformation
            - Compile a comprehensive market research report''',
            agent=self.agents.industry_researcher(),
            output_file='output/market_research.md'
        )
    
    def analyze_market_trends(self, industry):
        return Task(
            description=f'''Analyze AI and ML trends in the {industry} industry.
            - Benchmark against industry leaders
            - Identify technological gaps and opportunities
            - Create a detailed trend analysis report
            - Highlight potential AI adoption strategies''',
            agent=self.agents.market_analyst(),
            output_file='output/market_trends.md'
        )
    
    def generate_use_cases(self, company, industry):
        return Task(
            description=f'''Generate innovative AI/ML use cases for {company} in the {industry} sector.
            - Create a minimum of 5 unique, practical use cases
            - Align use cases with company's strategic goals
            - Provide technical feasibility assessment
            - Estimate potential business impact and ROI''',
            agent=self.agents.use_case_generator(),
            output_file='output/use_cases.md'
        )
    
    def curate_resources(self, company, industry):
        return Task(
            description=f'''Curate resources for AI implementation in {company}'s {industry}.
            - Find relevant datasets on Kaggle, HuggingFace, GitHub
            - Collect implementation guides and reference architectures
            - Validate resource quality and relevance
            - Compile a comprehensive resource guide''',
            agent=self.agents.resource_curator(),
            output_file='output/resources.md'
        )
