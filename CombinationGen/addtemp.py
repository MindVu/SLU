import json
import random

# Load the updated JSON file
with open("output_updated.json", "r", encoding="utf-8") as f:
    combinations_data = json.load(f)


# Function to add "value" and "template" fields to entities
def transform_entities(entity_value):
    if isinstance(entity_value, dict):
        if "example" in entity_value and "value" in entity_value:
            entity_value["template"] = entity_value["value"]
            entity_value["value"] = random.choice(entity_value["example"])
        elif "value" in entity_value:
            entity_value["template"] = entity_value["value"]
        else:
            entity_value["value"] = entity_value["example"][0]
    return entity_value


# Iterate through combinations and transform entities
for intent, combinations in combinations_data.items():
    for combination in combinations:
        for entity, value in combination.items():
            combination[entity] = transform_entities(value)

# Save the updated combinations to a new JSON file
with open("output_final.json", "w", encoding="utf-8") as f:
    json.dump(combinations_data, f, ensure_ascii=False, indent=4)
