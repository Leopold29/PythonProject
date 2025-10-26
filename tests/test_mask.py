import pytest
from src.mask import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number,expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567812345678", "1234 56** **** 5678"),
    (7000792289606361, "7000 79** **** 6361"),
])
def test_get_mask_card_number_valid(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("invalid_card", [
    "123456789012345",  # 15 digits
    "",                # пустая строка
    "1234 5678 9012 34",  # менее 16 символов
])
def test_get_mask_card_number_errors(invalid_card):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card)

@pytest.mark.parametrize("account_number,expected", [
    ("73654108430135874305", "**4305"),
    ("1234 5678 9012 3456", "**3456"),
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected