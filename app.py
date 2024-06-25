import streamlit as st
from dotenv import load_dotenv
import os
from textwrap import dedent
from crewai import Agent, Crew
from task import SoftwareDevelopmentTasks
from agents import SoftwareDevelopmentAgents

load_dotenv()

def main():



    # Load images
    banner_image = "images/NathcorpLogo-Text-side_400x53.png"  # Replace with your banner image path
    logo_image = "images\png-transparent-goal-definition-product-marketing-do-not-care-text-logo-plan.png"  # Replace with your logo image path
    # Display banner image
    st.image(banner_image, use_column_width=True)
    # Create columns for logo, title, and dropdown
    
    

    

    

    
    

    st.title("Software Development Crew")
    st.subheader("Welcome to the Software Development Crew")

    software_idea = st.text_input("Enter the software idea:", "school management system")

    def save_to_file(content, filename):
        with open(filename, 'w') as file:
            file.write(content)

    if st.button("Run Crew"):
        st.write("Running the Software Development Crew...")

        # Initialize tasks and agents
        tasks = SoftwareDevelopmentTasks()
        agents = SoftwareDevelopmentAgents()

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
                project_manager_agent
                
            ],
            tasks=[
                documentation_creation
            ],
            verbose=True
        )

        doc_arch_crew2 = Crew(
        agents = [
            architect_agent 
        ],
        tasks = [
            architecture_design
        ],
        verbose=True
        )

        st.write("Starting Documentation Crew...")
        doc_arch_results = doc_arch_crew.kickoff()
        st.write("Starting Architecture Crew...")
        doc_arch_results2 = doc_arch_crew2.kickoff()
        st.write("Documentation and Architecture Crew completed.")

        

        # Create Crew responsible for Development and Testing
        dev_crew = Crew(
            agents=[
                developer_agent
                
            ],
            tasks=[
                code_development
                
            ],
            verbose=True
        )

        Test_crew = Crew(
            agents=[
                tester_agent
            
            ],
            tasks=[
                unit_testing

            ],
            verbose=True
        )

        st.write("Starting Development Crew...")
        dev_test_results = dev_crew.kickoff()
        st.write("Starting Testing Crew...")
        dev_test_results2 = Test_crew.kickoff()
        st.write("Development and Testing Crew completed.")

        # Debug information
        st.write("Documentation and Architecture Results:")
        st.write(doc_arch_results)
        st.write(doc_arch_results2)

        # Save Documentation and Architecture outputs to files
        if len(doc_arch_results) >= 2:
            doc_result = doc_arch_results
            arch_result = doc_arch_results2
            save_to_file(doc_result, 'SRS_documentation.txt')
            save_to_file(arch_result, 'High_level_design_documentation.txt')
        else:
            st.error("Error: Incomplete results from Documentation and Architecture Crew")

        # Debug information
        st.write("Development and Testing Results:")
        st.write(dev_test_results)
        st.write(dev_test_results2)

        # Save Development output to a file
        if len(dev_test_results) >= 2:
            dev_result = dev_test_results
            test_result = dev_test_results2
            save_to_file(dev_result, 'Developed_code.txt')
            save_to_file(test_result, 'Test_results.txt')
        else:
            st.error("Error: Incomplete results from Development and Testing Crew")

        # Display results
        # st.write("## Results")
        # st.write("### Documentation and Architecture")
        # st.write("#### SRS Documentation")
        # st.write(doc_result)
        # st.write("#### High Level Design Documentation")
        # st.write(arch_result)
        # st.write("### Development and Testing")
        # st.write("#### Developed Code")
        # st.write(dev_result)
        # st.write("#### Unit Testing Results")
        # st.write(test_result)

        st.success('Files saved successfully!')
if __name__ == "__main__":
    main()