import os

from src import masks
from src import use_file_names

if __name__ == "__main__":
    print(masks.get_mask_card_number(1234123412341234))
    print(masks.get_mask_account(12345678900987654321))

    file_of_names = os.path.join(os.getcwd(), "data\\names.txt")
    print(file_of_names)
    print(use_file_names.get_names_list(file_of_names))
