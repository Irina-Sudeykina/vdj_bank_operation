from datetime import datetime

from src import generators, masks, processing, widget

if __name__ == "__main__":
    print(masks.get_mask_card_number(1234123412341234))
    print(masks.get_mask_account(12345678900987654321))

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

    print(widget.get_date("2024-03-11T02:26:18.671407"))
    print(widget.get_date(str(datetime.now())))

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

    print(processing.sort_by_date(operation_list, True))
    print(processing.sort_by_date(operation_list, False))
    print(processing.sort_by_date(operation_list))

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

    descriptions = generators.transaction_descriptions(transactions)
    for _ in range(3):
        print(next(descriptions))

    for card_number in generators.card_number_generator(1, 5):
        print(card_number)

    for card_number in generators.card_number_generator(8, 5):
        print(card_number)

    for card_number in generators.card_number_generator(5, 5):
        print(card_number)
