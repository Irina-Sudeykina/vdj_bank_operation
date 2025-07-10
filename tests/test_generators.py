from typing import Any

from src import generators


def test_filter_by_currency(
    transactions_all: list[dict[str, Any]],
    usd_transaction_one: dict[str, Any],
) -> None:
    """
    Проверка работы функции filter_by_currency,
    которая должна возвращать итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)
    :param transactions_all: Фикстура с полным списком транзакций
    :param usd_transaction_one: Фикстура с первой транзакцией в валюте USD
    :return: транзакция, где валюта операции соответствует заданной (например, USD)
    """
    usd_transactions = generators.filter_by_currency(transactions_all, "USD")
    assert next(usd_transactions) == usd_transaction_one
