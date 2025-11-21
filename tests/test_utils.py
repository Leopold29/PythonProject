from unittest.mock import mock_open, patch

from src.external_api import convert_transaction_to_rub
from src.utils import read_transactions


def test_read_transactions_valid():
    mock_json = '[{"amount": 100, "currency": "USD"}]'
    with patch("builtins.open", mock_open(read_data=mock_json)):
        result = read_transactions("fake_path.json")
        assert isinstance(result, list)
        assert result[0]["amount"] == 100


def test_read_transactions_empty():
    with patch("builtins.open", mock_open(read_data='')):
        result = read_transactions("fake_path.json")
        assert result == []


def test_read_transactions_not_a_list():
    mock_json = '{"amount": 100}'
    with patch("builtins.open", mock_open(read_data=mock_json)):
        result = read_transactions("fake_path.json")
        assert result == []


def test_read_transactions_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_transactions("fake_path.json")
        assert result == []


def test_convert_transaction_rub():
    transaction = {"amount": 100, "currency": "RUB"}
    result = convert_transaction_to_rub(transaction)
    assert isinstance(result, float)
    assert result == 100.0


@patch("src.external_api.get_exchange_rate")
def test_convert_transaction_usd(mock_rate):
    mock_rate.return_value = 75.0
    transaction = {"amount": 10, "currency": "USD"}
    result = convert_transaction_to_rub(transaction)
    assert result == 750.0


@patch("src.external_api.get_exchange_rate")
def test_convert_transaction_eur(mock_rate):
    mock_rate.return_value = 85.0
    transaction = {"amount": 10, "currency": "EUR"}
    result = convert_transaction_to_rub(transaction)
    assert result == 850.0


def test_convert_transaction_unknown_currency():
    transaction = {"amount": 10, "currency": "JPY"}
    result = convert_transaction_to_rub(transaction)
    assert result == 10.0
