import requests


def fetch_exchange_rate(currency_code: str) -> float:
    """
    Получает курс обмена указанной валюты к рублю через внешний API.

    Args:
        currency_code (str): Трехбуквенный код валюты (например, 'USD', 'EUR').

    Returns:
        float: Курс обмена к рублю, если успешно, иначе 0.0.
    """
    url = f'https://api.exchangerate-api.com/v4/latest/{currency_code}'
    response = requests.get(url)
    if response.status_code != 200:
        return 0.0
    data = response.json()
    return data['rates'].get('RUB', 0.0)
