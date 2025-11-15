import json
from typing import List, Dict, Any


def read_transactions(json_path: str) -> List[Dict[str, Any]]:
    """
    Reads the JSON-файл с транзакциями.

    Args:
        json_path (str): Путь к JSON-файлу.

    Returns:
        List[Dict[str, Any]]: Список транзакций в виде словарей.
                               Если файл не существует или содержит некорректный JSON,
                               возвращает пустой список.
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                # Если JSON содержит не список, возвращаем пустой список
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        # В случае ошибок открытия файла или парсинга JSON возвращаем пустой список
        return []
