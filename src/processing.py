from typing import Any


def filter_by_state(operation_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Функция принимает список словарей
    и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению
    :param operation_list: список словарей - банковские операции
    :param state: строка - статус операции, по умолчанию = EXECUTED
    :return: список словарей с указаным статусом операции
    """
    return [i for i in operation_list if str(i["state"]).upper() == str(state).upper()]


def sort_by_date(operation_list: list[dict[str, Any]], is_reverse_sort: bool = True) -> list[dict[str, Any]]:
    """
    Функция принимает список словарей - банковские операции
    и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате (date).
    :param use_list_operation: список словарей - банковские операции
    :param sort_order: необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    :return: отсортированный по дате список словарей - банковские операции
    """
    return sorted(operation_list, key=lambda tpl: tpl["date"], reverse=is_reverse_sort)
