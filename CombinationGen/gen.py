# import pandas as pd
# import random
# import json

# xls = pd.ExcelFile("SLUdataset.xlsx")
# intents = [
#     "Tra cứu thời tiết",
#     "tra cứu lịch ",
#     "đặt lịch ",
#     "liên hệ",
#     "đặt đồ ăn",
#     "hỏi thông tin",
#     "bật nhạc",
#     "công thức nấu ăn",
#     "gọi taxi",
#     "tra cứu đường đi",
#     "đặt vé",
#     "gợi ý phim",
#     "gợi ý địa điểm",
#     "xóa lịch",
# ]
# output_path = "output.json"
# entity_count_path = "entity_count.txt"
# total_combinations = 500


# # Function to generate combinations with specific names included (up to 6 elements)
# def generate_combinations_with_specific_names(
#     names, specific_names, max_combinations=35, df=None
# ):
#     combinations = []
#     combinations_with_value = []
#     count = 0
#     for leng in range(0, 7):
#         for _ in range(max_combinations):
#             random.shuffle(names)  # Exclude the first column
#             valid_combination = [name for name in specific_names if name in names[1:]]
#             num_additional_elements = min(leng, len(names) - len(valid_combination) - 1)
#             valid_combination += random.sample(
#                 [name for name in names[1:] if name not in valid_combination],
#                 num_additional_elements,
#             )
#             # Sort the combination to ensure uniqueness
#             sorted_combination = sorted([names[0]] + valid_combination)
#             if sorted_combination not in combinations:
#                 combinations.append(sorted_combination)
#                 comb = []
#                 for entity in sorted_combination:
#                     value = str(random.choice(df[entity]))
#                     if value == "nan":
#                         value = df[entity][0]
#                     entity_values = [f"{entity}: {value}"]
#                     comb += entity_values
#                 combinations_with_value.append(comb)
#                 # Include the first column in the combinations
#                 count = count + 1

#     return combinations_with_value, count


# # Track the columns that have already been included
# included_columns = set()

# # Generate combinations for each intent
# combinations_data = {}
# entity_count_data = {}

# for intent in intents:
#     df = pd.read_excel(xls, intent)
#     column_names = df.columns[1:].tolist()
#     imps = []

#     # Generate unique combinations with the specific names included (up to 6 elements)
#     combinations, count = generate_combinations_with_specific_names(
#         column_names, imps, df=df
#     )
#     print(f"{intent}: {count}")
#     if not combinations:
#         # Handle the case where no matching columns are found
#         continue

#     # Ensure all columns are included at least once
#     for column in column_names[1:]:
#         if column not in included_columns:
#             included_columns.add(column)

#     # # Count the number of times each entity (column value) appears in the combinations
#     # entity_count = {entity: 0 for entity in column_names}
#     # for combination in combinations:
#     #     for entity in combination[1:]:
#     #         entity_count[entity] += 1

#     # Store the combinations for the intent
#     combinations_data[intent] = combinations
#     # entity_count_data[intent] = entity_count

#     # Check if we have reached the desired total_combinations
#     if (
#         len(included_columns) >= len(column_names) - 1
#         and len(included_columns) >= total_combinations
#     ):
#         break  # Stop if we have included all columns and reached the desired total_combinations

# # Write the combinations to a JSON file with proper encoding
# with open(output_path, "w", encoding="utf-8") as f:
#     json.dump(combinations_data, f, ensure_ascii=False, indent=4)

# # # Write the entity counts to a text file
# # with open(entity_count_path, "w", encoding="utf-8") as f:
# #     for intent, entity_count in entity_count_data.items():
# #         f.write(f"Intent: {intent}\n")
# #         for entity, count in entity_count.items():
# #             f.write(f"{entity}: {count}\n")
# #         f.write("\n")

# import pandas as pd
# import random
# import json

# xls = pd.ExcelFile("SLUdataset.xlsx")
# intents = [
#     "Tra cứu thời tiết",
#     "tra cứu lịch ",
#     "đặt lịch ",
#     "liên hệ",
#     "đặt đồ ăn",
#     "hỏi thông tin",
#     "bật nhạc",
#     "công thức nấu ăn",
#     "gọi taxi",
#     "tra cứu đường đi",
#     "đặt vé",
#     "gợi ý phim",
#     "gợi ý địa điểm",
#     "xóa lịch",
# ]
# output_path = "output.json"
# entity_count_path = "entity_count.txt"
# total_combinations = 500


