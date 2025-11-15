import os
import requests
from typing import Dict

API_URL = "https://api.apilayer.com/exchangerates_data/convert"
API_ACCESS_KEY = os.getenv("API_ACCESS_KEY")


def get_exchange_rate(from_currency: str, to_currency: str = "RUB") -> float:
    """
    Получает текущий курс обмена с API.
    """
    headers = {"apikey": API_ACCESS_KEY}
    params: Dict[str, str] = {
        "from": from_currency,
        "to": to_currency,
        "amount": "1",
    }
    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("result", 0.0)


def convert_currency(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли, учитывая структуру с operationAmount.
    """
    operation_amount = transaction.get("operationAmount", {})
    amount = operation_amount.get("amount", 0)
    currency_info = operation_amount.get("currency", {})
    currency_code = currency_info.get("code")

    if currency_code == "RUB":
        return float(amount)
    elif currency_code in ("USD", "EUR"):
        rate = get_exchange_rate(currency_code)
        return float(amount) * rate
    else:
        # Неизвестная валюта
        return 0.0
