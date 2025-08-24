# Проект "Виджет финансовых операций"

 ## Описание:
 Проект "Виджет финансовых операций" - это проект на Python, 
 содержащий функции для работы с банковскими операциями
 
## Установка:
 1. Клонируйте репозиторий:
 ```
 git clone https://github.com/Irina-Sudeykina/vdj_bank_operation.git
 ```

 1. Установите зависимости:
 ```
 pip install -r requirements.txt
 ```

 ## Использование:
 ### Функция **get_mask_card_number**(card_number: int) -> str
  Функция маскировки номера банковской карты, 
  принимает номер карты в формате 1234123412341234
  и возвращает маску номера карты в формате XXXX XX** **** XXXX, где X — это цифра номера

 #### Пример использования: 
```
 from src import masks
 
 print(masks.get_mask_card_number(1234123412341234))
 ```
 #### Пример работы:
 ```
 1234 12** **** 1234
 ```

 ### Функция **get_mask_account**(account_num: int) -> str
 Функция маскировки номера банковского счета, 
 принимает номер банковского счета в формате 12345678900987654321
 и возвращает маску номера счета в формате **XXXX, где X — это цифра номера

 #### Пример использования: 
 ```
 from src import masks
 
 print(masks.get_mask_account(12345678900987654321))
 ```
 #### Пример работы:
 ```
 **4321
 ```

 ### Функция **mask_account_card**(acc_card: str) -> str
 Функция принимает строку формата Visa Platinum 7000792289606361
 или Maestro 7000792289606361 или Счет 73654108430135874305
 и возвращает строку с замаскированным значением номера карты/счета

 #### Пример использования: 
  ```
 from src import widget
 
 print(widget.mask_account_card("Счет 73654108430135874305"))
 print(widget.mask_account_card("Maestro 7000792289606361"))
 print(widget.mask_account_card("Visa Platinum 7000792289606361"))
 print(widget.mask_account_card("Maestro 1596837868705199"))
 print(widget.mask_account_card("Счет 64686473678894779589"))
 print(widget.mask_account_card("MasterCard 7158300734726758"))
 print(widget.mask_account_card("Счет 35383033474447895560"))
 print(widget.mask_account_card("Visa Classic 6831982476737658"))
 print(widget.mask_account_card("Visa Platinum 8990922113665229"))
 print(widget.mask_account_card("Visa Gold 5999414228426353"))
 print(widget.mask_account_card("Счет 73654108430135874305"))
 ```
 #### Пример работы:
 ```
 Счет **4305
 Maestro 7000 79** **** 6361
 Visa Platinum 7000 79** **** 6361
 Maestro 1596 83** **** 5199
 Счет **9589
 MasterCard 7158 30** **** 6758
 Счет **5560
 Visa Classic 6831 98** **** 7658
 Visa Platinum 8990 92** **** 5229
 Visa Gold 5999 41** **** 6353
 Счет **4305
 ```

 ### Функция **get_date**(use_iso_date: str) -> str
 Функция принимает строку в формате 2024-03-11T02:26:18.671407
 и возвращает строку с датой в формате ДД.ММ.ГГГГ (11.03.2024)

 #### Пример использования: 
 ```
 from datetime import datetime
 
 from src import widget
 
 print(widget.get_date("2024-03-11T02:26:18.671407"))
 print(widget.get_date(str(datetime.now())))
 ```
 #### Пример работы:
 ```
 11.03.2024
 02.07.2025
 ```

 ### Функция **filter_by_state**(operation_list: list[dict], state: str = "EXECUTED") -> list[dict]
 Функция принимает список словарей
 и опционально значение для ключа state (по умолчанию 'EXECUTED').
 Функция возвращает новый список словарей, содержащий только те словари,
 у которых ключ state соответствует указанному значению

 #### Пример использования: 
 ```
 from src import processing
 
 operation_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
 ]
 print(processing.filter_by_state(operation_list, "EXECUTED"))
 print(processing.filter_by_state(operation_list, "CANCELED"))
 print(processing.filter_by_state(operation_list))
 print(processing.filter_by_state(operation_list, "test"))
 print(processing.filter_by_state(operation_list, "executed"))
 ```
 #### Пример работы:
 ```
 [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
 
 [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
 
 [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
 
 []
 
 [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
 ```

 ### Функция **sort_by_date**(operation_list: list[dict], is_reverse_sort: bool = True) -> list[dict]
 Функция принимает список словарей - банковские операции
 и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
 Функция возвращает новый список, отсортированный по дате (date).

 #### Пример использования: 
 ```
 from src import processing
 
 operation_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
 ]
 print(processing.sort_by_date(operation_list, True))
 print(processing.sort_by_date(operation_list, False))
 print(processing.sort_by_date(operation_list))
 ```
 #### Пример работы:
 ```
 [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
  
 [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
  
 [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
 ```


