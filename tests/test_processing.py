from typing import Any

from src import processing


def test_filter_by_state(
    operation_list_all: list[dict[str, Any]],
    operation_list_executed: list[dict[str, Any]],
    operation_list_canceled: list[dict[str, Any]],
    operation_list_no_state: list[dict[str, Any]],
) -> None:
    """
    Проверка работы функции filter_by_state,
    которая должна возвращать список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению
    :param operation_list_all: фикстура с полным списком операций
    :param operation_list_executed: фикстура со списком операций с типом EXECUTED
    :param operation_list_canceled: фикстура со списком операций с типом CANCELED
    :param operation_list_no_state: фикстура со списком операций с отсутствующим состоянимем
    :return: список словарей с указаным статусом операции
    """
    assert processing.filter_by_state(operation_list_all, "EXECUTED") == operation_list_executed
    assert processing.filter_by_state(operation_list_all, "CANCELED") == operation_list_canceled
    assert processing.filter_by_state(operation_list_all) == operation_list_executed
    assert processing.filter_by_state(operation_list_all, "test") == []
    assert processing.filter_by_state(operation_list_all, "executed") == operation_list_executed

    assert processing.filter_by_state(operation_list_no_state) == []
    assert processing.filter_by_state([]) == []


def test_sort_by_date(
    operation_list_all: list[dict[str, Any]],
    operation_list_sort_asc: list[dict[str, Any]],
    operation_list_sort_desc: list[dict[str, Any]],
    operation_list_no_date: list[dict[str, Any]],
) -> None:
    """
    Проверка работы функции sort_by_date,
    которая должна возвращать список, отсортированный по дате (date)
    :param operation_list_all: фикстура с полным списком операций
    :param operation_list_sort_asc: фикстура со списком операций отсортированных в порядке возрастания
    :param operation_list_sort_desc: фикстура со списком операций отсортированных в порядке убывания
    :param operation_list_no_date: фикстура со списком операций с отсутствующей датой
    :return: список словарей с указаным статусом операции
    """
    assert processing.sort_by_date(operation_list_all, True) == operation_list_sort_desc
    assert processing.sort_by_date(operation_list_all, False) == operation_list_sort_asc
    assert processing.sort_by_date(operation_list_all) == operation_list_sort_desc

    assert processing.sort_by_date(operation_list_no_date) == operation_list_no_date
    assert processing.sort_by_date([]) == []
