import json
from typing import List, Dict, Any
from src.external_api import get_exchange_rate


def read_transactions(json_path: str) -> List[Dict[str, Any]]:
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли, используя функцию get_exchange_rate.
    Ожидается структура транзакции:
    {
        "operationAmount": {
            "amount": float,
            "currency": {"code": str}
        }
        ...
    }
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
