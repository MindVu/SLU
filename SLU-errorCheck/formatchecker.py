from collections import defaultdict

# Define the format checker function
def format_checker(data):
    format_checker_results = []

    # Extract left and right N-gram sets for each entity type
    left_ngrams = defaultdict(set)
    right_ngrams = defaultdict(set) 

    for example in data:
        for entity in example['entities']:
            span = entity['filler']
            left_ngram_set = set()
            right_ngram_set = set()
            tokens = example['sentence'].split()

            span_tokens = span.split()  # Split the span into tokens

            # Create left N-gram set
            for i in range(len(span_tokens) - 1):
                left_ngram_set.add(' '.join(span_tokens[:i + 1]))

            # Create right N-gram set
            for i in range(1, len(span_tokens)):
                right_ngram_set.add(' '.join(span_tokens[i:]))

            left_ngrams[entity['type']].update(left_ngram_set)
            right_ngrams[entity['type']].update(right_ngram_set)

    # Check adjacent tokens using N-gram sets
    for example in data:
        for entity in example['entities']:
            span = entity['filler']
            span_tokens = span.split()
            tokens = example['sentence'].split()

            try:
                # Check if the span is in the tokens list
                span_index = tokens.index(span)
            except ValueError:
                # Handle the case where the span is not found in tokens
                span_index = -1

            if span_index != -1:
                # Check if the text to the left of the span is in the left N-gram set
                left_adjacent_text = ' '.join(tokens[:span_index][-len(span_tokens) + 1:])
                if left_adjacent_text in left_ngrams[entity['type']]:
                    # Suggest adding the left adjacent text to the span
                    format_checker_results.append((example, entity['type'], span, 'add'))

                # Check if the text to the right of the span is in the right N-gram set
                right_adjacent_text = ' '.join(tokens[span_index + len(span_tokens):])
                if right_adjacent_text in right_ngrams[entity['type']]:
                    # Suggest adding the right adjacent text to the span
                    format_checker_results.append((example, entity['type'], span, 'add'))

    return format_checker_results
