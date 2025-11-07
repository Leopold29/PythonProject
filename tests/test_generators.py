import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    """
    Фикстура с примерными данными транзакций.

    Returns:
        List[Dict]: список транзакций с полями id, state, date, operationAmount, description, from, to.
    """
    return [
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


@pytest.mark.parametrize("currency_code, expected_count", [
    ("USD", 2),
    ("EUR", 1),
    ("RUB", 0),
])
def test_filter_by_currency(transactions, currency_code, expected_count):
    """
    Тест функции filter_by_currency.

    Args:
        transactions (List[Dict]): список транзакций.
        currency_code (str): код валюты для фильтрации.
        expected_count (int): ожидаемое количество транзакций после фильтрации.

    Returns:
        None
    """
    result = list(filter_by_currency(transactions, currency_code))
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(t['operationAmount']['currency']['code'] == currency_code for t in result)


def test_filter_by_currency_empty():
    """
    Тест функции filter_by_currency при пустом списке транзакций.

    Args:
        None

    Returns:
        None
    """
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(transactions):
    """
    Тест генератора описаний транзакций.

    Args:
        transactions (List[Dict]): список транзакций.

    Returns:
        None
    """
    gen = transaction_descriptions(transactions)
    descs = list(gen)
    assert descs == ["Payment 1", "Payment 2", "Payment 3"]
    transactions_with_missing_desc = [{"id": 4}]
    gen2 = transaction_descriptions(transactions_with_missing_desc)
    assert next(gen2) == ''


@pytest.mark.parametrize("start, stop, expected_first, expected_last", [
    (1, 3, "0000 0000 0000 0001", "0000 0000 0000 0003"),
    (9999999999999998, 9999999999999999, "9999 9999 9999 9998", "9999 9999 9999 9999"),
])
def test_card_number_generator_range(start, stop, expected_first, expected_last):
    """
    Тест генератора номеров карт по диапазону.

    Args:
        start (int): начальное число диапазона.
        stop (int): конечное число диапазона.
        expected_first (str): ожидаемый первый номер карты.
        expected_last (str): ожидаемый последний номер карты.

    Returns:
        None
    """
    gen = card_number_generator(start, stop)
    result = list(gen)
    if result:
        assert result[0] == expected_first
        assert result[-1] == expected_last
    else:
        assert stop < start  # если диапазон некорректен, результат пустой


def test_card_number_generator_empty():
    """
    Тест генератора номеров карт при пустом диапазоне.

    Args:
        None

    Returns:
        None
    """
    gen = card_number_generator(5, 4)
    result = list(gen)
    assert result == []
