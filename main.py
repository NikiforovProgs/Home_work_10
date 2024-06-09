from src.widget import date_conversion, mask_card_number

"""Импортируем функции из директории src"""

if __name__ == "__main__":
    print(mask_card_number("Visa Platinum 6831982476737658"))
    print(date_conversion("2014-12-05"))
