import os
from typing import Any

import requests
from dotenv import load_dotenv


def conversion_currency(amount: float, currency_from: str, currency_to: str) -> float:
    """
    Функция конвертации суммы из одной валюты в другую
    :param amount: сумма, которую нужно сконвертировать
    :param currency_from: конвертируемая валюта
    :param currency_to: валюта в которую нужно конвентировать
    :return: сконвертированная сумма
    """
    url = "https://api.apilayer.com/exchangerates_data/convert"

    load_dotenv()
    api_key = str(os.getenv("API_KEY"))

    payload: dict[str, Any] = {"amount": amount, "from": currency_from, "to": currency_to}
    headers = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers, params=payload)
        result = response.json()
        return round(float(result.get("result", 0)), 2)
    except Exception as err:
        print(f"Что-то пошло не так при обращении к api.apilayer.com: {err}")
        return float(0)
