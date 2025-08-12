import os
from pathlib import Path
from typing import Any
from unittest.mock import patch
from src import utils

# Задаём корневой путь проекта.
root_path = Path(__file__).resolve().parents[1]
file_of_names = os.path.join(root_path, "data\\operations_03.json")


def test_get_amount_transaction(
    transaction_amount_rub: dict[str, Any],
    transaction_amount_cny: dict[str, Any]
) -> None:
    """
    Проверка работы функции get_amount_transaction, которая
    принимает словрь с транзакцией и возвращает сумму транзакции в рублях
    :param transaction_amount_rub: Фикстура словаря транзакции, где сумма в рублях
    :param transaction_amount_cny: Фикстура словаря транзакции, где сумма в CNY
    :param mock_get: Фикстура заменяющая requests.get
    :return: сумма транзакции в рублях
    """
    assert utils.get_amount_transaction(transaction_amount_rub) == 31957.58
    assert utils.get_amount_transaction(transaction_amount_cny) == 8221.37


@patch("requests.get")
def test_get_amount_transaction_convert(mock_get: Any) -> None:
    """
    Проверка работы функции get_amount_transaction, которая
    принимает словрь с транзакцией и возвращает сумму транзакции в рублях
    Осуществление конвертации валюты
    :param mock_get: Фикстура заменяющая requests.get
    :return: сумма транзакции в рублях
    """
    mock_get.return_value.json.return_value = {"result": 8100.0}
    transaction_amount_usd = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "desctiption": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    assert utils.get_amount_transaction(transaction_amount_usd) == 8100.0


bad_json_file = os.path.join(root_path, "data\\bad_json_file.json")


def test_get_transactions_of_json_file(operations_json_file: str) -> None:
    """
    Проверка работы функции get_transactions_of_json_file,
    которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях
    :param operations_json_file: Фикстура списка словарей из json файла с финансовыми операциями
    :return: список словарей с данными о финансовых транзакциях
    """
    assert utils.get_transactions_of_json_file(file_of_names) == operations_json_file

    assert os.path.exists(file_of_names)

    assert utils.get_transactions_of_json_file("test") == []
    assert utils.get_transactions_of_json_file(bad_json_file) == []
