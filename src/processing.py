from typing import List, Dict, Any

def filter_by_state(
    transactions: List[Dict[str, Any]],
    state: str = 'EXECUTED'
) -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по значению ключа 'state'.

    Args:
        transactions (List[Dict[str, Any]]): список словарей с данными о транзакциях.
        state (str, optional): значение, по которому фильтруются транзакции. По умолчанию 'EXECUTED'.

    Returns:
        List[Dict[str, Any]]: отфильтрованный список транзакций.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]


def sort_by_date(
    transactions: List[Dict[str, Any]],
    reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по дате.

    Args:
        transactions (List[Dict[str, Any]]): список словарей с данными о транзакциях.
        reverse (bool, optional): порядок сортировки. По умолчанию True (по убыванию).

    Returns:
        List[Dict[str, Any]]: отсортированный список транзакций.
    """
    return sorted(
        transactions,
        key=lambda x: x.get('date', ''),
        reverse=reverse
    )