from typing import Any

import pandas as pd


def get_operations_csv(csv_file: str) -> list[dict[str, Any]]:
    """
    Функция для считывания финансовых операций из CSV
    принимает путь к файлу CSV в качестве аргумента
    возвращает список словарей с транзакциями
    :param csv_file: путь к файлу CSV
    :return: список словарей с транзакциями
    """
    try:
        df = pd.read_csv(csv_file)
        # Преобразуем ключи к строковым типам
        result: list[dict[str, Any]] = [{str(k): v for k, v in record.items()} for record in df.to_dict("records")]
    except Exception:
        result = []
    return result


def get_operations_xlsx(xlsx_file: str) -> list[dict[Any, Any]]:
    """
    Функция для считывания финансовых операций из XLSX
    принимает путь к файлу CSV в качестве аргумента
    возвращает список словарей с транзакциями
    :param xlsx_file: путь к файлу XLSX
    :return: список словарей с транзакциями
    """
    try:
        df = pd.read_excel(xlsx_file)
        # Преобразуем ключи к строковым типам
        result: list[dict[str, Any]] = [{str(k): v for k, v in record.items()} for record in df.to_dict("records")]
    except Exception:
        result = []
    return result
