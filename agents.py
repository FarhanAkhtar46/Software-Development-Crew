import os
from textwrap import dedent
from crewai import Agent
# from tools.browser_tools import BrowserTools
# from tools.search_tools import SearchTools
from langchain.llms import Ollama
from langchain_community.llms import Ollama
os.environ["OPENAI_MODEL_NAME"]="gpt-4o"

class SoftwareDevelopmentAgents:
    # def __init__(self):
    #     self.llm = Ollama(model=os.environ['MODEL'])
    openai_api_key=os.getenv('OPENAI_API_KEY')

    def project_manager_agent(self):
        return Agent(
            role="Project Manager",
            goal=dedent("""\
                Create comprehensive Software Requirements Specification (SRS) document
                for the given software idea."""),
            backstory=dedent("""\
                As the Project Manager, you are responsible for gathering requirements
                and creating the SRS document to guide the development process."""),
            tools=[
                # BrowserTools.scrape_and_summarize_website,
                # SearchTools.search_internet
            ],
            allow_delegation=False,
            # llm=self.llm,
            verbose=True
        )

    def architect_agent(self):
        return Agent(
            role="Architect",
            goal=dedent("""\
                Design system architecture and create flow diagrams for the given software idea."""),
            backstory=dedent("""\
                As the Architect, you are tasked with designing the system architecture
                and creating flow diagrams based on the SRS document."""),
            tools=[
                # BrowserTools.scrape_and_summarize_website,
                # SearchTools.search_internet
            ],
            # llm=self.llm,
            verbose=True
        )

    def software_developer_agent(self):
        return Agent(
            role="Software Developer",
            goal=dedent("""\
                Provide required code for the software solution."""),
            backstory=dedent("""\
                As the Software Developer, you are responsible for implementing the software
                solution based on the architecture and SRS document."""),
            tools=[
                # BrowserTools.scrape_and_summarize_website,
                # SearchTools.search_internet
            ],
            # llm=self.llm,
            verbose=True
        )

    def tester_agent(self):
        return Agent(
            role="Tester",
            goal=dedent("""\
                Provide unit testing steps on the provided code by software developer."""),
            backstory=dedent("""\
                As the Tester, you ensure the quality and functionality of the developed software
                by performing thorough unit testing."""),
            tools=[
                # BrowserTools.scrape_and_summarize_website,
                # SearchTools.search_internet
            ],
            allow_delegation=False,
            # llm=self.llm,
            verbose=True
        )
    
