import pandas as pd
import os

# Folder containing Excel files
input_folder = "input_files"   # change this to your folder path
output_file = "merged_output.xlsx"

# List to store dataframes
dataframes = []

# Loop through all files in the folder
for file in os.listdir(input_folder):
    if file.endswith(".xlsx") or file.endswith(".xls"):
        file_path = os.path.join(input_folder, file)
        print(f"Reading: {file_path}")
        
        # Read Excel file
        df = pd.read_excel(file_path)
        
        # Optional: Add filename column for reference
        df["Source_File"] = file
        
        dataframes.append(df)

# Merge all dataframes
merged_df = pd.concat(dataframes, ignore_index=True)

# Save to output file
merged_df.to_excel(output_file, index=False)

print(f"\nMerged file saved as: {output_file}")
