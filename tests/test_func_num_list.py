from src import func_num_list


def test_get_intersect_num_list() -> None:
    """
    Проверка фнкции get_intersect_num_list, которая возвращает список одинаковых чисел
    когда оба списка чисел не пустые
    :return: ожидаем список одинаковых чисел
    """
    assert func_num_list.get_intersect_num_list([1, 3, 5, 7], [3, 5, 9, 1]) == [1, 3, 5]


def test_get_intersect_empty_num_list() -> None:
    """
    Проверка фнкции get_intersect_num_list, которая возвращает список одинаковых чисел
    когда один или оба списка пустые
    :return: пустой список
    """
    assert func_num_list.get_intersect_num_list([], [3, 5, 9, 1]) == []
    assert func_num_list.get_intersect_num_list([1, 3, 5, 7], []) == []
    assert func_num_list.get_intersect_num_list([], []) == []
