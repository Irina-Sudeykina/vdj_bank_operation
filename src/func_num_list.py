def get_intersect_num_list(num_list1: list[int], num_list2: list[int]) -> list[int]:
    """
    Фуккция получает 2 списка чисел
    и возвращает новый список, стодержащий только те числа, которые сть в обоих списках
    :param num_list1: список чисел 1
    :param num_list2: список чисел 2
    :return: список, стодержащий только те числа, которые сть в обоих списках
    """
    if (len(num_list1) == 0) or (len(num_list2) == 0):
        return []

    return list(set(num_list1).intersection(set(num_list2)))


def get_intersect_num_list_02(num_list1: list[int], num_list2: list[int]) -> list[int]:
    """
    Фуккция получает 2 списка чисел
    и возвращает новый список, стодержащий только те числа, которые сть в обоих списках
    :param num_list1: список чисел 1
    :param num_list2: список чисел 2
    :return: список, стодержащий только те числа, которые сть в обоих списках
    """
    return [elem for elem in num_list1 if elem in num_list2]


def get_num_palindrom_list(num_list: list[int]) -> list[int]:
    """
    Функция, которая получает на вход список чисел
    и возвращает новый список, содержащий только числа, которые являются палиндромами
    :param num_list: список чисел
    :return: список, содержащий только числа, которые являются палиндромами
    """
    result_list = []

    for i in num_list:
        if i == int(str(i)[::-1]):
            result_list.append(i)

    return result_list


def get_num_palindrom_list_02(num_list: list[int]) -> list[int]:
    """
    Функция, которая получает на вход список чисел
    и возвращает новый список, содержащий только числа, которые являются палиндромами
    :param num_list: список чисел
    :return: список, содержащий только числа, которые являются палиндромами
    """
    return [i for i in num_list if i == int(str(i)[::-1])]


def get_unicue_num_list(num_list1: list[int], num_list2: list[int]) -> list[int]:
    """
    Функция, которая получает на вход два списка чисел
    и возвращает новый список, содержащий только те числа, которые есть только в одном из списков
    :param num_list1: список чисел 1
    :param num_list2: список чисел 2
    :return: список, содержащий только те числа, которые есть только в одном из списков
    """
    result_list = []

    result_list += list(set(num_list1).difference(set(num_list2)))
    result_list += list(set(num_list2).difference(set(num_list1)))

    return result_list


def get_unicue_num_list_02(num_list1: list[int], num_list2: list[int]) -> list[int]:
    """
    Функция, которая получает на вход два списка чисел
    и возвращает новый список, содержащий только те числа, которые есть только в одном из списков
    :param num_list1: список чисел 1
    :param num_list2: список чисел 2
    :return: список, содержащий только те числа, которые есть только в одном из списков
    """
    return list(set(num_list1) - set(num_list2)) + list(set(num_list2) - set(num_list1))
