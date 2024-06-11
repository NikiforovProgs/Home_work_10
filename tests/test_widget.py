from src.widget import mask_card_number, date_conversion


def test_mask_card_type_platinum():
    new_card_type_platinum: str = "Visa Platinum 6831982476737658"
    assert mask_card_number(new_card_type_platinum) == "Visa Platinum 6831 98** **** 7658"


def test_card_type_master():
    new_card_type_master: str = "Master Card 8541225633574896"
    assert mask_card_number(new_card_type_master) == "Master Card 8541 22** **** 4896"


def test_card_type_classic():
    new_card_type_classic: str = "Visa Classic 7589885622154877"
    assert mask_card_number(new_card_type_classic) == "Visa Classic 7589 88** **** 4877"


def test_card_type_gold():
    new_card_type_gold: str = "Visa Gold 3654775899651233"
    assert mask_card_number(new_card_type_gold) == "Visa Gold 3654 77** **** 1233"


def test_account_number():
    new_account_info: str = "Счет 73654108430135874305"
    assert mask_card_number(new_account_info) == "Счет **4305"


def test_date():
    new_date_info_1: str = "2014-12-05"
    assert date_conversion(new_date_info_1) == "05.12.2014"
    new_date_info_2: str = "2018 02 04"
    assert date_conversion(new_date_info_2) == "04.02.2018"
    new_date_info_3: str = "2011_03_07"
    assert date_conversion(new_date_info_3) == "07.03.2011"
