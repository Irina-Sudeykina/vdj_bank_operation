from src import masks, widget

if __name__ == "__main__":
    print(masks.get_mask_card_number(1234123412341234))
    print(masks.get_mask_account(12345678900987654321))

    print(widget.mask_account_card("Счет 73654108430135874305"))
    print(widget.mask_account_card("Maestro 7000792289606361"))
    print(widget.mask_account_card("Visa Platinum 7000792289606361"))
