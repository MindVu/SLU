import json

def modify_json(json_file_path, output_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    modified_data = {}
    for intent, combinations in data.items():
        modified_combinations = []
        for combination in combinations:
            modified_combination = {}
            for entity, value in combination.items():
                if isinstance(value, str):
                    modified_combination[entity] = {"value": value}
                else:
                    modified_combination[entity] = value
            modified_combinations.append(modified_combination)

        modified_data[intent] = modified_combinations

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(modified_data, output_file, ensure_ascii=False, indent=4)

# Example usage
json_file_path = 'output_last.json'
output_file_path = 'output_lasttest.json'
modify_json(json_file_path, output_file_path)
