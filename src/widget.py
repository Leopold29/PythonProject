from masks import mask_card, mask_account


def mask_account_card(info_str: str) -> str:
    """
    Определяет тип информации (карта или счет) и применяет соответствующую маскировку.
    """
    info_str = info_str.strip()
    parts = info_str.split()

    # Проверка: первая часть может быть "Счет" или название карты
    first_word = parts[0].lower()

    # Если первый элемент "Счет" или "счет"
    if first_word == "счет":
        # Объединяем оставшуюся часть для функции
        account_info = " ".join(parts)
        return mask_account(account_info)
    else:
        # Предполагаем, что это карта
        card_info = " ".join(parts)
        return mask_card(card_info)