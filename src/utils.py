import json
from typing import Any, Dict, List

from src.log_config import setup_logger

logger = setup_logger(__name__)


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
            logger.info(f"Чтение файла {file_path}")
            if not isinstance(data, list):
                logger.warning("Данные не являются списком")
                return []
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        return []
