import pytest
from src.widget import get_date

@pytest.mark.parametrize("date_str,expected", [
    ("2024-03-11", "11.03.2024"),
    ("2020-01-01", "01.01.2020"),
])
def test_get_date_valid(date_str, expected):
    assert get_date(date_str) == expected

def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("invalid-date")