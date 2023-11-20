import json
import random

# Load the generated JSON file
with open("output_updated.json", "r", encoding="utf-8") as f:
    combinations_data = json.load(f)
    
example_list = [
"bùn bò huế",
"phở gà",
"cơm gà",
"cơm rang dưa bò",
"gà quay",
"vịt quay",
"bò hầm",
"mỳ tương đen",
"gà rán",
"bún đậu mắm tôm",
"bánh cuốn",
"bún ốc",
"phở bò",
"cơm tấm",
"pasta",
"trà sữa",
"trà chanh",
"nem nướng",
"bánh ngọt",
"kem",
"hoa quả",
"pizza",
"cà phê"

]
# Iterate through combinations and transform entities
for intent, combinations in combinations_data.items():
    for combination in combinations:
        for entity, values in combination.items():
            if entity == 'dish_name' and values['value'] in example_list:
                values["example"] = example_list

# Save the updated combinations to a new JSON file
with open("output_updated.json", "w", encoding="utf-8") as f:
    json.dump(combinations_data, f, ensure_ascii=False, indent=4)