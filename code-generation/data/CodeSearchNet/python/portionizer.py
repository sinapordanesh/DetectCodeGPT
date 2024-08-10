import json

# File paths
input_file = './train.jsonl'
output_file = './train_50.jsonl'

# Define the number of entries you want to extract
n = 50  # Replace with the calculated 1% value if known

# Read the first n entries and write to a new file
with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    for i, line in enumerate(f_in):
        if i >= n:
            break
        f_out.write(line)

print(f'First {n} entries saved to {output_file}')