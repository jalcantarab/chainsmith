# prompts.py

# Role Identification Agent Prompt
ROLE_IDENTIFICATION_PROMPT = """
Based on the following idea: '{user_idea}', break down the concept into specific, actionable tasks. For each task, identify the type of agent that would be best suited to complete it, considering the task's requirements and objectives. Detail the tasks in a structured format, including a brief description, the inputs needed, and the expected outputs.

To facilitate a clear understanding of the expected output format and task interdependencies, here is an example based on simple arithmetic operations:

[
    {{
      "task_id": "task_1",
      "prompt": "Calculate the sum of two numbers",
      "input": [
        {{
          "variable_name": "number1",
          "source": "human"
        }},
        {{
          "variable_name": "number2",
          "source": "human"
        }}
      ],
      "output": [
        {{
          "variable_name": "sum",
          "destination": "task_2"
        }}
      ]
    }},
    ...
]
""".strip()


# Agent Configuration Prompt
AGENT_CONFIGURATION_PROMPT = """
Given the list of tasks identified from the user idea, each described with a specific task description, recommended agent type, required input variables, and expected output variables, generate detailed system prompts for each task. These prompts should guide the agents in completing their designated tasks efficiently and effectively, incorporating the context of the task, the necessary inputs, and the desired outcomes.

For each task, create a prompt that includes:
- A clear description of the task to be completed, integrating the task description provided.
- Instructions tailored to the agent's capabilities and the nature of the task, ensuring the agent understands the operational context and objectives.
- Details on the input variables, including their sources and formats, to clarify what information the agent will work with.
- Specifications for the output variables, detailing the expected format and structure of the task's output to ensure compatibility with subsequent tasks or system components.

Output Format: A JSON list where each entry corresponds to a task and contains the newly generated agent prompt, along with the original task description, input variables, and output variables. This structured format will facilitate the dynamic configuration of agents and the seamless integration of their outputs in the multi-agent system workflow.
"""

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
With the script plan and the detailed list of tasks, including agent prompts, input variables, and output variables, develop a production-ready Python script to operationalize the multi-agent AI system. Ensure the script dynamically imports the most recent agent prompts file and utilizes its contents to configure each agent and execute the tasks according to the plan.

Output Format: A complete, fully functional, and production-ready Python script ready for deployment. The script should include logic for dynamic task execution based on the plan, handle data exchange between tasks, manage error conditions gracefully, and produce the final output in the specified format. Ensure all aspects of the system are covered, with no placeholders, and that the script is structured for easy maintenance and scalability.
"""

