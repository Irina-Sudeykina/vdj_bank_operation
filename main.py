from datetime import datetime

from src import masks, widget

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
