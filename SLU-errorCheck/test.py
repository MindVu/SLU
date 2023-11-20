import json

# Define the error correction mapping
error_correction_mapping = {
    "duration": "time at",
    "error2": "correction2",
    # Add more error-correction pairs as needed
}

# Define input and output file paths
input_file_path = "train.jsonl"
output_file_path = "output.jsonl"

# Open the input and output files
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        try:
            data = json.loads(line)
            # Function to recursively check and correct values
            def check_and_correct(obj):
                if isinstance(obj, dict):
                    for key, value in obj.items():
                        if isinstance(value, str) and value in error_correction_mapping:
                            obj[key] = error_correction_mapping[value]
                        else:
                            check_and_correct(value)
                elif isinstance(obj, list):
                    for i, item in obj:
                        check_and_correct(item)
            check_and_correct(data)
            # Write the corrected data to the output file
            output_file.write(json.dumps(data) + '\n')
        except json.JSONDecodeError:
            # Handle invalid JSON lines if necessary
            print(f"Invalid JSON in line: {line}")

print("Error correction and replacement complete.")
