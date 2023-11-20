from collections import defaultdict

def label_variation_detector(data, k=2):
    label_variation_results = []

    # Create dictionaries to store left and right n-gram sets for each entity type
    left_ngrams = defaultdict(set)
    right_ngrams = defaultdict(set)

    # Iterate through examples and entities to collect n-grams
    for example in data:
        for entity in example['entities']:
            entity_type = entity['type']
            entity_filler = entity['filler']
            tokens = example['sentence'].split()

            # Find the index of the entity filler in the tokens list
            try:
                entity_index = tokens.index(entity_filler)
            except ValueError:
                # Handle the case where the entity filler is not found in tokens
                entity_index = -1

            if entity_index != -1:
                # Extract left and right n-grams around the entity
                start_index = max(0, entity_index - k)
                end_index = min(len(tokens), entity_index + len(entity_filler.split()) + k)
                left_ngram = ' '.join(tokens[start_index:entity_index])
                right_ngram = ' '.join(tokens[entity_index+1:end_index])

                # Add the n-grams to the corresponding sets
                left_ngrams[entity_type].add(left_ngram)
                right_ngrams[entity_type].add(right_ngram)

    # Iterate through entities and suggest changes based on n-gram sets
    for example in data:
        for entity in example['entities']:
            entity_type = entity['type']
            entity_filler = entity['filler']
            left_ngram_set = left_ngrams[entity_type]
            right_ngram_set = right_ngrams[entity_type]
            left_count = sum(1 for ngram in left_ngram_set if entity_filler in ngram)
            right_count = sum(1 for ngram in right_ngram_set if entity_filler in ngram)

            # Initialize suggested_change as the current entity type
            suggested_change = entity_type

            # Compare left_count and right_count to determine the suggested_change
            if left_count > right_count:
                if left_ngram_set:
                    suggested_change = entity_type
            elif right_count > left_count:
                if right_ngram_set:
                    suggested_change = entity_type

            # Skip cases where both sets have the same count and suggest the same entity
            if left_count == right_count and left_ngram_set == right_ngram_set:
                continue

            if suggested_change != entity_type:
                label_variation_results.append((example['id'], example['sentence'], entity_type, suggested_change))

    return label_variation_results
