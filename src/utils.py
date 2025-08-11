import json
from typing import Any


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
