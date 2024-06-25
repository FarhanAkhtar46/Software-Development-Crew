from dotenv import load_dotenv
load_dotenv()

from textwrap import dedent
from crewai import Agent, Crew

from task import SoftwareDevelopmentTasks
from agents import SoftwareDevelopmentAgents

tasks = SoftwareDevelopmentTasks()
agents = SoftwareDevelopmentAgents()

print("## Welcome to the Software Development Crew")
print('------------------------------------------')
software_idea = input("Enter the software idea: ")

# Create Agents
project_manager_agent = agents.project_manager_agent()
architect_agent = agents.architect_agent()
developer_agent = agents.software_developer_agent()
tester_agent = agents.tester_agent()

# Create Tasks
documentation_creation = tasks.documentation_creation(project_manager_agent, software_idea)
architecture_design = tasks.architecture_design(architect_agent, software_idea)
code_development = tasks.code_development(developer_agent, software_idea)
unit_testing = tasks.unit_testing(tester_agent, software_idea)

# Create Crew responsible for Documentation and Architecture
doc_arch_crew = Crew(
    agents=[
        project_manager_agent,
        architect_agent
    ],
    tasks=[
        documentation_creation,
        architecture_design
    ],
    verbose=True
)

doc_arch_result = doc_arch_crew.kickoff()

# Create Crew responsible for Development and Testing
dev_test_crew = Crew(
    agents=[
        developer_agent,
        tester_agent
    ],
    tasks=[
        code_development,
        unit_testing
    ],
    verbose=True
)

dev_test_result = dev_test_crew.kickoff()

# Print results
print("\n\n########################")
print("## Here are the results")
print("########################\n")
print("Documentation and Architecture:")
print(doc_arch_result)
print("\nDevelopment and Testing:")
print(dev_test_result)
