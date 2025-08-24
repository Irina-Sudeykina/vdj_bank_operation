import os
from pathlib import Path

from src import extractors, generators, processing, utils, widget

# Задаём корневой путь проекта.
root_path = Path(__file__).resolve().parents[0]

transactions_file_json = os.path.join(root_path, "data\\operations_03.json")
transactions_file_csv = os.path.join(root_path, "data\\transactions.csv")
transactions_file_xlsx = os.path.join(root_path, "data\\transactions_excel.xlsx")


def main() -> None:
    num_operation = int(
        input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
        )
    )
    if num_operation == 1:
        print("Для обработки выбран JSON-файл.")
        transactions_list = utils.get_transactions_of_json_file(transactions_file_json)
    elif num_operation == 2:
        print("Для обработки выбран CSV-файл.")
        transactions_list = extractors.get_operations_csv(transactions_file_csv)
    else:
        print("Для обработки выбран XLSX-файл.")
        transactions_list = extractors.get_operations_xlsx(transactions_file_xlsx)

    status_operation = input(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
"""
    ).upper()

    while status_operation not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"""Статус операции "{status_operation}" недоступен.""")
        status_operation = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
"""
        ).upper()

    transactions_list = processing.filter_by_state(transactions_list, status_operation)
    print(f"""Операции отфильтрованы по статусу "{status_operation}".""")

    is_sorted = input("Отсортировать операции по дате? Да/Нет\n").lower()
    if is_sorted == "да":
        is_desc = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        if is_desc == "по возрастанию":
            transactions_list = processing.sort_by_date(transactions_list, False)
        else:
            transactions_list = processing.sort_by_date(transactions_list, True)

    is_only_rub = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
    if is_only_rub == "да":
        rub_transactions = generators.filter_by_currency(transactions_list, "RUB")
        transactions_list = list(rub_transactions)

    is_filtred = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
    if is_filtred == "да":
        user_text = input("Введите слово для фильтрации по описанию\n")
        transactions_list = processing.process_bank_search(transactions_list, user_text)

    if len(transactions_list) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"\nВсего банковских операций в выборке: {len(transactions_list)}")
        for i in transactions_list:
            print(
                f"""
{widget.get_date(i.get("date", ""))} {i.get("description", "")}
{widget.mask_account_card(i.get("from", ""))}
Сумма: {i.get("amount", "")} {i.get("currency_name", "")}"""
            )


if __name__ == "__main__":
    main()
