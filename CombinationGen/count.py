import json

def count_entities_in_intents(json_file_path, output_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        intents_data = json.load(json_file)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for intent, entity_list in intents_data.items():
            output_file.write(f"Intent: {intent}\n")
            entity_count = {}

            for entity_info in entity_list:
                for entity, data in entity_info.items():
                    if isinstance(data, dict):
                        entity_value = data.get("value")
                    else:
                        entity_value = data

                    if entity_value is not None:
                        entity_count[entity] = entity_count.get(entity, 0) + 1

            for entity, count in entity_count.items():
                output_file.write(f"{entity}: {count}\n")

            output_file.write("\n")

if __name__ == "__main__":
    json_file_path = "output_final.json"  # Replace with the path to your JSON file
    output_file_path = "entity_count.txt"  # Replace with the desired output file path
    count_entities_in_intents(json_file_path, output_file_path)
