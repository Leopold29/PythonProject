import json
from unittest.mock import patch, mock_open


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


# Тесты
def test_read_transactions_json_valid():
    mock_data = [{"id": 1}, {"id": 2}]
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))) as mock_file:
        data = read_transactions('some_path.json')
        mock_file.assert_called_once_with('some_path.json', 'r', encoding='utf-8')
        assert isinstance(data, list)
        assert data == mock_data


def test_read_transactions_json_invalid():
    # Имитация исключения при открытии файла
    with patch("builtins.open", side_effect=FileNotFoundError):
        data = read_transactions('invalid_path.json')
        assert data == []


def test_read_transactions_json_not_list():
    # Возвращаем JSON, который не является списком
    with patch("builtins.open", mock_open(read_data=json.dumps({"not": "list"}))) as mock_file:
        data = read_transactions('some_path.json')
        mock_file.assert_called_once_with('some_path.json', 'r', encoding='utf-8')
        assert data == []


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