### Функция **filter_by_currency**(transaction_list, currency = "RUB") -> Generator[dict[str, Any]]:
 Функция принимает список словарей с транзакциями
 и возвращает итератор словарей, который поочередно выдает транзакции,
 где валюта операции соответствует заданной (например, USD)

 #### Пример использования: 
 ```
 from src import generators
 
 transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]
 usd_transactions = generators.filter_by_currency(transactions, "USD")
 for _ in range(2):
     print(next(usd_transactions))

 rub_transactions = generators.filter_by_currency(transactions, "RUB")
 print(list(rub_transactions))
 ```
 #### Пример работы:
 ```
 {'id': 939719570, 
  'state': 'EXECUTED', 
  'date': '2018-06-30T02:08:58.425572', 
  'operationAmount': {'amount': '9824.07', 
                      'currency': {'name': 'USD', 'code': 'USD'}}, 
  'description': 'Перевод организации', 
  'from': 'Счет 75106830613657916952', 
  'to': 'Счет 11776614605963066702'}
  
 {'id': 142264268, 
  'state': 'EXECUTED', 
  'date': '2019-04-04T23:20:05.206878', 
  'operationAmount': {'amount': '79114.93', 
                      'currency': {'name': 'USD', 'code': 'USD'}}, 
  'description': 'Перевод со счета на счет', 
  'from': 'Счет 19708645243227258542', 
  'to': 'Счет 75651667383060284188'}
  
  
 [
   {'id': 873106923, 
   'state': 'EXECUTED', 
   'date': '2019-03-23T01:09:46.296404', 
   'operationAmount': {'amount': '43318.34', 
                       'currency': {'name': 'руб.', 'code': 'RUB'}}, 
   'description': 'Перевод со счета на счет', 
   'from': 'Счет 44812258784861134719', 
   'to': 'Счет 74489636417521191160'}
 ]
 ```


### Функция **transaction_descriptions**(transaction_list: list[dict[str, Any]]) -> Generator[str]:
 Функция принимает список словарей с транзакциями
 и генерирует описание каждой операции по очереди

 #### Пример использования: 
 ```
 from src import generators
 
 transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]
 descriptions = generators.transaction_descriptions(transactions)
 for _ in range(3):
     print(next(descriptions))
 ```
 #### Пример работы:
 ```
 Перевод организации
 Перевод со счета на счет
 Перевод со счета на счет
 ```


### Функция **card_number_generator**(start: int, stop: int) -> list[str]:
 Функция принимает начальное и конечное значения для генерации
 и возвращает номера банковских карт в формате XXXX XXXX XXXX XXXX,
 где X — цифра номера карты.
 Генератор может сгенерировать номера карт в заданном диапазоне
 от 0000 0000 0000 0001 до 9999 9999 9999 9999.

 #### Пример использования: 
 ```
 from src import generators
 
 for card_number in generators.card_number_generator(1, 5):
    print(card_number)
 ```
 #### Пример работы:
 ```
 0000 00000 0000 0001
 0000 00000 0000 0002
 0000 00000 0000 0003
 0000 00000 0000 0004
 0000 00000 0000 0005
 ```


