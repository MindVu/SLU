import pandas as pd
import random
import json
from gen import generate_combinations_without_specific_names

xls = pd.ExcelFile("SLUdataset.xlsx")
intents = [
    "Tra cứu thời tiết",
    "tra cứu lịch ",
    "đặt lịch ",
    "liên hệ",
    "đặt đồ ăn",
    "hỏi thông tin",
    "bật nhạc",
    "công thức nấu ăn",
    "gọi taxi",
    "tra cứu đường đi",
    "đặt vé",
    "gợi ý phim",
    "gợi ý địa điểm",
    "xóa lịch",
]

output_path = "output_finaltest.json"
entity_count_path = "entity_count.txt"
total_combinations = 215
# Function to generate combinations with specific names included (up to 6 elements)
def generate_combinations_with_specific_names(
    names, specific_names, max_combinations=35, df=None
):
    combinations = []
    combinations_with_value = []
    count = 0
    for leng in range(0, 7):
        for _ in range(max_combinations):
            random.shuffle(names)  # Exclude the first column
            valid_combination = [name for name in specific_names if name in names[1:]]
            num_additional_elements = min(leng, len(names) - len(valid_combination) - 1)
            valid_combination += random.sample(
                [name for name in names[1:] if name not in valid_combination],
                num_additional_elements,
            )
            # Sort the combination to ensure uniqueness
            sorted_combination = sorted([names[0]] + valid_combination)
            if sorted_combination not in combinations:
                combinations.append(sorted_combination)
                comb = {}
                for entity in sorted_combination:
                    value = str(random.choice(df[entity]))
                    if value == "nan":
                        value = df[entity][0]
                    comb[entity] = value
                combinations_with_value.append(comb)
                # Include the first column in the combinations
                count = count + 1

    return combinations_with_value, count

# Read existing combinations from the output file
with open(output_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# Track the columns that have already been included
included_columns = set()

# Generate additional combinations for intents with fewer than 215 combinations
for intent in intents:
    # Skip intents that are not in the existing data
    if intent not in existing_data:
        continue

    # Get the existing combinations and count
    combinations = existing_data[intent]
    count = len(combinations)

    # Check if we need to generate more combinations
    while count < total_combinations:
        df = pd.read_excel(xls, intent)
        column_names = df.columns[1:].tolist()
        imps = []

        # Generate additional combinations considering different slot values
        additional_combinations, additional_count = generate_combinations_with_specific_names(
            column_names, imps, max_combinations=total_combinations - count, df=df
        )
        if not additional_combinations:
            break  # Break if no more combinations can be generated

        # Ensure all columns are included at least once
        for column in column_names[1:]:
            if column not in included_columns:
                included_columns.add(column)

        # Update count and add the additional combinations
        count += additional_count
        combinations.extend(additional_combinations)

    # Store the updated combinations for the intent
    existing_data[intent] = combinations

    # Check if we have reached the desired total_combinations
    if (
        len(included_columns) >= len(column_names) - 1
        and len(included_columns) >= total_combinations
    ):
        break  # Stop if we have included all columns and reached the desired total_combinations

# Write the updated combinations to the JSON file with proper encoding
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=4)
