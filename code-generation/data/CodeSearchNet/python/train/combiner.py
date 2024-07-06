import gzip
import json
import os

def extract_and_combine_files(input_dir, output_file):
    with open(output_file, 'w') as outfile:
        for i in range(1, 16):
            input_file = os.path.join(input_dir, f"{i}.jsonl.gz")
            print(f"Processing {input_file}")

            with gzip.open(input_file, 'rt') as infile:
                for line in infile:
                    json_data = json.loads(line)
                    outfile.write(json.dumps(json_data) + '\n')

    print(f"Combined file saved as {output_file}")

if __name__ == "__main__":
    input_directory = 'path/to/your/jsonl.gz/files'  # Replace with the path to your files
    output_file = 'combined.jsonl'
    
    extract_and_combine_files(input_directory, output_file)
