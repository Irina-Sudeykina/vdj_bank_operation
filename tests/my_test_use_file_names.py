import os
from pathlib import Path

from src import use_file_names

# Задаём корневой путь проекта.
root_path = Path(__file__).resolve().parents[1]
print(root_path)

file_of_names = os.path.join(root_path, "data\\names.txt")
print(file_of_names)

clean_list_names = use_file_names.get_names_list_02(file_of_names)
print(clean_list_names)

eng_names_list = use_file_names.get_list_of_lang_names(clean_list_names, "eng")
rus_names_list = use_file_names.get_list_of_lang_names(clean_list_names)
print(eng_names_list)
print(rus_names_list)

file_of_eng_names = os.path.join(root_path, "data\\eng_names.txt")
file_of_rus_names = os.path.join(root_path, "data\\rus_names.txt")
use_file_names.set_list_to_file(eng_names_list, file_of_eng_names)
use_file_names.set_list_to_file(rus_names_list, file_of_rus_names)
