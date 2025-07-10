from typing import Any

import pytest

from src import generators


def test_filter_by_currency(
    transactions_all: list[dict[str, Any]],
    usd_transaction_one: dict[str, Any],
    usd_transaction_two: dict[str, Any],
    rub_transaction_one: dict[str, Any],
    rub_transaction_two: dict[str, Any],
    transactions_no_operation_amount: list[dict[str, Any]],
    transactions_no_currency: list[dict[str, Any]],
    transactions_no_currency_code: list[dict[str, Any]],
) -> None:
    """
    Проверка работы функции filter_by_currency,
    которая должна возвращать итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)
    :param transactions_all: Фикстура с полным списком транзакций
    :param usd_transaction_one: Фикстура с первой транзакцией в валюте USD
    :param usd_transaction_two: Фикстура со второй транзакцией в валюте USD
    :param rub_transaction_one: Фикстура с первой транзакцией в валюте RUB
    :param rub_transaction_two: Фикстура со второй транзакцией в валюте RUB
    :param transactions_no_operation_amount: Фикстура со списком транзакций, где нет operationAmount
    :param transactions_no_currency: Фикстура со списком транзакций, где нет currency
    :param transactions_no_currency_code: Фикстура со списком транзакций, где нет кода валюты
    :return: транзакция, где валюта операции соответствует заданной (например, USD)
    """
    usd_transactions = generators.filter_by_currency(transactions_all, "USD")
    assert next(usd_transactions) == usd_transaction_one
    assert next(usd_transactions) == usd_transaction_two

    rub_transactions = generators.filter_by_currency(transactions_all)
    assert next(rub_transactions) == rub_transaction_one
    assert next(rub_transactions) == rub_transaction_two

    cny_transactions = generators.filter_by_currency(transactions_all, "CNY")
    transactions_no_oper_amount = generators.filter_by_currency(transactions_no_operation_amount)
    transactions_no_curr = generators.filter_by_currency(transactions_no_currency, "RUB")
    transactions_no_curr_code = generators.filter_by_currency(transactions_no_currency_code, "USD")
    with pytest.raises(StopIteration):
        next(cny_transactions)
        next(transactions_no_oper_amount)
        next(transactions_no_curr)
        next(transactions_no_curr_code)


def test_transaction_descriptions(
    transactions_all: list[dict[str, Any]],
    transactions_no_description: list[dict[str, Any]],
) -> None:
    """
    Проверка работы функции transaction_descriptions,
    которая должна возвращать описание каждой операции по очереди
    :param transactions_all: Фикстура с полным списком транзакций
    :param transactions_no_description: Фикстура со списком транзакций, где нет описания
    :return: описание каждой операции по очереди
    """
    descriptions = generators.transaction_descriptions(transactions_all)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"

    no_descriptions = generators.transaction_descriptions(transactions_no_description)
    assert next(no_descriptions) == ""
