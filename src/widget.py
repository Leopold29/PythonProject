from datetime import datetime
from mask import get_mask_account, get_mask_card_number

def get_date(date_str):
    """
    Преобразует строку даты в формат 'день.месяц.год'.

    Args:
        date_str (str): Строка даты в формате '2024-03-11'.

    Returns:
        str: Дата в формате 'дд.мм.гггг'.
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")

# Ваши исходные данные
card = "7000792289606361"  # номер карты
account = "73654108430135874305"  # номер счета
date_str = "2024-03-11"  # строка даты

# Маскируем данные
masked_account = get_mask_account(account)
masked_card = get_mask_card_number(card)
formatted_date = get_date(date_str)

# Выводим отформатированные и маскированные данные
print(f"Visa Platinum: {masked_card}")
print(f"Счет: {masked_account}")
print(f"Дата: {formatted_date}")