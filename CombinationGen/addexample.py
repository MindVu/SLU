import json
import random

# Load the generated JSON file
with open("output_updated.json", "r", encoding="utf-8") as f:
    combinations_data = json.load(f)

# List of example values
example_values = ["<int> đường <street> quận <district>",
                    "<int> phố <street> quận <district>",
                    "số <int> phố <street> quận <district>",
                    "phố <street> quận <district>",
                    "đường <street>"]

# Function to transform an entity into a structured format
def transform_entity(values, value):
    if value == "<address>":
        s = value
        return {"value": random.choice(example_values), "example": example_values, "template": s}
    return values

# Iterate through combinations and transform entities
for intent, combinations in combinations_data.items():
    for combination in combinations:
        for entity, values in combination.items():
            combination[entity] = transform_entity(values, values['value'])
            # print(values['value'])
            # # for v in values['value']:
            # #     print(v)
            
# Save the updated combinations to a new JSON file
with open("output_updated.json", "w", encoding="utf-8") as f:
    json.dump(combinations_data, f, ensure_ascii=False, indent=4)
