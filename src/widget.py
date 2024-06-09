def mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты или счета и возвращает маску."""

    #   Проверяем тип карты
    if "Visa Classic" in card_number:
        masked_number = card_number[:17] + " " + card_number[18:20] + "** **** " + card_number[-4:]
    elif "Master Card" in card_number:
        masked_number = card_number[:17] + " " + card_number[18:20] + "** **** " + card_number[-4:]
    elif "Счет" in card_number:
        masked_number = card_number[:17] + " " + card_number[18:20] + "** **** " + card_number[-4:]
    elif "Visa Platinum" in card_number:
        masked_number = card_number[:17] + " " + card_number[18:20] + "** **** " + card_number[-4:]
    elif "Visa Gold" in card_number:
        masked_number = card_number[:17] + " " + card_number[18:20] + "** **** " + card_number[-4:]
    return masked_number


def date_conversion(date: str) -> str:
    """Функция, преобразующая формат даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"

