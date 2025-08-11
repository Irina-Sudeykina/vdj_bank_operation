import json
from typing import Any

from src import external_api


def get_transactions_of_json_file(json_file: str) -> list[dict[str, Any]]:
    """
    Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях
    :param json_file: строка, содержащаая путь до JSON-файла
    :return: список словарей с данными о финансовых транзакциях
    """
    try:
        with open(json_file, mode="r", encoding="utf-8") as operations_file:
            try:
                operations_data = json.load(operations_file)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []

    return list(operations_data)


def get_amount_transaction(transaction: dict[str, Any]) -> float:
    """
    Функция принимает словрь с транзакцией и возвращает сумму транзакции в рублях
    :param transaction: словарь с транзакцией
    :return: сумма транзакции в рублях
    """
    amount = float(transaction.get("operationAmount", "").get("amount", 0))
    currency = transaction.get("operationAmount", "").get("currency", "").get("code", "RUB")

    if currency == "RUB":
        result_amount = amount
    elif (currency == "USD") or (currency == "EUR"):
        result_amount = external_api.conversion_currency(amount, currency, "RUB")
    else:
        result_amount = amount

    return result_amount
