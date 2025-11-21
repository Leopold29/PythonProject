import json
from typing import Any, Dict, List


def read_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл, содержащий данные о финансовых транзакциях.

    Аргументы:
        file_path (str): путь к файлу JSON.

    Возвращает:
        List[Dict[str, Any]]: список словарей с данными транзакций.
        Если файл пустой, содержит не список, не найден или возникла ошибка при чтении,
        возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