# # Function to generate combinations with specific names included (up to 6 elements)
# def generate_combinations_with_specific_names(
#     names, specific_names, max_combinations=35, df=None
# ):
#     combinations = []
#     combinations_with_value = []
#     count = 0
#     for leng in range(0, 7):
#         for _ in range(max_combinations):
#             random.shuffle(names)  # Exclude the first column
#             valid_combination = [name for name in specific_names if name in names[1:]]
#             num_additional_elements = min(leng, len(names) - len(valid_combination) - 1)
#             valid_combination += random.sample(
#                 [name for name in names[1:] if name not in valid_combination],
#                 num_additional_elements,
#             )
#             # Sort the combination to ensure uniqueness
#             sorted_combination = sorted([names[0]] + valid_combination)
#             if sorted_combination not in combinations:
#                 combinations.append(sorted_combination)
#                 comb = {}
#                 for entity in sorted_combination:
#                     value = str(random.choice(df[entity]))
#                     if value == "nan":
#                         value = df[entity][0]
#                     comb[entity] = value
#                 combinations_with_value.append(comb)
#                 # Include the first column in the combinations
#                 count = count + 1

#     return combinations_with_value, count


# # Track the columns that have already been included
# included_columns = set()

# # Generate combinations for each intent
# combinations_data = {}
# entity_count_data = {}

# for intent in intents:
#     df = pd.read_excel(xls, intent)
#     column_names = df.columns[1:].tolist()
#     imps = []

#     # Generate unique combinations with the specific names included (up to 6 elements)
#     combinations, count = generate_combinations_with_specific_names(
#         column_names, imps, df=df
#     )
#     print(f"{intent}: {count}")
#     if not combinations:
#         # Handle the case where no matching columns are found
#         continue

#     # Ensure all columns are included at least once
#     for column in column_names[1:]:
#         if column not in included_columns:
#             included_columns.add(column)

#     # # Count the number of times each entity (column value) appears in the combinations
#     # entity_count = {entity: 0 for entity in column_names}
#     # for combination in combinations:
#     #     for entity in combination[1:]:
#     #         entity_count[entity] += 1

#     # Store the combinations for the intent
#     combinations_data[intent] = combinations
#     # entity_count_data[intent] = entity_count

#     # Check if we have reached the desired total_combinations
#     if (
#         len(included_columns) >= len(column_names) - 1
#         and len(included_columns) >= total_combinations
#     ):
#         break  # Stop if we have included all columns and reached the desired total_combinations

# # Write the combinations to a JSON file with proper encoding
# with open(output_path, "w", encoding="utf-8") as f:
#     json.dump(combinations_data, f, ensure_ascii=False, indent=4)

# # # Write the entity counts to a text file
# # with open(entity_count_path, "w", encoding="utf-8") as f:
# #     for intent, entity_count in entity_count_data.items():
# #         f.write(f"Intent: {intent}\n")
# #         for entity, count in entity_count.items():
# #             f.write(f"{entity}: {count}\n")
# #         f.write("\n")


import pandas as pd
import random
import json

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
output_path = "output.json"
# entity_count_path = "entity_count.txt"
total_combinations = 3000
total = 0


def generate_combinations_without_specific_names(names, max_combinations=1000, df=None):
    combinations = []
    combinations_with_value = []
    count = 0
    for leng in range(1, 7):  # Start from 1 to include combinations with only one entity
        for _ in range(max_combinations):
            random.shuffle(names)
            if leng >= len(names):
                valid_combination = names
            else:
                valid_combination = random.sample(names, leng)
            sorted_combination = sorted(valid_combination)
            if sorted_combination not in combinations:
                combinations.append(sorted_combination)
                comb = {}
                for entity in sorted_combination:
                    value = str(random.choice(df[entity]))
                    if value == "nan":
                        value = df[entity][0]
                    comb[entity] = value
                combinations_with_value.append(comb)
                count = count + 1

    return combinations_with_value, count



# Track the columns that have already been included
included_columns = set()

# Generate combinations for each intent
combinations_data = {}
entity_count_data = {}

for intent in intents:
    df = pd.read_excel(xls, intent)
    column_names = df.columns[1:].tolist()
    imps = []

    # Generate unique combinations without specific names included (up to 6 elements)
    combinations, count = generate_combinations_without_specific_names(
        column_names, df=df
    )
    print(f"{intent}: {count}")
    total += count
    if not combinations:
        # Handle the case where no matching columns are found
        continue

    # Ensure all columns are included at least once
    for column in column_names[1:]:
        if column not in included_columns:
            included_columns.add(column)

    # Store the combinations for the intent
    combinations_data[intent] = combinations

    # Check if we have reached the desired total_combinations
    if (
        len(included_columns) >= len(column_names) - 1
        and len(included_columns) >= total_combinations
    ):
        break  # Stop if we have included all columns and reached the desired total_combinations
print(f"Total: {total}")
# # Write the combinations to a JSON file with proper encoding
# with open(output_path, "w", encoding="utf-8") as f:
#     json.dump(combinations_data, f, ensure_ascii=False, indent=4)
