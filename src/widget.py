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
