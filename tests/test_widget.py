import pytest

from src import widget


@pytest.mark.parametrize(
    "acc_card, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(acc_card: str, expected: str) -> None:
    """
    Проверка работы функции mask_account_card,
    которая должна возвращать маскированный номер счета или карты
    :param acc_card: наименование с номером карты или счета
    :param expected: маскированное значение номера карты/счета
    :return: маскированный номер счета или карты
    """
    assert widget.mask_account_card(acc_card) == expected

    with pytest.raises(ValueError) as exc_info:
        widget.mask_account_card("Visa Gold 599941422842635")

    assert str(exc_info.value) == "Задан неверный номер карты"


@pytest.mark.parametrize(
    "use_iso_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-05-11T02:26:18.0", "11.05.2024"),
    ],
)
def test_get_date(use_iso_date: str, expected: str, new_date_time: str, new_date_str: str) -> None:
    """
    Проверка работы функции get_date,
    которая должна возвращать строку с датой в формате ДД.ММ.ГГГГ (11.03.2024)
    :param use_iso_date: строка в формате 2024-03-11T02:26:18.671407
    :param expected: строка с датой в формате ДД.ММ.ГГГГ (11.03.2024)
    :return: строка с датой в формате ДД.ММ.ГГГГ (11.03.2024)
    """
    assert widget.get_date(use_iso_date) == expected
    assert widget.get_date(new_date_time) == new_date_str

    with pytest.raises(ValueError) as exc_info:
        widget.get_date("31.02.2005")

    assert str(exc_info.value) == "Задан неверный формат даты"
