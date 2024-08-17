import json
import argparse


def split_jsonl(file_path, num_splits=5):
    # Read the data from the original JSONL file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Determine the size of each chunk
    chunk_size = len(lines) // num_splits

    # Split and write the data into smaller JSONL files
    for i in range(num_splits):
        chunk_lines = lines[i*chunk_size : (i+1)*chunk_size]
        with open(f'{file_path}_part_{i+1}.jsonl', 'w') as chunk_file:
            chunk_file.writelines(chunk_lines)

    # Handle any remaining lines (if len(lines) is not divisible by num_splits)
    remaining_lines = lines[num_splits*chunk_size:]
    if remaining_lines:
        with open(f'{file_path}_part_{num_splits}.jsonl', 'a') as last_chunk_file:
            last_chunk_file.writelines(remaining_lines)

# Example usage

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default="", help="Input file path")
    parser.add_argument('--output', type=str, default="", help="Output files path")
    parser.add_argument('--splits', type=int, default=5, help="Number of desired splits")

    args = parser.parse_args()
    
    input_path = args.input
    output_path = args.output
    num_splits = args.splits
        
    split_jsonl(input_path, num_splits)

