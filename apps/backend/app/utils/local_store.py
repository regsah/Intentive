import json
import os
from typing import List, Dict
from datetime import datetime

def load_data(file_path: str) -> List[Dict]:
    if not os.path.exists(file_path):
        return []
    
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
        
def save_data(file_path: str, entry: Dict) -> None:
    data = load_data(file_path)
    data.append(entry)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
def clear_data(file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([], f)
