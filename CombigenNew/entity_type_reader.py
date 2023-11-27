import json
import pandas as pd

def read_entity_types(file_path):
    entity_types = pd.read_excel(file_path, sheet_name='entity_type')
    return entity_types

def update_json_with_entity_types(json_data, entity_types):
    for intent_name, combinations_list in json_data.items():
        for combination in combinations_list:
            for entity, value in combination.items():
                entity_type = get_entity_type(entity, entity_types)
                if entity_type:
                    combination[entity] = {'value': value, 'type': entity_type}
                else:
                    combination[entity] = {'value': value, 'type': ''}
    # Save the updated JSON back to the original file
    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

def get_entity_type(entity, entity_types):
    for col in entity_types.columns:
        if entity in entity_types[col].values:
            return col
    return None
