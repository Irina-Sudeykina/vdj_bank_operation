from src import decorators


@decorators.log()
def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки номера банковской карты
    :param card_number: номер карты в формате 1234123412341234
    :return: маска номера карты в формате XXXX XX** **** XXXX, где X — это цифра номера
    """
    if len(str(card_number)) == 16:
        return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
    else:
        raise ValueError("Задан неверный номер карты")


def get_mask_account(account_num: int) -> str:
    """
    Функция маскировки номера банковского счета
    :param account_num: номер банковского счета в формате 12345678900987654321
    :return: маска номера счета в формате **XXXX, где X — это цифра номера
    """
    if len(str(account_num)) <= 4:
        raise ValueError("Задан неверный номер счета")
    else:
        return f"**{str(account_num)[-4:]}"
