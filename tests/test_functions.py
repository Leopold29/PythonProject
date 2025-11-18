import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unittest.mock import patch
from external_api import fetch_exchange_rate


def test_fetch_exchange_rate_success():
    """
    Тест успешного получения курса обмена.
    """
    with patch('external_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'rates': {'RUB': 75.0}
        }
        rate = fetch_exchange_rate('USD')
        assert rate == 75.0


def test_fetch_exchange_rate_failure():
    """
    Тест случая, когда API возвращает ошибку (неуспешный статус).
    """
    with patch('external_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 500
        rate = fetch_exchange_rate('USD')
        assert rate == 0.0


def test_fetch_exchange_rate_no_rub():
    """
    Тест случая, когда в ответе нет курса RUB.
    """
    with patch('external_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'rates': {'EUR': 0.85}
        }
        rate = fetch_exchange_rate('EUR')
        assert rate == 0.0
