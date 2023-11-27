from combinations_generator import generate_and_save_json
from entity_type_reader import read_entity_types, update_json_with_entity_types
import json
from synonym_processor import update_json_with_synonyms

def main():
    excel_file_path = "slu.xlsx"
    intents = ["Tra cứu thời tiết",
"Tra cứu lịch",
"Bật nhạc",
"Tra công thức nấu ăn",
"Đặt lịch",
"Gọi taxi",
"tra cứu đường đi",
"Đặt vé",
"Gợi ý phim",
"gợi ý địa điểm",
"Xóa lịch",
"Liên hệ",
"đặt đồ ăn",
"Hỏi thông tin"]

    # Call the generate_and_save_json function for all intents
    generate_and_save_json(excel_file_path, intents)

    # Read entity types
    entity_types = read_entity_types(excel_file_path)

    # Read the generated JSON
    json_file_path = "output.json"
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

     # Update the generated JSON with entity types
    update_json_with_entity_types(json_data, entity_types)

    # Update the generated JSON with synonym entities
    update_json_with_synonyms(json_file_path, excel_file_path)
        
#     # Process synonym entities
#     synonym_entities = ["activity",
# "business_type",
# "condition",
# "genre",
# "weather_descriptor",
# "meal",
# "method",
# "ocassion",
# "payment_method",
# "transport_type",
# "type (premium, standard, pet friendly...)"
# ]  # Replace with your synonym entity names
    

    
if __name__ == "__main__":
    main()
