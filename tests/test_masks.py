import pytest

from src import masks


@pytest.mark.parametrize(
    "num_card, expected",
    [
        (1234123412341234, "1234 12** **** 1234"),
        (9876543210987654, "9876 54** **** 7654"),
    ],
)
def test_get_mask_card_number(num_card: int, expected: str) -> None:
    """
    Проверка рабоботы функции get_mask_card_number,
    которая должна возвращать маскированый номер карты
    :param num_card: номер карты
    :param expected: маскированый номер карты
    :return: маскированый номер карты
    """
    assert masks.get_mask_card_number(num_card) == expected

    with pytest.raises(ValueError) as exc_info:
        masks.get_mask_card_number(321)

    assert str(exc_info.value) == "Задан неверный номер карты"


@pytest.mark.parametrize(
    "account, expected",
    [
        (12345678900987654321, "**4321"),
        (9876543210987654, "**7654"),
    ],
)
def test_get_mask_account(account: int, expected: str) -> None:
    """
    Проверка рабоботы функции get_mask_account,
    которая должна возвращать маскированый номер счета
    :param account: номер счета
    :param expected: маскированый номер счета
    :return: маскированый номер счета
    """
    assert masks.get_mask_account(account) == expected

    with pytest.raises(ValueError) as exc_info:
        masks.get_mask_account(321)

    assert str(exc_info.value) == "Задан неверный номер счета"
