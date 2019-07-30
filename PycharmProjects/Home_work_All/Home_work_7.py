from Read_Write_File import read_file as rf
from Read_Write_File import add_file as wf
from Read_Write_File import error_file
from Regular_pattern import pattern_dates as pd
from Regular_pattern import pattern_years as py
from Regular_pattern import pattern_numbers as pn
from Regular_pattern import pattern_negative_numbers as pngn
from Regular_pattern import pattern_proper_names as ppn
from calendar import monthrange
import math


# Дан файл с текстом, создать список из дат в тексте - даты в формате DD-MM-YYYY (02-03-1999)

name_file_read = "./data.txt"
try:
    text = rf(name_file_read)
except FileNotFoundError:
    error_file(name_file_read)
else:
    list_dates = [pd(i) for i in text]
    clear_list_dates = [j for i in list_dates for j in i if j]
    print(clear_list_dates)

# Пользователь вводит год в формате - YYYY (1999) Определить, является ли год високосным.

MONTH = 2
year = input("Введите год в формате YYYY (1999): ")
input_validation = py(year)
if input_validation:
    year_definition = monthrange(int(input_validation[0]), MONTH)
    if year_definition[1] == 28:
        print("Не високосный год")
    else:
        print("Високосный год")
else:
    print("Некорректный формат даты")

# Дан файл вывести сумму всех чисел в файле. Цифры могут быть не целыми и отрицательными

name_file_read_numbers = "./numbers.txt"
try:
    list_numbers = rf(name_file_read_numbers)
except FileNotFoundError:
    error_file(name_file_read_numbers)
else:
    numb = [pn(i) for i in list_numbers]
    clear_list_numbers = [float(j.lstrip('.')) for i in numb for j in i if j]
    print(sum(clear_list_numbers))

# Написать генератор геометрической прогрессии.


def create_geomet_generator(b0, q, n):
    for n in range(1, n + 1):
        yield b0 * math.pow(q, n - 1)

# Проверка работы генератора


first_term_gprogres = int(input("Введите первый член геометрической прогрессии b1 = "))
denominator = int(input("Введите знаменатель геометрической прогрессии q = "))
numb_term = int(input("Какое количество членов геометрической прогресии необходимо вывести на экран? n = "))
for i in create_geomet_generator(first_term_gprogres, denominator, numb_term):
    print(i)

# Дан файл с текстом, удалить из файла все отрицательные числа, числа могут быть не целыми.

name_file_read_negative = "./numbers.txt"
name_file_write_without_negative = "./without_negative_numbers.txt"
try:
    list_negative_numbers = rf(name_file_read_negative)
except FileNotFoundError:
    error_file(name_file_read_negative)
else:
    sentence = [i.split(" ") for i in list_negative_numbers]
    for i in sentence:
        new_text = ""
        for j in i:
            if not pngn(j):
                new_text += j + " "
        wf(name_file_write_without_negative, new_text)

# Дан файл с текстом, вывести список который содержит все имена, все фамилии и все географические названия.


def cheekynew(line_text):
    if line_text != 0:
        return "\n"
    return ""


name_file_with_high_letters = "./text_with_high_letters.txt"
dict_proper_names = "./proper_names.txt"
try:
    list_with_high_letters = rf(name_file_with_high_letters)
except FileNotFoundError:
    error_file(name_file_with_high_letters)
else:
    sentences_form_file = [i.split(".") for i in list_with_high_letters]
    list_for_proper_names = [k.split(" ") for j in sentences_form_file for k in j]
    proper_names = [j for i in list_for_proper_names for j in i if ppn(j)]
    print(proper_names)
    try:
        list_dict_proper_names = rf(dict_proper_names)
    except FileNotFoundError:
        error_file(dict_proper_names)
    else:
        clear_list_proper_names = list(map(str.strip, list_dict_proper_names))
        if clear_list_proper_names == []:
            line = 0
        else:
            line = 1
        true_proper_names = [i for i in proper_names if i in clear_list_proper_names]
        false_proper_names = [i for i in proper_names if i not in clear_list_proper_names]
        true_proper_names = list(dict.fromkeys(true_proper_names))
        false_proper_names = list(dict.fromkeys(false_proper_names))
        print(f"Эти имена точно являются именами собственными => {true_proper_names}")
        print(f"Этих имен нет в словаре собственных имен => {false_proper_names}")
        answear = input("Добавить новые имена в словарь? y/n: ")
        while answear != 'n':
            if answear == 'y':
                for i in false_proper_names:
                    answear = input(f"Добавить имя '{i}' в словарь? y/n: ")
                    if answear == 'y':
                        wf(dict_proper_names, cheekynew(line) + i)

