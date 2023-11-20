import json

def count_entities_in_intents(json_file_path, output_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        total_combinations = 0

        for intent, combinations in data.items():
            total_combinations += len(combinations)

            output_file.write(f'Intent: {intent}\n')
            output_file.write(f'Number of Combinations: {len(combinations)}\n')

            entity_count = {}
            for combination in combinations:
                for entity, value in combination.items():
                    entity_count[entity] = entity_count.get(entity, 0) + 1

            for entity, count in entity_count.items():
                output_file.write(f'{entity}: {count}\n')

            output_file.write('\n')

        output_file.write(f'Total Combinations: {total_combinations}\n')

# Example usage
json_file_path = 'output_lasttest.json'
output_file_path = 'entity_count.txt'
count_entities_in_intents(json_file_path, output_file_path)
