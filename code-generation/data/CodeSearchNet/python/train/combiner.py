import gzip
import json
import os

def extract_and_combine_files(input_dir, output_file):
    with open(output_file, 'w') as outfile:
        # List all .jsonl.gz files in the directory
        files = [f for f in os.listdir(input_dir) if f.endswith('.jsonl.gz')]
        files.sort()  # Sort the files if order is important (e.g., numerical order)

        for input_file in files:
            input_path = os.path.join(input_dir, input_file)
            print(f"Processing {input_path}")

            with gzip.open(input_path, 'rt') as infile:
                for line in infile:
                    json_data = json.loads(line)
                    outfile.write(json.dumps(json_data) + '\n')

    print(f"Combined file saved as {output_file}")

if __name__ == "__main__":
    input_directory = './'  # Replace with the path to your files
    output_file = 'train.jsonl'
    
    extract_and_combine_files(input_directory, output_file)
