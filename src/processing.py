from typing import Any


def filter_by_state(use_list_operation: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Функция принимает список словарей
    и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению
    :param use_list_operation: список словарей - банковские операции
    :param state: строка - статус операции, по умолчанию = EXECUTED
    :return: список словарей с указаным статусом операции
    """
    return [i for i in use_list_operation if str(i["state"]).upper() == str(state).upper()]


def sort_by_date(use_list_operation: list[dict[str, Any]], sort_order: bool = True) -> list[dict[str, Any]]:
    """
    Функция принимает список словарей - банковские операции
    и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате (date).
    :param use_list_operation: список словарей - банковские операции
    :param sort_order: необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    :return: отсортированный по дате список словарей - банковские операции
    """
    return sorted(use_list_operation, key=lambda tpl: tpl["date"], reverse=sort_order)
