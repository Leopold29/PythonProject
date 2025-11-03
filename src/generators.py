from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по валюте.

    Args:
        transactions (List[Dict]): список транзакций.
        currency_code (str): код валюты, по которому фильтруем.

    Returns:
        Iterator[Dict]: итератор по транзакциям в заданной валюте.
    """
    for transaction in transactions:
        if ('operationAmount' in transaction and
                'currency' in transaction['operationAmount'] and
                'code' in transaction['operationAmount']['currency']):
            if transaction['operationAmount']['currency']['code'] == currency_code:
                yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор описаний транзакций.

    Args:
        transactions (List[Dict]): список транзакций.

    Returns:
        Iterator[str]: итератор описаний.
    """
    for transaction in transactions:
        yield transaction.get('description', '')


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start (int): начальное значение диапазона.
        stop (int): конечное значение диапазона.

    Returns:
        Iterator[str]: номера карт.
    """
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        formatted_number = ' '.join([card_number[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_number
