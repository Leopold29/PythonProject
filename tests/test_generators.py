import os
import sys

# Добавляем папку src в системный путь, чтобы можно было импортировать generators
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Импортируем функции из generators.py
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Пример данных для тестов
transactions = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2022-01-01T00:00:00",
        "operationAmount": {
            "amount": "100",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Payment 1",
        "from": "Account 1",
        "to": "Account 2"
    },
    {
        "id": 2,
        "state": "EXECUTED",
        "date": "2022-01-02T00:00:00",
        "operationAmount": {
            "amount": "200",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Payment 2",
        "from": "Account 3",
        "to": "Account 4"
    },
    {
        "id": 3,
        "state": "FAILED",
        "date": "2022-01-03T00:00:00",
        "operationAmount": {
            "amount": "300",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Payment 3",
        "from": "Account 5",
        "to": "Account 6"
    },
]


def test_filter_by_currency_found():
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert all(t['operationAmount']['currency']['code'] == 'USD' for t in result)


def test_filter_by_currency_not_found():
    result = list(filter_by_currency(transactions, "RUB"))
    assert result == []


def test_filter_by_currency_empty():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions():
    gen = transaction_descriptions(transactions)
    descs = list(gen)
    assert descs == ["Payment 1", "Payment 2", "Payment 3"]
    # Проверка, что по умолчанию возвращает пустую строку, если description отсутствует
    transactions_with_missing_desc = [{"id": 4}]
    gen2 = transaction_descriptions(transactions_with_missing_desc)
    assert next(gen2) == ''


def test_card_number_generator_range():
    gen = card_number_generator(1, 3)
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]
    result = list(gen)
    assert result == expected


def test_card_number_generator_edge():
    gen = card_number_generator(9999999999999998, 9999999999999999)
    result = list(gen)
    assert result[0] == "9999 9999 9999 9998"
    assert result[-1] == "9999 9999 9999 9999"


def test_card_number_generator_empty():
    gen = card_number_generator(5, 4)
    result = list(gen)
    assert result == []
