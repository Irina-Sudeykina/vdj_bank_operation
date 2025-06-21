from typing import Union

from src import func_num_list


def sum_of_values(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Функция, суммирующая два числа
    """
    return a + b


print(sum_of_values(4, 7.6))

num_list1 = [1, 3, 5, 7]
num_list2 = [3, 5, 9, 1]

print(func_num_list.get_intersect_num_list(num_list1, num_list2))
print(func_num_list.get_intersect_num_list_02(num_list1, num_list2))
print(func_num_list.get_unicue_num_list(num_list1, num_list2))
print(func_num_list.get_unicue_num_list_02(num_list1, num_list2))

num_list = [121, 576, 786, 7896987]

print(func_num_list.get_num_palindrom_list(num_list))
print(func_num_list.get_num_palindrom_list_02(num_list))


def get_area_of_circle(radius_of_circle: Union[int, float]) -> Union[int, float]:
    """
    Функция рассчитывает площадь окружности
    :param radius_of_circle: радиус окружности
    :return: площадь окружности
    """
    pi = 3.14

    return pi * (radius_of_circle**2)


def get_description_circle(radius_of_circle: Union[int, float], area_of_circle: Union[int, float]) -> str:
    """
    Процедура возвращает информацию о радиусе и площади окружности
    :param radius_of_circle: радиус окружности
    :param area_of_circle: площадь окружности
    :return: информация о радиусе и площади окружности
    """
    return "Radius is " + str(radius_of_circle) + "; area is " + str(round(area_of_circle, 2))


def get_info_circle(radius_of_circle: Union[int, float]) -> None:
    """
    Функция расчитывает площадь окружности и выводит информацию о радиусе и площади окружности
    :param radius_of_circle: радиус окружности
    :return: информация о радиусе и площади окружности
    """
    area_of_circle = get_area_of_circle(radius_of_circle)
    description_circle = get_description_circle(radius_of_circle, area_of_circle)

    print(description_circle)


radius_circle = int(input("Enter circle radius (int): "))

get_info_circle(radius_circle)
