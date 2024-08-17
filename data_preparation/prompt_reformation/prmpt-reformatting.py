import os
from openai import OpenAI
import json
import time
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed


# Access the API key from the environment variable
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'], 
)
# Configuration for GPT-4
temperature = 0.7
max_tokens = 300
model = "gpt-4o"


def clean_up_prompt(prompt):
    # Remove any occurrences of backticks and "python" keyword
    prompt = prompt.replace("```python", "")
    prompt = prompt.replace("```", "")
    return prompt.strip()


def generate_transformed_prompt(original_prompt, system_prompt="You are a prompt engineer helper", model_name="gpt-4o"):
    
    user_prompt = f"""
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
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ], 
            timeout=360, 
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return clean_up_prompt(response.choices[0].message.content.strip())
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Timeout or error occurred."
    
    
def process_prompt(item):
    original_prompt = item['Prompt']
    file_name = item["File_Name"]
    transformed_prompt = generate_transformed_prompt(original_prompt=original_prompt)
    return {
        "original_prompt": original_prompt, 
        "Prompt": transformed_prompt, 
        "File_Name": file_name
        }


def main(input_file, output_file, max_workers=5):
    # Load the input JSON file
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    results = []
    
    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_prompt = {executor.submit(process_prompt, item): item for item in data}
        
        # i = 0
        for i, future in enumerate(as_completed(future_to_prompt)):
            try:
                result = future.result()
                results.append(result)
                
                # Show iteration process visually
                sys.stdout.write(f"\rProcessed {i + 1} of {len(data)} prompts...")
                sys.stdout.flush()
            except Exception as e:
                print(f"\nError processing prompt {i + 1}: {e}")

    # Save results to the output JSON file
    with open(output_file, 'w') as outfile:
        json.dump(results, outfile, indent=4)
    
    print("\nProcessing complete.")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default="input.json")
    parser.add_argument('--output', type=str, default="output.json")
    parser.add_argument('--workers', type=int, default=5, help="Number of parallel workers")

    args = parser.parse_args()
    
    input_path = args.input
    output_path = args.output
    max_worker = args.workers
    
    main(input_path, output_path, max_worker)
