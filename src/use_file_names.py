import os


def get_names_list(use_file_name: str) -> list[str]:
    """
    Функция принимает имя файла и возвращает список имен, содержащихся в файле,
    игнорируя знаки препинания пробелы и цыфры
    :param use_file_name: имя файла
    :return: список имен из указанного файла
    """
    if not os.path.exists(use_file_name):
        return ["Такого файла не существует."]

    result_list_names = []
    del_chr = "0123456789,. |/!()[]{};:'&?@#№%^&*"

    with open(use_file_name, "r", encoding="utf-8") as file:
        list_mames_of_file = file.readlines()

    for i in list_mames_of_file:
        tmp_name = i.strip()
        for j in del_chr:
            tmp_name = tmp_name.replace(j, "")
        if tmp_name != "":
            result_list_names.append(tmp_name)

    return result_list_names


def get_names_list_02(use_file_name: str) -> list[str]:
    """
    Функция принимает имя файла и возвращает список имен, содержащихся в файле,
    игнорируя знаки препинания пробелы и цыфры
    :param use_file_name: имя файла
    :return: список имен из указанного файла
    """
    if not os.path.exists(use_file_name):
        return ["Такого файла не существует."]

    result_list_names = []

    with open(use_file_name, "r", encoding="utf-8") as file:
        list_mames_of_file = file.readlines()

    for i in list_mames_of_file:
        tmp_name = ""
        for j in i:
            if j.isalpha():
                tmp_name += j
        if tmp_name != "":
            result_list_names.append(tmp_name)

    return result_list_names


def get_list_of_lang_names(use_names_list: list[str], use_lang: str = "rus") -> list[str]:
    """
    Функция принимает список с именами
    и формирует список с именами только на английском или на русском языке
    :param use_names_list: список с именами
    :param use_lang: краткое наименование языка rus | eng
    :return: список с именами только на английском или на русском языке
    """
    result_list = []

    if use_lang == "eng":
        lang_chr = "abcdefghijklmnopqrstuvwxyz"
    else:
        lang_chr = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    for i in use_names_list:
        if i[0].lower() in lang_chr:
            result_list.append(i)

    return result_list


def set_list_to_file(use_list: list[str], use_file_name: str) -> None:
    """
    Функция принимает список строк и записывает его в файл
    :param use_list: список строк
    :param use_file_name: путь к файлу для записи списка
    :return: функция ничего не возвращает
    """
    with open(use_file_name, "w", encoding="utf-8") as file:
        for i in use_list:
            file.write(i + "\n")
