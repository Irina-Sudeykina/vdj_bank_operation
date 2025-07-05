import pytest

from src import func_num_list


@pytest.mark.parametrize(
    "num_list1, num_list2, expected",
    [
        ([1, 3, 5, 7], [3, 5, 9, 1], [1, 3, 5]),
        ([4, 3, 5, 7], [3, 5, 9, 1], [3, 5]),
    ],
)
def test_get_intersect_num_list(num_list1: list[int], num_list2: list[int], expected: list[int]) -> None:
    """
    Проверка фнкции get_intersect_num_list, которая возвращает список одинаковых чисел
    когда оба списка чисел не пустые
    :param num_list1: список чисел 1
    :param num_list2: список чисел 2
    :param expected: итоговый список чисел
    :return: ожидаем список одинаковых чисел
    """
    assert func_num_list.get_intersect_num_list(num_list1, num_list2) == expected


def test_get_intersect_empty_num_list() -> None:
    """
    Проверка фнкции get_intersect_num_list, которая возвращает список одинаковых чисел
    когда один или оба списка пустые
    :return: пустой список
    """
    assert func_num_list.get_intersect_num_list([], [3, 5, 9, 1]) == []
    assert func_num_list.get_intersect_num_list([1, 3, 5, 7], []) == []
    assert func_num_list.get_intersect_num_list([], []) == []


def test_get_intersect_num_list_02() -> None:
    """
    Проверка фнкции get_intersect_num_list_02, которая возвращает список одинаковых чисел
    когда оба списка чисел не пустые
    :return: ожидаем список одинаковых чисел
    """
    assert func_num_list.get_intersect_num_list_02([1, 3, 5, 7], [3, 5, 9, 1]) == [1, 3, 5]


def test_get_intersect_empty_num_list_02() -> None:
    """
    Проверка фнкции get_intersect_num_list_02, которая возвращает список одинаковых чисел
    когда один или оба списка пустые
    :return: пустой список
    """
    assert func_num_list.get_intersect_num_list_02([], [3, 5, 9, 1]) == []
    assert func_num_list.get_intersect_num_list_02([1, 3, 5, 7], []) == []
    assert func_num_list.get_intersect_num_list_02([], []) == []


def test_get_num_palindrom_list() -> None:
    """
    Проверка работы функции get_num_palindrom_list,
    котарая должна возвращать список с полиндромами
    когда список не пустой
    :return: список с полиндромами
    """
    assert func_num_list.get_num_palindrom_list([123, 343, 78987]) == [343, 78987]


def test_get_num_palindrom_empty_list() -> None:
    """
    Проверка работы функции get_num_palindrom_list,
    котарая должна возвращать список с полиндромами
    когда список пустой
    :return: пустой список
    """
    assert func_num_list.get_num_palindrom_list([]) == []


def test_get_num_palindrom_list_02() -> None:
    """
    Проверка работы функции get_num_palindrom_list_02,
    котарая должна возвращать список с полиндромами
    когда спискок не пустой
    :return: список с полиндромами
    """
    assert func_num_list.get_num_palindrom_list_02([123, 343, 78987]) == [343, 78987]


def test_get_num_palindrom_empty_list_02() -> None:
    """
    Проверка работы функции get_num_palindrom_list_02,
    котарая должна возвращать список с молиндромами
    когда список пустой
    :return: пустой список
    """
    assert func_num_list.get_num_palindrom_list_02([]) == []


"""
def test_get_num_palindrom_text_list() -> None:
    \"""
    Проверка работы функции get_num_palindrom_list,
    котарая должна возвращать список с полиндромами
    когда список не пустой, но содержит не числа, а строки
    :return: список с полиндромами
    \"""
    with pytest.raises(ValueError):
        func_num_list.get_num_palindrom_list([1, 33, 'ada'])
        func_num_list.get_num_palindrom_list(["test", 'abcd', 'ada', 5])

"""


def test_get_unicue_num_list() -> None:
    """
    Проверка функции get_unicue_num_list,
    которя должна возвращать список не одинаковых чисел
    когда оба списка не пустые
    :return: список не одинаковых чисел
    """
    assert func_num_list.get_unicue_num_list([1, 2, 3, 4, 5], [4, 5, 6, 7]) == [1, 2, 3, 6, 7]


def test_get_unicue_num_empty_list() -> None:
    """
    Проверка функции get_unicue_num_list,
    которя должна возвращать список не одинаковых чисел
    когда один или оба списка пустые
    :return: список не одинаковых чисел, либо пустой список
    """
    assert func_num_list.get_unicue_num_list([], [4, 5, 6, 7]) == [4, 5, 6, 7]
    assert func_num_list.get_unicue_num_list([1, 2, 3, 4, 5], []) == [1, 2, 3, 4, 5]
    assert func_num_list.get_unicue_num_list([], []) == []


def test_get_unicue_num_list_02() -> None:
    """
    Проверка функции get_unicue_num_list_02,
    которя должна возвращать список не одинаковых чисел
    когда оба списка не пустые
    :return: список не одинаковых чисел
    """
    assert func_num_list.get_unicue_num_list_02([1, 2, 3, 4, 5], [4, 5, 6, 7]) == [1, 2, 3, 6, 7]


def test_get_unicue_num_empty_list_02() -> None:
    """
    Проверка функции get_unicue_num_list_02,
    которя должна возвращать список не одинаковых чисел
    когда один или оба списка пустые
    :return: список не одинаковых чисел, либо пустой список
    """
    assert func_num_list.get_unicue_num_list_02([], [4, 5, 6, 7]) == [4, 5, 6, 7]
    assert func_num_list.get_unicue_num_list_02([1, 2, 3, 4, 5], []) == [1, 2, 3, 4, 5]
    assert func_num_list.get_unicue_num_list_02([], []) == []
