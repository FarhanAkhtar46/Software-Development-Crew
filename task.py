from crewai import Task
from textwrap import dedent
 
class SoftwareDevelopmentTasks:
    def documentation_creation(self, agent, software_idea):
        return Task(description=dedent(f"""\
            Create a comprehensive Software Requirements Specification (SRS) document for the software idea: {software_idea}.
 
            The SRS should include:
            - Functional requirements
            - Non-functional requirements
            - Use cases
            - User stories
 
            Pay attention to detail to ensure all aspects of the software idea are covered.
            """),
            agent=agent,
            expected_output="Comprehensive SRS document covering all specified sections."
        )
 
    def architecture_design(self, agent, software_idea):
        return Task(description=dedent(f"""\
            Design the system architecture and create flow diagrams for the software idea: {software_idea}.
 
            The architecture should cover:
            - High-level design
            - Component diagrams
            - Sequence diagrams
            - Data flow diagrams
 
            Ensure the design is scalable and meets the requirements outlined in the SRS document.
            """),
            agent=agent,
            expected_output="System architecture design with all required diagrams."
        )
 
    def code_development(self, agent, software_idea):
        return Task(description=dedent(f"""\
            Develop the software solution and write code based on the software idea: {software_idea}.
 
            The development should include:
            - Implementing the architecture
            - Writing clean and maintainable code
            - Following best practices and coding standards
 
            Ensure the code is functional and meets the specified requirements.
            """),
            agent=agent,
            expected_output="Functional and maintainable codebase meeting specified requirements."
        )
 
    def unit_testing(self, agent, software_idea):
        return Task(description=dedent(f"""\
            Provide unit testing steps on the provided solution for the software idea: {software_idea}.
 
            The testing should cover:
            - Functional tests
            - Edge cases
            - Performance tests
 
            Provide steps for performing above testing on given development code.
            """),
            agent=agent,
            expected_output="Steps for performing unit testing on given development code."
            
        )
 
 