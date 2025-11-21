import os
from typing import Dict

import requests

API_URL = "https://api.apilayer.com/exchangerates_data/latest"
API_KEY = os.getenv("API_ACCESS_KEY")


def get_exchange_rate(currency: str) -> float:
    """
    Получает текущий курс обмена для указанной валюты к рублю.
    Возвращает курс или 0.0, если произошла ошибка.
    """
    headers = {"apikey": API_KEY}
    params = {"base": "USD", "symbols": "RUB"}  # Можно менять base в зависимости от валюты
    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        rates = data.get("rates", {})
        if currency == "USD":
            return rates.get("RUB", 0.0)
        elif currency == "EUR":
            # Для EUR нужно сделать отдельный запрос или изменить base
            # Можно сделать общий запрос с base=USD и получать EUR, или делать отдельные
            # Для простоты: сделаем отдельный запрос для EUR
            params = {"base": "EUR", "symbols": "RUB"}
            response = requests.get(API_URL, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("rates", {}).get("RUB", 0.0)
        else:
            return 0.0
    except requests.RequestException:
        return 0.0


def convert_transaction_to_rub(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    Если валюта USD или EUR — запрашивает курс.
    Возвращает сумму в float.
    """
    amount = transaction.get("amount", 0)
    currency = transaction.get("currency")
    if currency == "RUB" or currency is None:
        return float(amount)
    elif currency in ["USD", "EUR"]:
        rate = get_exchange_rate(currency)
        return float(amount) * rate
    else:
        # Неизвестная валюта
        return float(amount)
