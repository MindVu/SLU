# import json
# import random

# def update_entities(json_data, template_value):
#     for intent, entities in json_data.items():
#         for entity in entities:
#             entity_name, entity_info = entity.popitem()

#             # Handle the case where 'value' is not present
#             # value = entity_info.get("value", None)

#             # Check if 'value' matches the specified template and handle different types
#             if value == template_value:
#                 example_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']  # Replace with your example values
#                 entity_info["example"] = example_values
#                 entity_info["template"] = template_value
#                 entity_info["value"] = random.choice(example_values)

#     return json_data

# # Load your JSON data
# with open("output_lasttest.json", "r", encoding="utf-8") as file:
#     json_data = json.load(file)

# # Specify the template value to check in the 'value' field
# template_value = "<int>"  # Replace with your template value

# # Update the entities
# updated_json_data = update_entities(json_data, template_value)

# # Save the updated JSON data to a new file
# with open("updated_json_file.json", "w", encoding="utf-8") as file:
#     json.dump(updated_json_data, file, ensure_ascii=False, indent=4)
import json
import random

def update_entities(json_data, template_value):
    for intent, entities in json_data.items():
        for entity in entities:
            entity_name, entity_info = entity.popitem()

            # Handle the case where 'value' is not present or is a float
            if isinstance(entity_info, dict):
                value = entity_info.get("value")
                if isinstance(value, (str, int)):
                    # Check if 'value' matches the specified template
                    if value == template_value:
                        example_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']  # Replace with your example values
                        entity_info["example"] = example_values
                        entity_info["template"] = template_value
                        entity_info["value"] = random.choice(example_values)

    return json_data

# Load your JSON data
with open("output_lasttest.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)

# Specify the template value to check in the 'value' field
template_value = "<int>"  # Replace with your template value

# Update the entities
updated_json_data = update_entities(json_data, template_value)

# Save the updated JSON data to a new file
with open("updated_json_file.json", "w", encoding="utf-8") as file:
    json.dump(updated_json_data, file, ensure_ascii=False, indent=4)

