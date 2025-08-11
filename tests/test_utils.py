import os
from pathlib import Path

from src import utils

# Задаём корневой путь проекта.
root_path = Path(__file__).resolve().parents[1]
file_of_names = os.path.join(root_path, "data\\operations_03.json")
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
