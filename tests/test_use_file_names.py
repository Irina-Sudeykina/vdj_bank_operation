import os
from pathlib import Path

from src import use_file_names

# Задаём корневой путь проекта.
root_path = Path(__file__).resolve().parents[1]
file_of_names = os.path.join(root_path, "data\\names.txt")


def test_get_names_list(cleaned_name_list: list[str]) -> None:
    """
    Проверка функции get_names_list_02,
    которая должна возвращать очищеный список имен
    :param cleaned_name_list: фикстура с очищенным списком имен
    :return: очищеный список имен
    """
    assert use_file_names.get_names_list(file_of_names) == cleaned_name_list
    assert use_file_names.get_names_list_02(file_of_names) == cleaned_name_list

    assert use_file_names.get_names_list("неправильный путь к файлу") == ["Такого файла не существует."]
    assert use_file_names.get_names_list_02("неправильный путь к файлу") == ["Такого файла не существует."]


def test_get_list_of_lang_names(
    cleaned_name_list: list[str], eng_name_list: list[str], rus_name_list: list[str]
) -> None:
    """
    Проверка функции get_list_of_lang_names,
    которая должна возвращать список с именами только на английском или только на русском
    :param cleaned_name_list: фикстура с очищенным списком имен
    :param eng_name_list: фикстура со списком имен на английском
    :param rus_name_list: фикстура со списком имен на русском
    :return: список имен на русском или на английском
    """
    assert use_file_names.get_list_of_lang_names(cleaned_name_list, "eng") == eng_name_list
    assert use_file_names.get_list_of_lang_names(cleaned_name_list) == rus_name_list


def test_set_list_to_file(
    eng_name_list: list[str], rus_name_list: list[str], eng_data_file: str, rus_data_file: str
) -> None:
    """
    Проверка функции set_list_to_file,
    которая должна записывать список имен в файл
    :param eng_name_list: фикстура со списком имен на английском
    :param rus_name_list: фикстура со списком имен на русском
    :param eng_data_file: фикстура содержимого файла с именами на английском
    :param rus_data_file: фикстура содержимого файла с именами на русском
    :return: файл со списком имен
    """
    file_of_eng_names = os.path.join(root_path, "data\\eng_names.txt")
    file_of_rus_names = os.path.join(root_path, "data\\rus_names.txt")
    use_file_names.set_list_to_file(eng_name_list, file_of_eng_names)
    use_file_names.set_list_to_file(rus_name_list, file_of_rus_names)

    assert os.path.exists(file_of_eng_names)
    assert os.path.exists(file_of_rus_names)

    with open(file_of_eng_names, "r", encoding="utf-8") as file:
        data_value = file.read()
        assert data_value == eng_data_file

    with open(file_of_rus_names, "r", encoding="utf-8") as file:
        data_value = file.read()
        assert data_value == rus_data_file
