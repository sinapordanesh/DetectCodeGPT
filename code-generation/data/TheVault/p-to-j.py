import pandas as pd

# Paths to your Parquet files
parquet_file1 = './python-00000-of-00002.parquet'
parquet_file2 = './python-00001-of-00002.parquet'

# Load the Parquet files into DataFrames
df1 = pd.read_parquet(parquet_file1)
df2 = pd.read_parquet(parquet_file2)

# Merge the DataFrames (you can adjust the type of merge as needed)
merged_df = pd.concat([df1, df2], ignore_index=True)

# Convert the merged DataFrame to JSONL format
jsonl_result = merged_df.to_json(orient='records', lines=True)

# Save the JSONL to a file
with open('small_train.jsonl', 'w') as jsonl_file:
    jsonl_file.write(jsonl_result)

print("Merged JSONL file created successfully!")
