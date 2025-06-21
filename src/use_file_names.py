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
    del_chr = "0123456789,.|/!()[]{};:'&?@#№%^&*"

    with open(use_file_name, "r", encoding="utf-8") as file:
        list_mames_of_file = file.readlines()

    for i in list_mames_of_file:
        tmp_name = i.strip()
        for j in del_chr:
            tmp_name = tmp_name.replace(j, "")
        if tmp_name != "":
            result_list_names.append(tmp_name)

    return result_list_names
