import os
from pathlib import Path

from src import use_file_names

# Задаём корневой путь проекта.
root_path = Path(__file__).resolve().parents[1]
file_of_names = os.path.join(root_path, "data\\names.txt")


def test_get_names_list_02(cleaned_name_list: list[str]) -> None:
    """
    Проверка функции get_names_list_02,
    которая должна возвращать очищеный список имен
    :param cleaned_name_list: фикстура с очищенным списком имен
    :return: очищеный список имен
    """
    assert use_file_names.get_names_list_02(file_of_names) == cleaned_name_list
