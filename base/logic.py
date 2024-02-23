# Assuming generate_ai_text is in openai_chat.py
from openai_chat import generate_ai_text
import prompts
import json
import re

class MultiAgentSystemGenerator:
    def __init__(self):
        print("System initialized with OpenAI.")

    def generate_completion(self, prompt, temperature=0.111):
        print(f"Sending prompt to OpenAI: {prompt}")
        response = generate_ai_text(prompt, temperature)
        print("Received response from OpenAI.")
        print(f"Response: {response}")
        
        cleaned_response = self.clean_json_response(response)
        print(f"Cleaned JSON response: {cleaned_response}")
        
        return cleaned_response

    def clean_json_response(self, response):
        json_match = re.search(r'(\{.*\}|\[.*\])', response, re.DOTALL)
        if json_match:
            return json_match.group(0)
        else:
            print("No JSON structure found in the response.")
            return response

    def process_user_idea(self, user_idea):
        print(f"Processing user idea: {user_idea}")
        
        role_identification_prompt = prompts.ROLE_IDENTIFICATION_PROMPT.format(user_idea=user_idea)
        print("Generating tasks for role identification...")
        tasks_json = self.generate_completion(role_identification_prompt)
        
        try:
            tasks = json.loads(tasks_json)
            print("Successfully decoded JSON from response.")
            print(f"Tasks identified: {json.dumps(tasks, indent=2)}")
        except json.JSONDecodeError:
            print("Error decoding JSON from response. Response was not in expected JSON format.")
            print(f"Failed JSON content: {tasks_json}")
            return None

        for index, task in enumerate(tasks, start=1):
            print(f"Configuring agent for task {index}...")
            agent_configuration_prompt = prompts.AGENT_CONFIGURATION_PROMPT.format(
                task=task["task"],
                description=task["description"]
            )
            task['agent_prompt'] = self.generate_completion(agent_configuration_prompt)
            print(f"Task {index} configuration: {task['agent_prompt']}")
        
        print("Generating script plan...")
        return tasks  # This is where you stopped; adjust as needed for full functionality.

def main():
    user_idea = "Develop a system to analyze financial documents."
    print(f"Starting system generation for user idea: {user_idea}")
    
    system_generator = MultiAgentSystemGenerator()
    system_script = system_generator.process_user_idea(user_idea)

    if system_script:
        print("Generated System Script successfully:")
        print(system_script)
    else:
        print("Failed to generate system script due to errors.")

if __name__ == "__main__":
    main()