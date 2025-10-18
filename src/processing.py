from typing import List, Dict, Any
from datetime import datetime

def filter_by_state(items: List[Dict[str, Any]], target_state: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список элементов по заданному состоянию.

    Args:
        items: список словарей, каждый из которых должен содержать ключ 'state'.
        target_state: строка, по которой осуществляется фильтрация.
                      Возвращаются только те элементы, у которых 'state' равно target_state.

    Returns:
        Список словарей, удовлетворяющих условию фильтрации.
    """
    return [item for item in items if item.get('state') == target_state]

def sort_by_date(items: List[Dict[str, Any]], date_field: str = 'date') -> List[Dict[str, Any]]:
    """
    Сортирует список элементов по дате, указанной в поле date_field.

    Args:
        items: список словарей, каждый из которых должен содержать ключ, указанный в параметре date_field.
        date_field: название поля, по которому нужно сортировать. По умолчанию 'date'.

    Returns:
        Отсортированный список словарей по возрастанию даты.
    """
    return sorted(
        items,
        key=lambda item: datetime.fromisoformat(item[date_field])
    )

# Пример данных
data = [
    {'id': 1, 'state': 'active', 'date': '2025-10-10T10:00:00'},
    {'id': 2, 'state': 'inactive', 'date': '2025-10-09T09:00:00'},
    {'id': 3, 'state': 'active', 'date': '2025-10-11T11:00:00'},
    {'id': 4, 'state': 'inactive', 'date': '2025-10-18T08:00:00'},
]

# Фильтрация по состоянию 'active'
filtered_active = filter_by_state(data, 'active')
print("Фильтр по состоянию 'active':")
for item in filtered_active:
    print(item)

# Сортировка всех данных по дате
sorted_data = sort_by_date(data)
print("\nДанные отсортированы по дате:")
for item in sorted_data:
    print(item)