import pytest
from src.masks import hide_card, mask_account


@pytest.fixture
def card_type():
    return "4568452421454868"


@pytest.fixture
def account():
    return "52454568521020142561"


def test_masks(card_type, account):
    assert hide_card(card_type) == "4568 45** **** 4868"
    assert mask_account(account) == "**2561"
