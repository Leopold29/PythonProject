import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def transactions():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-03-11T10:00:00'},
        {'id': 2, 'state': 'CANCELED', 'date': '2024-03-10T09:00:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2024-03-12T11:00:00'},
        {'id': 4, 'state': 'FAILED', 'date': '2024-03-09T08:00:00'},
    ]

def test_filter_by_state_default(transactions):
    result = filter_by_state(transactions)
    assert all(t['state'] == 'EXECUTED' for t in result)
    assert len(result) == 2

def test_filter_by_state_specific(transactions):
    result = filter_by_state(transactions, 'CANCELED')
    assert all(t['state'] == 'CANCELED' for t in result)
    assert len(result) == 1

def test_sort_by_date_descending(transactions):
    sorted_tx = sort_by_date(transactions)
    dates = [t['date'] for t in sorted_tx]
    assert dates == sorted(dates, reverse=True)

def test_sort_by_date_ascending(transactions):
    sorted_tx = sort_by_date(transactions, reverse=False)
    dates = [t['date'] for t in sorted_tx]
    assert dates == sorted(dates)