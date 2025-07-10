from typing import Any, Generator


def filter_by_currency(transaction_list: list[dict[str, Any]], currency: str = "RUB") -> Generator[dict[str, Any]]:
    """
    Функция принимает список словарей с транзакциями
    и возвращает итератор с словарей, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)
    :param transaction_list: список словарей с транзакциями
    :param currency: валюта операции (например, USD)
    :return: итератор с словарей
    """
    return (
        x
        for x in transaction_list
        if x.get("operationAmount", "").get("currency", "").get("code", "").upper() == currency.upper()
    )


def transaction_descriptions(transaction_list: list[dict[str, Any]]) -> Generator[str]:
    """
    Функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди
    :param transaction_list: список словарей с транзакциями
    :return: описание каждой операции по очереди
    """
    for transaction in transaction_list:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> list[str]:
    """
    Функция принимает начальное и конечное значения для генерации
    и возвращает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    :param start: начальное значение для генерации
    :param stop: конечное значение для генерации
    :return: номера банковских карт в формате XXXX XXXX XXXX XXXX
    """
    result_card_numbers = (str(x).zfill(16) for x in range(start, stop + 1))
    result_card_numbers = (f"{x[0:4]} {x[4:9]} {x[9:13]} {x[-4:]}" for x in result_card_numbers)

    return list(result_card_numbers)
