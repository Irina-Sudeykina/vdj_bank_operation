import logging

logging.basicConfig(filemode="w")

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки номера банковской карты
    :param card_number: номер карты в формате 1234123412341234
    :return: маска номера карты в формате XXXX XX** **** XXXX, где X — это цифра номера
    """
    logger.info(f"Проверяем номер карты: {card_number}")
    if len(str(card_number)) == 16:
        logger.info("Возвращаем маскированный номер")
        return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
    else:
        logger.error(f"Задан неверный номер карты: {card_number}")
        raise ValueError("Задан неверный номер карты")


def get_mask_account(account_num: int) -> str:
    """
    Функция маскировки номера банковского счета
    :param account_num: номер банковского счета в формате 12345678900987654321
    :return: маска номера счета в формате **XXXX, где X — это цифра номера
    """
    logger.info(f"Проверяем номер банковского счета: {account_num}")
    if len(str(account_num)) <= 4:
        logger.error(f"Задан неверный номер счета: {account_num}")
        raise ValueError("Задан неверный номер счета")
    else:
        logger.info("Возвращаем маскированный номер счета")
        return f"**{str(account_num)[-4:]}"
