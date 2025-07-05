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

 ## Тестирование:
Проект покрыт тестами фреймворка pytest. Для их запуска выполните команду:
```
pytest
```

 ## Документация:

 ## Лицензия:
 Проект распространяется под [лицензией MIT](LICENSE).
 