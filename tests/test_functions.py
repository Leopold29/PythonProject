import os
from unittest.mock import patch


# Предположим, что эти функции у вас реализованы где-то в коде
def read_transactions(filepath):
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except Exception:
        return []


def convert_currency(transaction):
    from src.external_api import get_exchange_rate
    currency = transaction.get("currency")
    amount = transaction.get("amount", 0)
    if currency == "USD":
        rate = get_exchange_rate("USD", "RUB")
        return amount * rate
    elif currency == "EUR":
        rate = get_exchange_rate("EUR", "RUB")
        return amount * rate
    elif currency == "RUB":
        return amount
    else:
        return 0.0


# Тест для функции чтения JSON
def test_read_transactions_json_valid():
    data = read_transactions('data/operations.json')
    assert isinstance(data, list)


def test_read_transactions_json_invalid():
    data = read_transactions('invalid_path.json')
    assert data == []


def test_read_transactions_json_not_list():
    # Создаем папку, если ее нет
    os.makedirs('data', exist_ok=True)
    filename = 'data/test_invalid.json'
    # Создаем файл с некорректными данными
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('{"not": "list"}')
    result = read_transactions(filename)
    assert result == []


# Тест для функции конвертации валют
@patch('src.external_api.get_exchange_rate')
def test_convert_currency_usd_eur(mock_get_rate):
    mock_get_rate.return_value = 75.0
    transaction_usd = {"amount": 10, "currency": "USD"}
    transaction_eur = {"amount": 20, "currency": "EUR"}
    assert abs(convert_currency(transaction_usd) - 750.0) < 1e-6
    assert abs(convert_currency(transaction_eur) - 1500.0) < 1e-6


@patch('src.external_api.get_exchange_rate')
def test_convert_currency_rub(mock_get_rate):
    mock_get_rate.return_value = 75.0
    transaction_rub = {"amount": 1000, "currency": "RUB"}
    assert convert_currency(transaction_rub) == 1000.0


def test_convert_currency_unknown():
    transaction = {"amount": 50, "currency": "ABC"}
    assert convert_currency(transaction) == 0.0
