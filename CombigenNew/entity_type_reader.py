import json
import pandas as pd
import random
import re
file_path = "Build SLU dataset 2.xlsx"
def read_entity_types(file_path):
    entity_types = pd.read_excel(file_path, sheet_name='entity_type')
    return entity_types

def read_annotation_value(file_path):
    annotation_values = pd.read_excel(file_path, sheet_name='chú thích')
    return annotation_values

annotation_values = read_annotation_value(file_path)
def update_json_with_entity_types(json_data, entity_types):
    for intent_name, combinations_list in json_data.items():
        for combination in combinations_list:
            for entity, value in combination.items():
                entity_type = get_entity_type(entity, entity_types)
                value = filling(value)
                if entity_type:
                    combination[entity] = {'value': value, 'type': entity_type}
                else:
                    combination[entity] = {'value': value, 'type': ''}
    # Save the updated JSON back to the original file
    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

def get_entity_type(entity, entity_types):
    for col in entity_types.columns:
        if entity in entity_types[col.strip()].values:
            return col.strip()
    print(entity)
    return None

def filling(value):
    if str(value).isdigit():
        return (str(int(value)))
    try:
        placeholders = re.findall(r'\<\s*(.*?)\s*\>', value)
        if len(placeholders) == 0:
            return value
        for placeholder in placeholders:
            value_list = list(annotation_values[f"<{placeholder}>"].dropna())
            chosen_value = random.choice(value_list)
            value = re.sub(fr'\<{placeholder}\>', str(chosen_value), value)
            value = filling(value)
        return value
    except:

        # print(str(int(value)))
        return str(int(value))