from datetime import date, datetime
from typing import Any

import pytest


@pytest.fixture
def cleaned_name_list() -> list[str]:
    """
    Фикстура со списком имен
    :return: список имен
    """
    return [
        "Иван",
        "Джон",
        "Анна",
        "Мэри",
        "Сергей",
        "Emily",
        "Kate",
        "Peter",
        "Michael",
        "Николай",
        "Alice",
        "Sophia",
        "Борис",
        "David",
        "Elizabeth",
        "Кристина",
        "Джеймс",
        "Мария",
        "Анастасия",
        "Thomas",
        "Alexandra",
        "Алексей",
        "Robert",
        "Olivia",
        "Ольга",
        "Daniel",
        "Emma",
        "Татьяна",
        "Richard",
        "William",
        "Светлана",
        "John",
        "Jessica",
        "Максим",
        "Catherine",
        "Томас",
        "Lily",
        "Марина",
        "Christopher",
        "Marie",
        "Владимир",
        "Benjamin",
        "Hannah",
        "Наталья",
        "София",
        "Александр",
        "Jacob",
        "Олег",
        "Андрей",
        "Артем",
        "Mia",
        "Илья",
        "Noah",
        "Елена",
        "Александра",
        "Алиса",
        "Алена",
        "Альберт",
        "Инга",
        "Маргарита",
        "Карина",
        "Елена",
        "Артур",
        "Софья",
        "Матвей",
        "Максим",
        "Андреа",
        "Елизавета",
        "Сергей",
        "Дмитрий",
        "Любовь",
        "Михаил",
        "Екатерина",
        "Виктория",
        "Евгения",
        "Анастасия",
        "Евгений",
        "Anthony",
        "Джон",
        "Антон",
        "Лариса",
        "Владислав",
        "Арсений",
        "Мирослава",
        "Тимофей",
        "Маргарита",
        "Лилия",
        "Софи",
        "Тимур",
        "Алёна",
        "Elena",
        "Марина",
        "Юлия",
        "Зинаида",
        "Юрий",
        "Patrick",
        "Сабина",
        "Анжелика",
        "София",
        "Ирина",
        "Даниил",
        "Адам",
        "Алина",
        "Анастасия",
        "Виктор",
    ]


@pytest.fixture
def eng_name_list() -> list[str]:
    """
    Фикстура со списком имен на английском
    :return: список имен
    """
    return [
        "Emily",
        "Kate",
        "Peter",
        "Michael",
        "Alice",
        "Sophia",
        "David",
        "Elizabeth",
        "Thomas",
        "Alexandra",
        "Robert",
        "Olivia",
        "Daniel",
        "Emma",
        "Richard",
        "William",
        "John",
        "Jessica",
        "Catherine",
        "Lily",
        "Christopher",
        "Marie",
        "Benjamin",
        "Hannah",
        "Jacob",
        "Mia",
        "Noah",
        "Anthony",
        "Elena",
        "Patrick",
    ]


@pytest.fixture
def rus_name_list() -> list[str]:
    """
    Фикстура со списком имен на русском
    :return: список имен
    """
    return [
        "Иван",
        "Джон",
        "Анна",
        "Мэри",
        "Сергей",
        "Николай",
        "Борис",
        "Кристина",
        "Джеймс",
        "Мария",
        "Анастасия",
        "Алексей",
        "Ольга",
        "Татьяна",
        "Светлана",
        "Максим",
        "Томас",
        "Марина",
        "Владимир",
        "Наталья",
        "София",
        "Александр",
        "Олег",
        "Андрей",
        "Артем",
        "Илья",
        "Елена",
        "Александра",
        "Алиса",
        "Алена",
        "Альберт",
        "Инга",
        "Маргарита",
        "Карина",
        "Елена",
        "Артур",
        "Софья",
        "Матвей",
        "Максим",
        "Андреа",
        "Елизавета",
        "Сергей",
        "Дмитрий",
        "Любовь",
        "Михаил",
        "Екатерина",
        "Виктория",
        "Евгения",
        "Анастасия",
        "Евгений",
        "Джон",
        "Антон",
        "Лариса",
        "Владислав",
        "Арсений",
        "Мирослава",
        "Тимофей",
        "Маргарита",
        "Лилия",
        "Софи",
        "Тимур",
        "Алёна",
        "Марина",
        "Юлия",
        "Зинаида",
        "Юрий",
        "Сабина",
        "Анжелика",
        "София",
        "Ирина",
        "Даниил",
        "Адам",
        "Алина",
        "Анастасия",
        "Виктор",
    ]


