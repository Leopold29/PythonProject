import requests
import json


def get_exchange_rate(currency_code: str) -> float:
    """
    Получает текущий курс обмена указанной валюты к российскому рублю (RUB) через внешний API.

    Args:
        currency_code (str): Трехбуквенный код валюты, например, 'USD', 'EUR'.

    Returns:
        float: Курс обмена к рублю. Если запрос неуспешен или курс не найден, возвращает 0.0.
    """
    url = f'https://api.exchangerate-api.com/v4/latest/{currency_code}'
    response = requests.get(url)
    if response.status_code != 200:
        return 0.0
    data = response.json()
    return data['rates'].get('RUB', 0.0)


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли по текущему курсу обмена.

    Args:
        transaction (dict): Словарь с информацией о транзакции, должен содержать ключи:
            - 'operationAmount' (dict): содержит 'amount' (float) и 'currency' (dict) с 'code' (str).

    Returns:
        float: Сумма в рублях после конвертации. Если валюта уже рубль, возвращает исходную сумму.
        Если курс получить не удалось, возвращает 0.0.
    """
    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['code']
    if currency == 'RUB':
        return amount
    rate = get_exchange_rate(currency)
    return amount * rate


def read_transactions(file_path: str) -> list:
    """
    Читает список транзакций из JSON файла.

    Args:
        file_path (str): Путь к файлу формата JSON, содержащему список транзакций.

    Returns:
        list: Список транзакций (каждая — это словарь).
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
