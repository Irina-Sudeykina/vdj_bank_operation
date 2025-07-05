import pytest

from src import func_num_list


@pytest.mark.parametrize(
    "num_list1, num_list2, expected",
    [
        ([1, 3, 5, 7], [3, 5, 9, 1], [1, 3, 5]),
        ([4, 3, 5, 7], [3, 5, 9, 1], [3, 5]),
        ([], [3, 5, 9, 1], []),
        ([1, 3, 5, 7], [], []),
        ([], [], []),
    ],
)
def test_get_intersect_num_list(num_list1: list[int], num_list2: list[int], expected: list[int]) -> None:
    """
    Проверка фнкции get_intersect_num_list, которая возвращает список одинаковых чисел
    :param num_list1: список чисел 1
    :param num_list2: список чисел 2
    :param expected: итоговый список чисел
    :return: ожидаем список одинаковых чисел
    """
    assert func_num_list.get_intersect_num_list(num_list1, num_list2) == expected
    assert func_num_list.get_intersect_num_list_02(num_list1, num_list2) == expected


@pytest.mark.parametrize(
    "my_list, expected",
    [
        ([123, 343, 78987], [343, 78987]),
        ([678, 676, 888], [676, 888]),
        ([], []),
    ],
)
def test_get_num_palindrom_list(my_list: list[int], expected: list[int]) -> None:
    """
    Проверка работы функции get_num_palindrom_list,
    котарая должна возвращать список с полиндромами
    :param my_list: список чисел
    :param expected: итоговый список чисел
    :return: список с полиндромами
    """
    assert func_num_list.get_num_palindrom_list(my_list) == expected
    assert func_num_list.get_num_palindrom_list_02(my_list) == expected


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


@pytest.mark.parametrize(
    "num_list1, num_list2, expected",
    [
        ([1, 2, 3, 4, 5], [4, 5, 6, 7], [1, 2, 3, 6, 7]),
        ([4, 3, 5, 7], [3, 5, 9, 1], [4, 7, 9, 1]),
        ([], [3, 5, 9, 1], [9, 3, 5, 1]),
        ([1, 3, 5, 7], [], [1, 3, 5, 7]),
        ([], [], []),
    ],
)
def test_get_unicue_num_list(num_list1: list[int], num_list2: list[int], expected: list[int]) -> None:
    """
    Проверка функции get_unicue_num_list,
    которя должна возвращать список не одинаковых чисел
    :param num_list1: список чисел 1
    :param num_list2: список чисел 2
    :param expected: итоговый список чисел
    :return: список не одинаковых чисел
    """
    assert func_num_list.get_unicue_num_list(num_list1, num_list2) == expected
    assert func_num_list.get_unicue_num_list_02(num_list1, num_list2) == expected