@pytest.fixture
def eng_data_file() -> str:
    """
    Фикстура содержимого файла с именами на английском
    :return: список имен
    """
    return """Emily
Kate
Peter
Michael
Alice
Sophia
David
Elizabeth
Thomas
Alexandra
Robert
Olivia
Daniel
Emma
Richard
William
John
Jessica
Catherine
Lily
Christopher
Marie
Benjamin
Hannah
Jacob
Mia
Noah
Anthony
Elena
Patrick
"""


@pytest.fixture
def rus_data_file() -> str:
    """
    Фикстура содержимого файла с именами на русском
    :return: список имен
    """
    return """Иван
Джон
Анна
Мэри
Сергей
Николай
Борис
Кристина
Джеймс
Мария
Анастасия
Алексей
Ольга
Татьяна
Светлана
Максим
Томас
Марина
Владимир
Наталья
София
Александр
Олег
Андрей
Артем
Илья
Елена
Александра
Алиса
Алена
Альберт
Инга
Маргарита
Карина
Елена
Артур
Софья
Матвей
Максим
Андреа
Елизавета
Сергей
Дмитрий
Любовь
Михаил
Екатерина
Виктория
Евгения
Анастасия
Евгений
Джон
Антон
Лариса
Владислав
Арсений
Мирослава
Тимофей
Маргарита
Лилия
Софи
Тимур
Алёна
Марина
Юлия
Зинаида
Юрий
Сабина
Анжелика
София
Ирина
Даниил
Адам
Алина
Анастасия
Виктор
"""


@pytest.fixture
def new_date_time() -> str:
    """
    Фикстура текущих даты и временив формате 2024-03-11T02:26:18.671407
    :return: строка в формате 2024-03-11T02:26:18.671407
    """
    return str(datetime.now())


@pytest.fixture
def new_date_str() -> str:
    """
    Фикстура текущей даты в формате ДД.ММ.ГГГГ (11.03.2024)
    :return: строка в формате ДД.ММ.ГГГГ (11.03.2024)
    """
    today = date.today()
    return today.strftime("%d.%m.%Y")


@pytest.fixture
def operation_list_all() -> list[dict[str, Any]]:
    """
    Фикстура с полным списком операций
    :return: список операций
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 675436780, "state": "EXECUTED"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def operation_list_executed() -> list[dict[str, Any]]:
    """
    Фикстура со списком операций с типом EXECUTED
    :return: список операций
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 675436780, "state": "EXECUTED"},
    ]


@pytest.fixture
def operation_list_canceled() -> list[dict[str, Any]]:
    """
    Фикстура со списком операций с типом CANCELED
    :return: список операций
    """
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def operation_list_no_state() -> list[dict[str, Any]]:
    """
    Фикстура со списком операций с отсутствующим состоянимем
    :return: список операций
    """
    return [
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def operation_list_sort_asc() -> list[dict[str, Any]]:
    """
    фикстура со списком операций отсортированных в порядке возрастания
    :return: список операций
    """
    return [
        {"id": 675436780, "state": "EXECUTED"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def operation_list_sort_desc() -> list[dict[str, Any]]:
    """
    фикстура со списком операций отсортированных в порядке убывания
    :return: список операций
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 675436780, "state": "EXECUTED"},
    ]


@pytest.fixture
def operation_list_no_date() -> list[dict[str, Any]]:
    """
    Фикстура со списком операций с отсутствующей датой
    :return: список операций
    """
    return [
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 594226727, "state": "CANCELED"},
    ]


@pytest.fixture
def transactions_all() -> list[dict[str, Any]]:
    """
    Фикстура с полным списком транзакций
    :return: список транзакций
    """
    return [
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
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def usd_transaction_one() -> dict[str, Any]:
    """
    Фикстура с первой транзакцией в валюте USD
    :return: список транзакций
    """
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


@pytest.fixture
def usd_transaction_two() -> dict[str, Any]:
    """
    Фикстура с полным списком транзакций
    :return: список транзакций
    """
    return {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
