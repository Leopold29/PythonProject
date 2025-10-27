from typing import Dict, List


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список транзакций по заданному состоянию.
    """
    return [
        transaction for transaction in transactions
        if transaction.get('state') == state
    ]


def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список транзакций по дате.
    """
    return sorted(
        transactions,
        key=lambda x: x.get('date', ''),
        reverse=reverse
    )


# Пример входных данных
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Использование filter_by_state по умолчанию ('EXECUTED')
filtered_executed = filter_by_state(transactions)
print("Фильтр по статусу 'EXECUTED':")
print(filtered_executed)

# Использование filter_by_state с другим статусом
filtered_canceled = filter_by_state(transactions, 'CANCELED')
print("\nФильтр по статусу 'CANCELED':")
print(filtered_canceled)

# Использование sort_by_date (по убыванию)
sorted_transactions = sort_by_date(transactions)
print("\nОтсортированный по дате (по убыванию):")
print(sorted_transactions)
