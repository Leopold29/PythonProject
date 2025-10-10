from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """
    Маскирует номер карты в формате: XXXX XX** **** XXXX
    Где показываются первые 6 цифр (первые 4 и 2), и последние 4 цифры.
    Остальные символы заменены на звёздочки.
    """
    # Преобразуем номер карты в строку и убираем пробелы, если есть
    number_str = str(card_number).replace(" ", "")

    # Проверка длины номера (должно быть минимум 16 цифр)
    if len(number_str) < 16:
        raise ValueError("Неверная длина номера карты")

    # Берём первые 4 цифры
    first_four = number_str[:4]
    # Берём следующие 2 цифры
    next_two = number_str[4:6]
    # Берём последние 4 цифры
    last_four = number_str[-4:]

    # Создаём маску в нужном формате
    masked_card = f"{first_four} {next_two}** **** {last_four}"
    return masked_card


def get_mask_account(account_number: Union[int, str]) -> str:
    """
    Маскирует номер счёта в формате: **XXXX
    Где показываются последние 4 цифры номера.
    """
    number_str = str(account_number).replace(" ", "")
    last_four = number_str[-4:]
    return f"**{last_four}"


# Пример номера карты
card = 7000792289606361
print(get_mask_card_number(card))
# Вывод: 7000 79******6361

# Пример номера счёта
account = 73654108430135874305
print(get_mask_account(account))
# Вывод: **4305
