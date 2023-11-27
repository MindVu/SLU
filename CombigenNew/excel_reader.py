import pandas as pd

def read_excel(file_path, intent_name):
    data = pd.read_excel(file_path, sheet_name=intent_name)
    return data
