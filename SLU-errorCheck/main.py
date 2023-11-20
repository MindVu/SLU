import json
from collections import defaultdict
from formatchecker import format_checker
from labelvariation import label_variation_detector

# Read the JSONL file
def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))
    return data

def save_results_to_txt(output_file, format_checker_results, label_variation_results):
    with open(output_file, 'w', encoding='utf-8') as file:
        
        
        file.write("Label Variation Results:\n")
        for result in label_variation_results:
            example_id, sentence, current_annotation, suggested_change, entity_filler = result
            file.write(f"Example ID: {example_id}\n")
            file.write(f"Sentence: {sentence}\n")
            file.write(f"Current Annotation: {current_annotation}\n")
            file.write(f"Suggested Change: {suggested_change}\n")
            file.write(f"Entity Filler: {entity_filler}\n")
            file.write("\n")
            
# Save the N-gram sets to a text file
def save_n_gram_sets_to_txt(file_path, left_ngrams, right_ngrams):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Left N-grams:\n")
        for entity_type, ngram_set in left_ngrams.items():
            file.write(f"Entity Type: {entity_type}\n")
            for ngram in ngram_set:
                file.write(f"{ngram}\n")

        file.write("\nRight N-grams:\n")
        for entity_type, ngram_set in right_ngrams.items():
            file.write(f"Entity Type: {entity_type}\n")
            for ngram in ngram_set:
                file.write(f"{ngram}\n")

# Main function to process the JSONL file
def process_jsonl(file_path):
    data = read_jsonl(file_path)
    format_checker_results = format_checker(data)
    label_variation_results = label_variation_detector(data)

    # Extract and save N-gram sets
    left_ngrams, right_ngrams = extract_n_gram_sets(data)
    save_n_gram_sets_to_txt('n_gram.txt', left_ngrams, right_ngrams)

    return format_checker_results, label_variation_results

# Extract and save N-gram sets for both methods
def extract_n_gram_sets(data):
    left_ngrams = defaultdict(set)
    right_ngrams = defaultdict(set)

    # Loop through each example in the data
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

    return left_ngrams, right_ngrams

jsonl_file = 'test.jsonl'
format_checker_results, label_variation_results = process_jsonl(jsonl_file)

# Count the number of suggestions for each method
format_checker_suggestion_count = len(format_checker_results)
label_variation_suggestion_count = len(label_variation_results)

# Save the results to a text file
output_file = 'suggestions.txt'
save_results_to_txt(output_file, format_checker_results, label_variation_results)

# Print the suggestion counts
print(f"Format Checker Suggestions: {format_checker_suggestion_count}")
print(f"Label Variation Detector Suggestions: {label_variation_suggestion_count}")
print(f"Results saved to '{output_file}'")