from gemini_chat import GeminiChat
import prompts
import json

class MultiAgentSystemGenerator:
    def __init__(self):
        self.gemini_chat = GeminiChat()
        print("GeminiChat initialized.")

    def generate_completion(self, prompt):
        # Added more detailed print statements for debugging
        print(f"Sending prompt to GeminiChat: {prompt[:100]}...")  # Print a portion of the prompt for readability
        response = self.gemini_chat.send_message(prompt=prompt)
        print("Received response from GeminiChat.")
        print(f"Response (first 100 chars): {response[:100]}")  # Print a portion of the response
        return response

    def process_user_idea(self, user_idea):
        print(f"Processing user idea: {user_idea}")
        
        role_identification_prompt = prompts.ROLE_IDENTIFICATION_PROMPT.format(user_idea=user_idea)
        print("Generating tasks for role identification...")
        tasks_json = self.generate_completion(role_identification_prompt)
        
        # Attempt to parse the JSON and print the error or success message
        try:
            tasks = json.loads(tasks_json)
            print("Successfully decoded JSON from response.")
            print(f"Tasks identified: {json.dumps(tasks, indent=2)}")
        except json.JSONDecodeError:
            print("Error decoding JSON from response. Response was not in expected JSON format.")
            print(f"Failed JSON content: {tasks_json}")
            return None

        # Assuming tasks is a list of dictionaries after successful parsing
        for index, task in enumerate(tasks, start=1):
            print(f"Configuring agent for task {index}...")
            agent_configuration_prompt = prompts.AGENT_CONFIGURATION_PROMPT.format(agent_roles=json.dumps(task))
            task['agent_prompt'] = self.generate_completion(agent_configuration_prompt)
            print(f"Task {index} configuration: {task['agent_prompt'][:100]}")  # Print a portion for readability
        
        print("Generating script plan...")
        script_planning_prompt = prompts.SCRIPT_PLANNING_PROMPT.format(agent_prompts=json.dumps(tasks), user_idea=user_idea)
        script_plan = self.generate_completion(script_planning_prompt)
        print("Script plan generated.")

        print("Generating system assembly script...")
        system_assembly_prompt = prompts.SYSTEM_ASSEMBLY_PROMPT.format(script_plan=script_plan, agent_prompts=json.dumps(tasks))
        system_script = self.generate_completion(system_assembly_prompt)
        print("System assembly script generated.")

        return system_script

def main():
    user_idea = "Develop a system to manage a smart greenhouse."
    print(f"Starting system generation for user idea: {user_idea}")
    
    system_generator = MultiAgentSystemGenerator()
    system_script = system_generator.process_user_idea(user_idea)

    if system_script:
        print("Generated System Script successfully:")
        print(system_script[:1000])  # Print the first 1000 characters to avoid flooding the console
    else:
        print("Failed to generate system script due to errors.")

if __name__ == "__main__":
    main()
