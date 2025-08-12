import os
from pathlib import Path
from typing import Any
from unittest.mock import Mock
import pytest

from src import decorators

# Задаём корневой путь проекта.
root_path = Path(__file__).resolve().parents[1]
file_of_names = os.path.join(root_path, "data\\my_log.txt")


def test_log_ok() -> None:
    """
    Проверка декоратора log на то, что он не мешает нормальной работе функций
    :return: Корректный результат работы фунции
    """

    @decorators.log()
    def add_numbers(a: int | float, b: int | float) -> int | float:
        """
        Функция для тестирования декоратора
        Просто складывает два числа
        :param a: первое число
        :param b: второе число
        :return: сумма чисел a и b
        """
        return a + b

    result = add_numbers(3, 5)
    assert result == 8


def test_log_err() -> None:
    """
    Проверка декоратора log на то, что отлавливает ошибки в работе функций
    :return: отлавливает ошибку в работе функции
    """

    @decorators.log()
    def add_numbers(a: int | float, b: int | float) -> int | float:
        """
        Функция для тестирования декоратора
        Просто складывает два числа
        :param a: первое число
        :param b: второе число
        :return: сумма чисел a и b
        """
        return a + b

    with pytest.raises(Exception):
        add_numbers(2, "3")


def test_log_ok_print_console(capsys: Any, log_ok_str: str) -> None:
    """
    Проверка декоратора log на корректность записи в консоль
    когда функция отрабатывает без ошибок
    :param capsys: Фикстура для захвата вывода в консоль
    :param log_ok_str: Фикстура лога при корректном срабатывании функции
    :return: Корректный текст в консоли
    """

    @decorators.log()
    def add_numbers(a: int | float, b: int | float) -> int | float:
        """
        Функция для тестирования декоратора
        Просто складывает два числа
        :param a: первое число
        :param b: второе число
        :return: сумма чисел a и b
        """
        return a + b

    mock_fread = Mock(return_value=log_ok_str)
    capsys.readouterr = mock_fread
    add_numbers(3, 5)
    captured = capsys.readouterr()
    assert captured == log_ok_str


def test_log_err_print_console(capsys: Any, log_err_str: str) -> None:
    """
    Проверка декоратора log на корректность записи в консоль
    когда функция отрабатывает с ошибокой
    :param capsys: Фикстура для захвата вывода в консоль
    :param log_err_str: Фикстура лога при срабатывании функции с ошибкой
    :return: Корректный текст в консоли
    """

    @decorators.log()
    def add_numbers(a: int | float, b: int | float) -> int | float:
        """
        Функция для тестирования декоратора
        Просто складывает два числа
        :param a: первое число
        :param b: второе число
        :return: сумма чисел a и b
        """
        return a + b

    with pytest.raises(Exception):
        add_numbers(2, "3")

    captured = capsys.readouterr()
    assert captured.out == f"{log_err_str}\n"


def test_log_print_file(log_ok_str: str, log_err_str: str) -> None:
    """
    Проверка декоратора log на корректность записи в консоль
    когда функция отрабатывает без ошибок
    :param log_ok_str: Фикстура лога при корректном срабатывании функции
    :param log_err_str: Фикстура лога при срабатывании функции с ошибкой
    :return: Корректный текст в консоли
    """

    @decorators.log(file_of_names)
    def add_numbers(a: int | float, b: int | float) -> int | float:
        """
        Функция для тестирования декоратора
        Просто складывает два числа
        :param a: первое число
        :param b: второе число
        :return: сумма чисел a и b
        """
        return a + b

    if os.path.exists(file_of_names):
        os.remove(file_of_names)

    add_numbers(3, 5)
    assert os.path.exists(file_of_names)

    mock_fread = Mock(return_value="test")
    with open(file_of_names, "r", encoding="utf-8") as file:
        file.read = mock_fread
        data_value = file.read()
        assert data_value == "test"

    if os.path.exists(file_of_names):
        os.remove(file_of_names)

    with pytest.raises(Exception):
        add_numbers(2, "3")
        assert os.path.exists(file_of_names)

    with open(file_of_names, "r", encoding="utf-8") as file:
        data_value = file.read()
        assert data_value == f"{log_err_str}\n"