### Функция **conversion_currency**(amount: float, currency_from: str, currency_to: str) -> float:
 Функция конвертации суммы из одной валюты в другую

 #### Пример использования: 
 ```
 from src import external_api
 
 print(external_api.conversion_currency(100, "USD", "RUB"))
 ```
 #### Пример работы:
 ```
 8100.0
 ```
 
 
 ### Функция **get_transactions_of_json_file**(json_file: str) -> list[dict[str, Any]]:
 Функция принимает на вход путь до JSON-файла
 и возвращает список словарей с данными о финансовых транзакциях

 #### Пример использования: 
 ```
 from src import utils
  
 print(utils.get_transactions_of_json_file("operations.json"))
 ```
 #### Пример работы:
 ```
[
	{
		"id": 441945886,
		"state": "EXECUTED",
		"date": "2019-08-26T10:50:58.294041",
		"operationAmount": {
			"amount": "31957.58",
			"currency": {
				"name": "руб.",
				"code": "RUB"		
			}
		},
		"desctiption": "Перевод организации",
		"from": "Maestro 1569837868705199",
		"to": "Счет 64686473678894779589"
	},
	{
		"id": 41428829,
		"state": "EXECUTED",
		"date": "2019-07-03T18:35:29.512364",
		"operationAmount": {
			"amount": "8221.37",
			"currency": {
				"name": "USD",
				"code": "USD"		
			}
		},
		"desctiption": "Перевод организации",
		"from": "MasterCard 7158300734726758",
		"to": "Счет 35383033474447895560"
	},
	{
		"id": 939719570,
		"state": "EXECUTED",
		"date": "2018-06-30T02:08:58.425572",
		"operationAmount": {
			"amount": "9824.07",
			"currency": {
				"name": "USD",
				"code": "USD"		
			}
		},
		"desctiption": "Перевод организации",
		"from": "Счет 75106830613657916952",
		"to": "Счет 1177661460593066702"
	},
	{
		"id": 587085106,
		"state": "EXECUTED",
		"date": "2018-03-23T10:45:06.972075",
		"operationAmount": {
			"amount": "48223,05",
			"currency": {
				"name": "руб.",
				"code": "RUB"		
			}
		},
		"desctiption": "Открытие вклада",
		"to": "Счет 41421565395219882431"
	}
]
 ```


### Функция **get_amount_transaction**(transaction: dict[str, Any]) -> float:
 Функция принимает словрь с транзакцией и возвращает сумму транзакции в рублях

 #### Пример использования: 
 ```
 from src import utils
 
 transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "desctiption": "Перевод организации",
        "from": "Maestro 1569837868705199",
        "to": "Счет 64686473678894779589",
    }

 print(utils.get_amount_transaction(transaction))
 ```
 #### Пример работы:
 ```
 31957.58
 ```
 
 #### Пример использования: 
 ```
 from src import utils
 
 transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
        "desctiption": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }

 print(utils.get_amount_transaction(transaction))
 ```
 #### Пример работы:
 ```
 8100.0
 ```


### Функция **get_operations_csv**(csv_file: str) -> list[dict[str, Any]]:
 Функция для считывания финансовых операций из CSV
 принимает путь к файлу CSV в качестве аргумента
 возвращает список словарей с транзакциями

 #### Пример использования: 
 ```
 from src import extractors

 if __name__ == "__main__":
    result = get_operations_csv("transactions.csv")
    print(result)
 ```
 #### Пример работы:
 ```
 [
	{
		'id': 2177828.0, 
		'state': 'EXECUTED', 
		'date': '2022-04-14T15:14:21Z', 
		'amount': 24853.0, 
		'currency_name': 
		'Yuan Renminbi', 
		'currency_code': 'CNY', 
		'from': 'Счет 38577962752140632721', 
		'to': 'Счет 47657753885349826314', 
		'description': 'Перевод со счета на счет'}, 
	{
		'id': 4137938.0, 
		'state': 'EXECUTED', 
		'date': '2023-01-04T13:13:34Z', 
		'amount': 15560.0, 
		'currency_name': 'Real', 
		'currency_code': 'BRL', 
		'from': nan, 
		'to': 'Счет 38164279390569873521', 
		'description': 'Открытие вклада'
	}
]
 ```
 
 
