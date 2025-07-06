from datetime import datetime

from src import masks


def mask_account_card(acc_card: str) -> str:
    """
    Функция принимает строку формата Visa Platinum 7000792289606361
    или Maestro 7000792289606361 или Счет 73654108430135874305
    и возвращает строку с замаскированным значением номера карты/счета
    :param acc_card: строка, содержащая номер карты или счета
    :return: строка с замаскированным значением номера карты/счета
    """
    if acc_card[-20:].isdigit():
        return f"{acc_card[:(len(acc_card) - 20)]}{masks.get_mask_account(int(acc_card[-20:]))}"
    else:
        return f"{acc_card[:(len(acc_card) - 16)]}{masks.get_mask_card_number(int(acc_card[-16:]))}"


def get_date(use_iso_date: str) -> str:
    """
    Функция принимает строку в формате 2024-03-11T02:26:18.671407
    и возвращает строку с датой в формате ДД.ММ.ГГГГ (11.03.2024)
    :param use_iso_date: строка в формате 2024-03-11T02:26:18.671407
    :return: строка с датой в формате ДД.ММ.ГГГГ (11.03.2024)
    """
    try:
        return datetime.fromisoformat(use_iso_date).strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Задан неверный формат даты")
