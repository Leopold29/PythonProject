from typing import Union

def get_mask_card_number(card_number: Union[int, str]) -> str:
    """
    Маскирует номер карты в формате: XXXX XX** **** XXXX
    Где показываются первые 4 цифры, 2 цифры после них и последние 4 цифры.
    Остальные заменены на звёздочки.
    """
    number_str = str(card_number).replace(" ", "")

    if len(number_str) < 16:
        raise ValueError("Неверная длина номера карты")

    first_four = number_str[:4]
    next_two = number_str[4:6]
    last_four = number_str[-4:]

    masked_card = f"{first_four} {next_two}** **** {last_four}"
    return masked_card

def get_mask_account(account_number: Union[int, str]) -> str:
    """
    Маскирует номер счёта в формате: **XXXX
    Где показываются последние 4 цифры.
    """
    number_str = str(account_number).replace(" ", "")
    last_four = number_str[-4:]
    return f"**{last_four}"

if __name__ == "__main__":
    # Пример данных для теста
    card_example = "7000792289606361"
    account_example = "73654108430135874305"

    print(get_mask_card_number(card_example))
    print(get_mask_account(account_example))
