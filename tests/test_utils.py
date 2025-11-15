from unittest.mock import patch
from src.utils import convert_to_rub


def test_convert_to_rub_usd_eur_rub():
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
    transaction_rub = {
        'operationAmount': {
            'amount': 100,
            'currency': {'code': 'RUB'}
        }
    }

    with patch('src.utils.get_exchange_rate') as mock_get_rate:
        mock_get_rate.return_value = 75.0
        assert convert_to_rub(transaction_usd) == 7500.0
        assert convert_to_rub(transaction_eur) == 7500.0
        assert convert_to_rub(transaction_rub) == 100.0
