import re
from typing import Union

# Предположим, что функции маскировки из прошлого задания находятся в модуле masks
# и выглядят так:
# from masks import get_mask_card_number, get_mask_account

# Для этого примера я вставлю функции маскировки прямо сюда (их можно импортировать из masks)

def get_mask_card_number(card_number: Union[int, str]) -> str:
    """
    Маскирует номер карты в формате: XXXX XX** **** XXXX
    Где показываются первые 6 цифр (первые 4 и 2), и последние 4 цифры.
    Остальные символы заменены на звёздочки.
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
    Маскирует номер счета в формате: **XXXX
    Где показываются последние 4 цифры номера.
    """
    number_str = str(account_number).replace(" ", "")
    last_four = number_str[-4:]
    return f"**{last_four}"

def mask_account_card(info: str) -> str:
    """
    Обрабатывает строку с типом и номером карты или счета,
    возвращая строку с маскированным номером.
    """
    parts = info.strip().split()
    if not parts:
        raise ValueError("Пустая строка")
    # Определяем, что это: карта или счет
    first_word = parts[0]
    # Обработка карт
    if first_word.lower() in {"visa", "mastercard", "maestro", "visa", "visa", "visa"}:
        # Вариант, что название карты может состоять из нескольких слов, например "Visa Platinum"
        # Поэтому ищем, где находится номер: номер — последний элемент
        card_number = parts[-1]
        # Маскируем номер
        masked_number = get_mask_card_number(card_number)
        # Формируем результат
        return f"{' '.join(parts[:-1])} {masked_number}"
    elif first_word.lower() == "счет":
        # Обработка счета
        account_number = parts[1]
        masked_number = get_mask_account(account_number)
        return f"Счет {masked_number}"
    else:
        # Неизвестный формат
        raise ValueError("Неизвестный тип карты или счета")

def get_date(date_str: str) -> str:
    """
    Преобразует строку даты из формата "YYYY-MM-DDTHH:MM:SS.ssssss"
    в формат "ДД.ММ.ГГГГ".
    """
    # Можно использовать регулярное выражение или datetime
    from datetime import datetime
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")