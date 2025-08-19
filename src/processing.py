import re
from typing import Any


def filter_by_state(operation_list: list[dict[str, Any | None]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Функция принимает список словарей
    и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению
    :param operation_list: список словарей - банковские операции
    :param state: строка - статус операции, по умолчанию = EXECUTED
    :return: список словарей с указаным статусом операции
    """
    return [i for i in operation_list if str(i.get("state")).upper() == str(state).upper()]


def sort_by_date(operation_list: list[dict[str, Any]], is_reverse_sort: bool = True) -> list[dict[str, Any]]:
    """
    Функция принимает список словарей - банковские операции
    и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате (date).
    :param operation_list: список словарей - банковские операции
    :param is_reverse_sort: необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    :return: отсортированный по дате список словарей - банковские операции
    """
    return sorted(operation_list, key=lambda tpl: tpl.get("date", ""), reverse=is_reverse_sort)


def process_bank_search(data: list[dict], search: str = "") -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании есть данная строка.
    :param data: список словарей с данными о банковских операциях
    :param search: строка поиска
    :return: отфильтрованный список словарей с данными о банковских операциях
    """
    pattern = re.compile(rf"{search.lower()}")
    return [i for i in data if re.findall(pattern, str(i.get("description")).lower())]
