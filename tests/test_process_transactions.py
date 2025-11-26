from unittest.mock import MagicMock, patch

from src import process_transactions


def test_read_transactions_csv():
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{'id': 1, 'amount': 100}]
    with patch('pandas.read_csv', return_value=mock_df):
        result = process_transactions.read_transactions_csv('dummy_path.csv')
        assert result == [{'id': 1, 'amount': 100}]


def test_read_transactions_excel():
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{'id': 2, 'amount': 200}]
    with patch('pandas.read_excel', return_value=mock_df):
        result = process_transactions.read_transactions_excel('dummy_path.xlsx')
        assert result == [{'id': 2, 'amount': 200}]
