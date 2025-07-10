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
