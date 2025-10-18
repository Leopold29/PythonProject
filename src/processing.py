from typing import List, Dict, Any
from datetime import datetime


def filter_by_status(items: List[Dict[str, Any]], target_status: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список элементов по статусу.

    Args:
        items: список словарей, каждый из которых содержит ключ 'status'.
        target_status: статус для фильтрации.

    Returns:
        Отфильтрованный список элементов.
    """
    return [item for item in items if item.get('status') == target_status]


def sort_by_date(items: List[Dict[str, Any]], date_field: str = 'date') -> List[Dict[str, Any]]:
    """
    Сортирует список элементов по дате.

    Args:
        items: список словарей, каждый из которых содержит ключ с датой.
        date_field: ключ, по которому осуществляется сортировка.

    Returns:
        Отсортированный список.
    """
    return sorted(
        items,
        key=lambda item: datetime.fromisoformat(item[date_field])
    )
