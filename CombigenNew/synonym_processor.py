import json
import pandas as pd

def process_synonyms(json_data, excel_file_path):
    for intent_name, combinations_list in json_data.items():
        for combination in combinations_list:
            for entity, details in combination.items():
                # print(entity)
                print(details)
                if details['type'] == 'synonym':
                    # print('ok')
                    process_synonym_entity(entity, details, combination, combinations_list, excel_file_path)

def process_synonym_entity(entity, details, combination, combinations_list, excel_file_path):
    synonym_sheet_name = entity.lower()  # Assuming the sheet name is the lowercase of the entity name
    synonyms_data = pd.read_excel(excel_file_path, sheet_name=synonym_sheet_name)

    # Skip the first column and take values from the column that has the same name as the 'value' field
    synonym_values_column = details['value']
    if synonym_values_column in synonyms_data:
        synonym_values = synonyms_data[synonym_values_column].dropna().tolist()
    else:
        return

    # Add 'example' field that consists of the synonym values
    details['example'] = [details['value']] + synonym_values

    # Add more combinations by replacing the value with the synonym values
    for synonym_value in synonym_values:
        new_combination = combination.copy()
        new_combination[entity] = {'value': synonym_value, 'type': 'synonym', 'example': [details['value']]+synonym_values}
        combinations_list.append(new_combination)

def update_json_with_synonyms(json_file_path, excel_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    process_synonyms(json_data, excel_file_path)

    # Save the updated JSON back to the original file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)
