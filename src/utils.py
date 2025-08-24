import json
import logging
from typing import Any

from src import external_api

logging.basicConfig(filemode="w")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_of_json_file(json_file: str) -> list[dict[str, Any]]:
    """
    Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях
    :param json_file: строка, содержащаая путь до JSON-файла
    :return: список словарей с данными о финансовых транзакциях
    """
    try:
        logger.info(f"Открываем json файл {json_file} с транзакцтями на чтение")
        with open(json_file, mode="r", encoding="utf-8") as operations_file:
            try:
                logger.info("Записываем содержимое json файла {json_file} в переменную operations_data")
                operations_data = json.load(operations_file)
                operations_data = list(operations_data)
                operations_data_result = []
                for i in operations_data:
                    if len(i) != 0:
                        operations_data_result.append(
                            {
                                "id": i.get("id"),
                                "state": i.get("state", ""),
                                "date": i.get("date", ""),
                                "amount": i.get("operationAmount", "").get("amount"),
                                "currency_name": i.get("operationAmount", "").get("currency", "").get("name", ""),
                                "currency_code": i.get("operationAmount", "")
                                .get("currency", "")
                                .get("code", "")
                                .upper(),
                                "from": i.get("from", ""),
                                "to": i.get("to", ""),
                                "description": i.get("description", ""),
                            }
                        )
            except json.JSONDecodeError:
                logger.error(f"Десериализация json файла {json_file} невозможна. Что-то с ним не так.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл {json_file} не найден.")
        return []

    return operations_data_result


def get_amount_transaction(transaction: dict[str, Any]) -> float:
    """
    Функция принимает словрь с транзакцией и возвращает сумму транзакции в рублях
    :param transaction: словарь с транзакцией
    :return: сумма транзакции в рублях
    """
    amount = float(transaction.get("operationAmount", "").get("amount", 0))
    logger.debug(f"Сумма транзакции: {amount}")
    currency = transaction.get("operationAmount", "").get("currency", "").get("code", "RUB")
    logger.debug(f"Валюта транзакции: {currency}")

    logger.info("Проверяем в какой валюте была транзакция")
    if currency == "RUB":
        result_amount = amount
    elif (currency == "USD") or (currency == "EUR"):
        logger.info(f"Переводим валюту транзакции из {currency} в RUB")
        result_amount = external_api.conversion_currency(amount, currency, "RUB")
    else:
        result_amount = amount

    return result_amount
