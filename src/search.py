import re
from typing import Dict, List


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Ищет в описании транзакций совпадения с регулярным выражением.

    Args:
        data (List[Dict]): список транзакций.
        search (str): строка для поиска, интерпретируется как регулярное выражение.

    Returns:
        List[Dict]: список транзакций, у которых в описании есть совпадение.
    """
    pattern = re.compile(search, re.IGNORECASE)
    result = [
        transaction for transaction in data
        if 'description' in transaction and pattern.search(transaction['description'])
    ]
    return result
