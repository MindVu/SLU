# from itertools import combinations
# import random
# import json
# from excel_reader import read_excel

# def generate_combinations(entities):
#     all_combinations = []
#     for r in range(1, len(entities) + 1):
#         entity_combinations = list(combinations(entities, r))
#         all_combinations.extend(entity_combinations)

#     return all_combinations

# def generate_random_combination(entity_columns, intent_data):
#     return [random.choice(intent_data[col].dropna().tolist()) for col in entity_columns]

# def generate_and_save_json(file_path, intents):
#     all_results = {}

#     for intent_name in intents:
#         data = read_excel(file_path, intent_name)
        
#         # Extract entities (columns) excluding the first column (intent name)
#         entity_columns = data.columns[1:]

#         # Generate combinations of entities
#         intent_combinations = generate_combinations(entity_columns)

#         # Create a list to store combinations
#         combinations_list = []

#         # Ensure each intent has at least 215 combinations
#         while len(combinations_list) < 200:
#             # Populate the combinations list
#             for combination in intent_combinations:
#                 combination_values = generate_random_combination(combination, data)
#                 combination_dict = dict(zip(combination, combination_values))
#                 combinations_list.append(combination_dict)
#                 if len(combinations_list) == 200:
#                     break

#         # Save the result for each intent
#         result_json = {intent_name: combinations_list}
#         all_results.update(result_json)

#         # Count the number of combinations and store in a text file
#         num_combinations = len(combinations_list)
#         with open("combinations_count.txt", "a", encoding='utf-8') as count_file:
#             count_file.write(f"{intent_name}: {num_combinations}\n")

#     # Save all intents in one JSON file
#     with open("output.json", "w", encoding='utf-8') as json_file:
#         json.dump(all_results, json_file, ensure_ascii=False, indent=2)
import random
import json
from excel_reader import read_excel
from collections import Counter

def generate_and_save_json(file_path, intents, max_combinations=215):
    all_results = {}

    for intent_name in intents:
        data = read_excel(file_path, intent_name)

        # Extract entities (columns) excluding the first column (intent name)
        entity_columns = data.columns[1:].tolist()  # Convert Index to list

        # Create a dictionary to store combination counts for each entity
        entity_combination_counts = {entity: Counter() for entity in entity_columns}

        # Create a list to store combinations
        combinations_list = []

        # Ensure each intent has at least max_combinations combinations
        while len(combinations_list) < max_combinations:
            combination_values = generate_uniform_combination(entity_columns, data, entity_combination_counts)
            combinations_list.append(combination_values)

        # Save the result for each intent
        result_json = {intent_name: combinations_list}
        all_results.update(result_json)

        # Count the number of combinations and store in a text file
        num_combinations = len(combinations_list)
        with open("combinations_count.txt", "a", encoding='utf-8') as count_file:
            count_file.write(f"{intent_name}: {num_combinations}\n")

        # Count the final numbers of appearances of each value with the corresponding entity and store in a text file
        with open("entity_value_counts.txt", "a", encoding='utf-8') as entity_count_file:
            entity_count_file.write(f"{intent_name}:\n")
            for entity, value_counts in entity_combination_counts.items():
                for value, count in value_counts.items():
                    entity_count_file.write(f"{entity} - {value}: {count}\n")

    # Save all intents in one JSON file
    with open("output.json", "w", encoding='utf-8') as json_file:
        json.dump(all_results, json_file, ensure_ascii=False, indent=2)

def generate_uniform_combination(entity_columns, data, entity_combination_counts):
    # Shuffle entity columns for randomness
    shuffled_entity_columns = random.sample(entity_columns, random.randint(1, len(entity_columns)))

    combination_values = {}

    for col in shuffled_entity_columns:
        values = data[col].dropna().tolist()

        # Shuffle values for randomness
        random.shuffle(values)

        # Choose a random value first
        chosen_value = random.choice(values)
        combination_values[col] = chosen_value

        # Increment the count for the chosen value
        entity_combination_counts[col][chosen_value] += 1

        # Add more values to achieve a more balanced appearance
        while entity_combination_counts[col][chosen_value] < len(values) // len(shuffled_entity_columns):
            # Not adding more values to the combination_values dictionary,
            # as each entity in the combination should have only one value
            entity_combination_counts[col][chosen_value] += 1

    return combination_values

# Example usage:
# generate_and_save_json("your_file_path.xlsx", ["intent1", "intent2"], max_combinations=1000)
