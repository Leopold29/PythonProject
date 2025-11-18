from unittest.mock import patch
from src.utils import get_exchange_rate, convert_to_rub


def test_fetch_exchange_rate_success():
    """
    Тестирует успешное получение курса обмена валюты к рублю.
    Мокает ответ API с курсом.
    """
    with patch('src.utils.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'rates': {'RUB': 75.0}
        }
        rate = get_exchange_rate('USD')
        assert rate == 75.0


def test_fetch_exchange_rate_failure():
    """
    Тестирует обработку ошибки при неуспешном ответе API.
    Возвращает 0.0 при ошибке.
    """
    with patch('src.utils.requests.get') as mock_get:
        mock_get.return_value.status_code = 500
        rate = get_exchange_rate('USD')
        assert rate == 0.0


def test_fetch_exchange_rate_no_rub():
    """
    Тестирует случай, когда в ответе API нет курса RUB.
    Ожидается возвращение 0.0.
    """
    with patch('src.utils.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'rates': {'EUR': 0.85}
        }
        rate = get_exchange_rate('EUR')
        assert rate == 0.0


def test_convert_to_rub_usd_eur():
    """
    Тестирует конвертацию транзакции из USD и EUR в рубли.
    Использует мок для get_exchange_rate.
    """
    transaction_usd = {
        'operationAmount': {
            'amount': 100,
            'currency': {'code': 'USD'}
        }
    }
    transaction_eur = {
        'operationAmount': {
            'amount': 100,
            'currency': {'code': 'EUR'}
        }
    }

    with patch('src.utils.get_exchange_rate') as mock_get_rate:
        # задаем курс 75 для обеих валют
        mock_get_rate.side_effect = lambda code: 75.0
        result_usd = convert_to_rub(transaction_usd)
        result_eur = convert_to_rub(transaction_eur)
        assert result_usd == 7500.0
        assert result_eur == 7500.0


def test_convert_to_rub_rub():
    """
    Тестирует конвертацию уже рублевой транзакции.
    Ожидается, что сумма не изменится.
    """
    transaction_rub = {
        'operationAmount': {
            'amount': 100,
            'currency': {'code': 'RUB'}
        }
    }
    result = convert_to_rub(transaction_rub)
    assert result == 100.0


def test_convert_to_rub_unknown_currency():
    """
    Тестирует случай, когда валюта неизвестна.
    Ожидается возвращение 0.0.
    """
    transaction_unknown = {
        'operationAmount': {
            'amount': 100,
            'currency': {'code': 'XYZ'}
        }
    }
    with patch('src.utils.get_exchange_rate') as mock_get_rate:
        mock_get_rate.return_value = 0.0
        result = convert_to_rub(transaction_unknown)
        assert result == 0.0
