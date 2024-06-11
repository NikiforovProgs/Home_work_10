from src.widget import date_conversion, mask_card_number
from src.processing import filter_by_state, sort_by_date

"""Импортируем функции из директории src"""

if __name__ == "__main__":
    print(mask_card_number("Visa Platinum 6831982476737658"))
    print(date_conversion("2014-12-05"))
    print(filter_by_state())
    print(sort_by_date())
