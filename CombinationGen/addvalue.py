import json
import random

# Load the updated JSON file
with open("output_last.json", "r", encoding="utf-8") as f:
    combinations_data = json.load(f)

# Define the mapping of words to search for and their corresponding replacements
replace_words = {
    "<hour_int>": [
        "0", "1", "2", "3", "4", "5", "6","7","8","9","10","11","12","13", "20", "21", "24"
    ],
    "<month_int>": [
        "0", "1", "2", "3", "4", "5", "6","7","8","9","10","11","12"
    ],
    "<day_int>": [
        "0", "1", "2", "3", "4", "5", "6","7"
    ],
    "<min_int>": [
        "0", "1", "2", "3", "4", "5", "6","7","8","9","10","11","12","13", "20", "21", "24", "25", "30", "35", "40", "45", "50", "55"
    ],
    "<province>": [
        "Hải Phòng", "Thái Bình", "Nam Định", "Quảng Ninh", "Tây Ninh", "Cần Thơ", "Khánh Hòa"
    ],
    "<city>": [
        "Hà Nội", "Sài Gòn", "Huế", "Đà Nẵng", "Cần Thơ", "Thái Bình"
    ],
    "<country>": [
        "Việt Nam", "Trung Quốc", "Mỹ", "Đức", "Hàn Quốc", "Nhật Bản", "Pháp"
    ],
    "<area>": [
        "khu vui chơi", "khu ăn uống", "khu vực làm việc"
    ]
}


# Function to replace words in a dictionary
def replace_words_in_dict(d):
    for key, value in d.items():
        if isinstance(value, str):
            for word, replacements in replace_words.items():
                if word in value:
                    replacement = random.choice(replacements)
                    d[key] = value.replace(word, replacement)
        elif isinstance(value, dict):
            replace_words_in_dict(value)
    return d


# Iterate through combinations and replace words based on the mapping
for intent, combinations in combinations_data.items():
    for combination in combinations:
        replace_words_in_dict(combination)

# Save the updated combinations to a new JSON file
with open("output_last.json", "w", encoding="utf-8") as f:
    json.dump(combinations_data, f, ensure_ascii=False, indent=4)
