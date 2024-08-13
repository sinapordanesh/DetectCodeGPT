import os
import openai
import json
import time
import sys
import argparse


# Access the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configuration for GPT-4
temperature = 0.7
max_tokens = 300
model = "gpt-4"

def clean_up_prompt(prompt):
    # Remove any occurrences of backticks and "python" keyword
    prompt = prompt.replace("```python", "")
    prompt = prompt.replace("```", "")
    return prompt.strip()

def generate_transformed_prompt(original_prompt):
    # Engineered prompt to send to GPT
    gpt_prompt = f"""
Hey GPT, I need to convert the following code generation prompt into a different format. Please transform the provided prompt into a Python function definition with a docstring, similar to the example given. Ensure that your response contains only the final transformed prompt, with no additional text, as I will be storing it directly in a spreadsheet.

Original Prompt:
"{original_prompt}"

Example of Desired Format:

def example_function(param1, param2):
    \"\"\"
    **Purpose**: Provide a clear and concise description of what the function does.

    :param param1: Description of param1, including its type and any relevant details.
    :param param2: Description of param2, including its type and any relevant details.
    
    [Additional Sections (optional)]: 
        - Any additional notes, such as exceptions raised, compliance notes, or versioning information.

    :return: Description of the return value, including its type.
    \"\"\"

Instructions:
- Only generate the function definition and the docstring.
- Do not generate any actual code, return statements, or print statements inside the function.
- Do not include any code formatting (like ```python), comments, or additional text outside the function and docstring.
- The response should be plain text with only the function definition and the docstring, and nothing else.
- The last character of your response should be the closing quotation mark (") after the docstring.
"""
    # Communicate with GPT API
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": gpt_prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )

    transformed_prompt = response['choices'][0]['message']['content'].strip()
    return clean_up_prompt(transformed_prompt)

def main(input_file, output_file):
    # Load the input JSON file
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    results = []

    for i, item in enumerate(data):
        original_prompt = item['prompt']
        
        # Show iteration process visually
        sys.stdout.write(f"\rProcessing prompt {i + 1} of {len(data)}...")
        sys.stdout.flush()
        
        # Generate the transformed prompt
        transformed_prompt = generate_transformed_prompt(original_prompt)
        
        # Collect the transformed prompt
        results.append({"original_prompt": original_prompt, "transformed_prompt": transformed_prompt})
        
        # Sleep to prevent hitting rate limits
        time.sleep(1)  # Adjust if necessary

    # Save results to the output JSON file
    with open(output_file, 'w') as outfile:
        json.dump(results, outfile, indent=4)
    
    print("\nProcessing complete.")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default="input.json")
    parser.add_argument('--output', type=str, default="output.json")
    args = parser.parse_args()
    
    input_path = args.input
    output_path = args.output
    main(input_path, output_path)
