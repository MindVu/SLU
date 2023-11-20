import pandas as pd

# Read the information from the text file
with open("entity_count.txt", "r") as file:
    input_data = file.read()

# Split the input data into sections for each intent
sections = [section.strip() for section in input_data.split("Intent:") if section.strip()]

# Initialize lists to store data
intents = []
num_combinations = []
num_entities = []

# Process each section
for section in sections:
    lines = section.split("\n")
    intent = lines[0].strip()
    num_combinations_value = int(lines[1].split(":")[1].strip())
    intent_data = {"Intent": intent, "Number of Combinations": num_combinations_value}

    num_entities_value = 0
    for line in lines[2:]:
        if ":" in line:
            num_entities_value += 1

    intents.append(intent_data)
    num_combinations.append(num_combinations_value)
    num_entities.append(num_entities_value)

# Create a DataFrame from the collected data
df = pd.DataFrame(intents)

# Add Number of Entities column to the DataFrame
df["Number of Entities"] = num_entities

# Display and save the DataFrame
df.to_csv("output_table.csv", columns=["Intent", "Number of Combinations", "Number of Entities"], index=False)
print(df)
