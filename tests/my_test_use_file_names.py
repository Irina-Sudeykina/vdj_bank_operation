import os
from pathlib import Path

from src import use_file_names

# Задаём корневой путь проекта.
root_path = Path(__file__).resolve().parents[1]
print(root_path)

file_of_names = os.path.join(root_path, "data\\names.txt")
print(file_of_names)
print(use_file_names.get_names_list(file_of_names))

print(use_file_names.get_list_of_lang_names(file_of_names, "eng"))
print(use_file_names.get_list_of_lang_names(file_of_names))
