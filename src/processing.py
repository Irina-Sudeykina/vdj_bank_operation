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
