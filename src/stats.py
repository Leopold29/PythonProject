from collections import Counter
from typing import Dict, List


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по каждой из заданных категорий.

    Args:
        data (List[Dict]): список транзакций.
        categories (List[str]): список категорий для подсчета.

    Returns:
        Dict[str, int]: словарь с количеством операций по каждой категории.
    """
    counts: Counter[str] = Counter()
    for transaction in data:
        description = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                counts[category] += 1
    # Обеспечить, что все категории есть в результате
    result = {category: counts.get(category, 0) for category in categories}
    return result
