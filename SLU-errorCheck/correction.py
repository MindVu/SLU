import json
# Define a mapping of slot type replacements
slot_type_mapping = {
    'time at': 'duration',
    'duration': 'time at',
    'changing value': 'target number',
    'target number': 'changing value'
}
import json

# Read and process the error.txt file to create an error mapping
error_mapping = {}

def apply_correction(current_ids, current_correction):
    for id in current_ids:
        error_mapping[id] = current_correction
        print(f'ID: {id}, Error: {current_correction}')

with open('error.txt', 'r') as error_file:
    lines = error_file.readlines()
    current_correction = None
    current_ids = []
    for line in lines:
        if line.startswith("Suggest slot type:"):
            if current_correction and current_ids:
                apply_correction(current_ids, current_correction)
            current_correction = line.split(":")[-1].strip()
            current_ids = []
        elif line.startswith("["):
            ids = [id.strip() for id in line.split('[')[1].split(']')[0].split(",")]
            if current_correction:
                current_ids.extend(ids)

# Process each JSONL file
jsonl_files = ['train.jsonl', 'test.jsonl', 'dev.jsonl']

for jsonl_file in jsonl_files:
    corrected_data = []

    with open(jsonl_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        corrected_line = line
        for id, correction in error_mapping.items():
            corrected_line = corrected_line.replace(correction, slot_type_mapping.get(correction, correction))
        corrected_data.append(corrected_line)

    # Write the corrected data back to the JSONL file
    corrected_jsonl_file = jsonl_file.replace('.jsonl', '_corrected.jsonl')
    with open(corrected_jsonl_file, 'w') as corrected_file:
        corrected_file.writelines(corrected_data)

    print(f'Corrected {jsonl_file} and saved as {corrected_jsonl_file}')
