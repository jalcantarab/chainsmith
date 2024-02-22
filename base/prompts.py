# Role Identification Agent Prompt
# This prompt aims to break down the user's idea into a simple JSON list of tasks.
# In prompts.py, adjust the ROLE_IDENTIFICATION_PROMPT like so:

ROLE_IDENTIFICATION_PROMPT = """
Based on the following idea: '{user_idea}', identify the primary tasks needed to realize this idea, up to 5 tasks maximum. 
List each task with a brief description and any key details necessary for understanding the task's scope and requirements, ensuring each task is simple and actionable. 
The output should be formatted as a JSON list of objects, where each object represents a distinct task necessary to complete the system. 
Each task object should include a 'task' key with a short description as its value, and a 'description' key with a longer, detailed description as its value.

Please ensure the output adheres to proper JSON syntax, including the use of double quotes for strings, and commas to separate items in the list and keys in the objects.

Example Output Format:
[
    {{
        "task": "Define System Requirements",
        "description": "Identify the specific objectives, constraints, and functionalities required for the system."
    }},
    {{
        "task": "Gather Data",
        "description": "Collect relevant financial documents, reports, and records from various sources."
    }}
    // Additional tasks as needed
]
""".strip()



# Detailed Task Configuration Prompt
# This prompt is designed to elaborate on each task, incorporating specific variables (inputs and outputs) for the system prompts.
AGENT_CONFIGURATION_PROMPT = """
Given the task: '{task}', with the following description: '{description}', create a detailed system prompt that outlines how to achieve this task. Include necessary input variables and expected output variables, ensuring that each is clearly defined. The output should be formatted as a JSON object that includes the original task and description, the detailed system prompt, and lists of input and output variables.

Example Output Format:
{{
    "task": "{task}",
    "description": "{description}",
    "system_prompt": "Detailed instructions on how to achieve the task.",
    "input_variables": [
        {{"variable_name": "input1", "source": "Source Description"}},
        
    ],
    "output_variables": [
        {{"variable_name": "output1", "destination": "Destination Description"}},
        
    ]
}}
""".strip()


# Script Planning Prompt
SCRIPT_PLANNING_PROMPT = """
Based on the detailed list of tasks and their corresponding agent prompts, input variables, and output variables, create a comprehensive plan for a multi-agent AI system. This plan should detail how each task is executed by its designated agent, how data flows between tasks, and how the system should handle errors or unexpected inputs. 

Consider the following components in your plan:
- Data Exchange: Specify how the output from one task will be used as input for subsequent tasks. Include any necessary data transformation or integration steps to ensure compatibility between task outputs and inputs.
- Error Handling: Outline strategies for dealing with errors at various stages of task execution. Consider both common errors related to data quality or availability and more complex issues that might arise from interactions between tasks.
- Execution Flow: Describe the sequence in which tasks should be executed, taking into account any dependencies between tasks. Indicate any parallel processing opportunities to optimize the system's efficiency.
- Final Output Format: Define the format and structure of the system's final output, ensuring it meets the user's needs and is suitable for any intended downstream processes or systems.

Output Format: A structured system architecture/technical specification document in JSON format, ready to guide the development of the Python script. This document should include sections for data exchange, error handling, execution flow, and final output format, providing a clear blueprint for building a cohesive and functional multi-agent AI system.
"""

# System Assembly Prompt
SYSTEM_ASSEMBLY_PROMPT = """
With the script plan and the detailed list of tasks, including agent prompts, input variables, and output variables, develop a production-ready Streamlit App Python script to operationalize the multi-agent AI system. Ensure the script dynamically imports the most recent agent prompts file and utilizes its contents to configure each agent and execute the tasks according to the plan.

Output Format: A complete, fully functional, and production-ready Python script ready for deployment. The script should include logic for dynamic task execution based on the plan, handle data exchange between tasks, manage error conditions gracefully, and produce the final output in the specified format. Ensure all aspects of the system are covered, with no placeholders, and that the script is structured for easy maintenance and scalability.
"""

