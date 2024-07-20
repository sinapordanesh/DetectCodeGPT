"""
This script generates a dataset by combining code and prompts related to specific programming tasks. It processes files from two separate directories: one containing human-written code (solutions) and the other containing machine-generated code (outputs). Additionally, it reads a JSON file containing prompts for these tasks.

The script matches files and prompts based on a common ID pattern found in their names (e.g., 'p00000' corresponds to 'p00000.py' in human code, 'p00000_solution.py' in machine code, and 'p00000.html' in the prompt JSON). Each matched set of prompt, solution, and output is then consolidated into a single record and written to a .txt file in JSON format.

Requirements:
- Python 3.x
- Files must be organized and named as specified:
  * Human-written code files in '/path/to/human_code' ending with '.py'
  * Machine-generated code files in '/path/to/machine_code' ending with '_solution.py'
  * Prompts stored in a JSON file at '/path/to/prompts.json', with 'File_Name' keys ending with '.html'
- All paths and filenames must follow the conventions described for the script to function correctly.

Output:
- The script outputs a '.txt' file containing JSON records. Each record represents a single task and includes:
  * 'prompt': The text describing the task (extracted from the JSON file).
  * 'output': Machine-generated code corresponding to the task.
  * 'solution': Human-written code corresponding to the same task.
"""


import json
import os

# Path setup
human_code_dir = './human_code'
machine_code_dir = './machine_code'
prompt_json_path = './prompts.json'
output_dataset_path = './output_dataset.txt'

# Load the prompts from the JSON file
with open(prompt_json_path, 'r') as file:
    prompts = json.load(file)

# Index prompts by file name for quick lookup
prompt_dict = {prompt['File_Name'].replace('.html', ''): prompt['Prompt'] for prompt in prompts}

# Function to read content from a file
def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Open the output file for writing
with open(output_dataset_path, 'w') as dataset_file:
    # Iterate over human code files
    for filename in os.listdir(human_code_dir):
        if filename.endswith('.py'):
            file_id = filename.replace('.py', '')
            
            # Corresponding machine code file path
            machine_filename = f'{file_id}_solution.py'
            machine_file_path = os.path.join(machine_code_dir, machine_filename)
            
            # Check if both machine code file and prompt exist
            if os.path.exists(machine_file_path) and file_id in prompt_dict:
                # Read contents of human and machine code files
                human_content = read_file_content(os.path.join(human_code_dir, filename))
                machine_content = read_file_content(machine_file_path)
                prompt_content = prompt_dict[file_id]
                
                # Write to the dataset file
                dataset_file.write(json.dumps({
                    'prompt': prompt_content,
                    'output': machine_content,
                    'solution': human_content
                }) + '\n')

print("Dataset creation complete.")