### Функция **get_operations_xlsx**(xlsx_file: str) -> list[dict[Any, Any]]:
 Функция для считывания финансовых операций из XLSX
 принимает путь к файлу CSV в качестве аргумента
 возвращает список словарей с транзакциями

 #### Пример использования: 
 ```
 from src import extractors

 if __name__ == "__main__":
    result = get_operations_xlsx("transactions_excel.xlsx")
    print(result)
 ```
 #### Пример работы:
 ```
 [
	{
		'id': 2177828.0, 
		'state': 'EXECUTED', 
		'date': '2022-04-14T15:14:21Z', 
		'amount': 24853.0, 
		'currency_name': 
		'Yuan Renminbi', 
		'currency_code': 'CNY', 
		'from': 'Счет 38577962752140632721', 
		'to': 'Счет 47657753885349826314', 
		'description': 'Перевод со счета на счет'}, 
	{
		'id': 4137938.0, 
		'state': 'EXECUTED', 
		'date': '2023-01-04T13:13:34Z', 
		'amount': 15560.0, 
		'currency_name': 'Real', 
		'currency_code': 'BRL', 
		'from': nan, 
		'to': 'Счет 38164279390569873521', 
		'description': 'Открытие вклада'
	}
]
 ```
 
### Функция **process_bank_search**(data: list[dict], search: str = "") -> list[dict]:
 Функция принимает список словарей с данными о банковских операциях и строку поиска,
 и возвращает список словарей, у которых в описании есть данная строка.

 #### Пример использования: 
 ```
 from src import processing
 
 transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
]

 if __name__ == "__main__":
    result = processing.process_bank_search(transactions, "на счет")
    print(result)
 ```
 #### Пример работы:
 ```
 [
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
]
 ```
 
 
 ### Функция **process_bank_operations**(data: list[dict], categories: list) -> dict:
 Функция принимает список словарей с данными о банковских операциях и список категорий операций
 и возвращает словарь, в котором ключи — это названия категорий,
 а значения — это количество операций в каждой категории

 #### Пример использования: 
 ```
 from src import processing
 
 transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
		'id': 4137938.0, 
		'state': 'EXECUTED', 
		'date': '2023-01-04T13:13:34Z', 
		'amount': 15560.0, 
		'currency_name': 'Real', 
		'currency_code': 'BRL', 
		'from': nan, 
		'to': 'Счет 38164279390569873521', 
		'description': 'Открытие вклада'
	},
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
]

 if __name__ == "__main__":
    result = processing.process_bank_search(transactions, ["Перевод организации", "Перевод со счета на счет"])
    print(result)
 ```
 #### Пример работы:
 ```
{"перевод организации": 1, "перевод со счета на счет": 2}
 ```


 ## Декораторы:
 ### Декоратор **log**(filename: str | None = None) -> Any
  Декоратор, который может логировать работу функции
  и ее результат как в файл, так и в консоль

 #### Пример использования (запись в консоль): 
```
 import decorators

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
 ```
 #### Пример работы (запись в консоль):
 ```
 
2025-08-03 15:41:48:
Function add_numbers called with args: (3, 5) and kwargs: {}.
Execution time: 0:00:00.0033. Result: 8

 ```
 #### Пример использования (запись в файл): 
```
import decorators

file_of_names = "my_log.txt"

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
 
result = add_numbers(3, 5)
 ```
 #### Пример работы (запись в файл):
 ```

2025-08-03 15:53:58:
Function add_numbers called with args: (3, 5) and kwargs: {}.
Execution time: 0:00:00.0010. Result: 8

 ```

 ## Тестирование:
Проект покрыт тестами фреймворка pytest. Для их запуска выполните команду:
```
pytest
```
Для выгрузки отчета о покрытии проекта тестами выполните команду:
```
pytest --cov=src --cov-report=html
```

 ## Логирование:
Работа проекта логируется.
Логи соханяются в папку logs и презаписываются при каждом запуске приложения.

 ## Документация:

 ## Лицензия:
 Проект распространяется под [лицензией MIT](LICENSE).
 