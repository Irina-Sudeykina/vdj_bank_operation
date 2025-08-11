import os
import sys
from io import StringIO
from typing import Any
from unittest.mock import patch

from dotenv import load_dotenv

from src import external_api


@patch("requests.get")
def test_conversion_currency(mock_get: Any) -> None:
    """
    Проверка функции conversion_currency, конвертирующей сумму из одной валюты в другую
    :param mock_get: Фикстура заменяющая requests.get
    :return: сконвертированная сумма
    """
    url = "https://api.apilayer.com/exchangerates_data/convert"

    load_dotenv()
    api_key = str(os.getenv("API_KEY"))

    payload = {"amount": 100, "from": "USD", "to": "RUB"}
    headers = {"apikey": api_key}

    mock_get.return_value.json.return_value = {"result": 8100.0}
    assert external_api.conversion_currency(100, "USD", "RUB") == 8100.0
    mock_get.assert_called_once_with(url, headers=headers, params=payload)


@patch("requests.get")
def test_conversion_currency_err(mock_get: Any) -> None:
    """
    Проверка функции conversion_currency, конвертирующей сумму из одной валюты в другую
    Отлавливаем ошибки
    :param mock_get: Фикстура заменяющая requests.get
    :return: сконвертированная сумма
    """
    mock_get.side_effect = Exception("Искусственная ошибка при обращении к API")

    # Вызываем функцию, ожидая возвращения нуля при возникновении ошибки
    result = external_api.conversion_currency(100, "USD", "RUB")

    # Проверяем, что результат соответствует ожиданиям
    assert isinstance(result, float)
    assert result == 0.0

    captured_output = StringIO()
    sys.stdout = captured_output  # перенаправляем stdout

    external_api.conversion_currency(100, "USD", "RUB")  # повторно запускаем функцию для захвата output

    sys.stdout = sys.__stdout__  # восстанавливаем стандартный поток вывода

    expected_message = (
        "Что-то пошло не так при обращении к api.apilayer.com: Искусственная ошибка при обращении к API\n"
    )
    assert captured_output.getvalue().strip() == expected_message.strip()
