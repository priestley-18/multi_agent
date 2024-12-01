import os
from dotenv import load_dotenv
from crewai import Crew
from tools.web_search_tool import WebSearchTool
from agents import UseCaseGenerationAgents
from tasks import UseCaseGenerationTasks

# Load environment variables
load_dotenv()

def main():
    # Configuration
    company = "Tesla"
    industry = "Automotive and Clean Energy"

    # Initialize tools
    web_search_tool = WebSearchTool().as_tool()

    # Create agents
    agents = UseCaseGenerationAgents(web_search_tool)

    # Create tasks
    tasks = UseCaseGenerationTasks(agents, web_search_tool)

    # Define the crew
    crew = Crew(
        agents=[
            agents.industry_researcher(),
            agents.market_analyst(),
            agents.use_case_generator(),
            agents.resource_curator()
        ],
        tasks=[
            tasks.research_industry(company, industry),
            tasks.analyze_market_trends(industry),
            tasks.generate_use_cases(company, industry),
            tasks.curate_resources(company, industry)
        ],
        verbose=2
    )

    # Run the crew
    result = crew.kickoff()
    print(result)

if __name__ == "__main__":
    main()