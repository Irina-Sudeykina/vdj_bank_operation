def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки номера банковской карты
    :param card_number: номер карты в формате 1234123412341234
    :return: маска номера карты в формате XXXX XX** **** XXXX, где X — это цифра номера
    """
    if len(str(card_number)) == 16:
        return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
    else:
        return "Задан неверный номер карты"


def get_mask_account(account_num: int) -> str:
    """
    Функция маскировки номера банковского счета
    :param account_num: номер банковского счета в формате 12345678900987654321
    :return: маска номера счета в формате **XXXX, где X — это цифра номера
    """
    return f"**{str(account_num)[-4:]}"


def mask_account_card(acc_card: str) -> str:
    """
    Функция принимает строку формата Visa Platinum 7000792289606361
    или Maestro 7000792289606361 или Счет 73654108430135874305
    и возвращает строку с замаскированным значением номера карты/счета
    :param acc_card: строка, содержащая номер карты или счета
    :return: строка с замаскированным значением номера карты/счета
    """
    if acc_card[-20:].isdigit():
        return f"{acc_card[:(len(acc_card) - 20)]}{get_mask_account(acc_card[-20:])}"
    else:
        return f"{acc_card[:(len(acc_card) - 16)]}{get_mask_card_number(acc_card[-16:])}"
