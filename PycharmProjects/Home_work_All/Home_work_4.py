# Написать программу перевода числа из арабских цифр в число из римских цифр.
# Написать программу обратного перевода.

DICT_NUMBERS = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
LIST_FOR_ONLY_MINUS = [4, 9, 40, 90, 400, 900]

def convert_arabian_to_rim(numb):
    list_arabian_number = []
    list_rimean_number = []
    len_numb = len(numb)
    numb = int(numb)
    cnt_numbers = 0
    while cnt_numbers < len_numb:
        divider = int('1'.ljust((len_numb - cnt_numbers), '0'))
        remainder_division = numb % divider
        decomposed_number = numb / divider
        if remainder_division != 0:
            numb = remainder_division
            list_arabian_number.append(int(decomposed_number) * divider)
            cnt_numbers += 1
        else:
            list_arabian_number.append(int(decomposed_number) * divider)
            cnt_numbers = len_numb
    list_rimean_key = [DICT_NUMBERS[i] for i in DICT_NUMBERS]
    for i in list_arabian_number:
        list_required_values = [[k, v] for k, v in DICT_NUMBERS.items() if len(str(k)) == len(str(i))]
        if i not in list_rimean_key and i not in LIST_FOR_ONLY_MINUS:
            sum_elements = 0
            remain_result = ''
            while sum_elements < i:
                remain_result += list_required_values[0][1]
                sum_elements += list_required_values[0][0]
                count = len(remain_result)
            if count > 3:
                sum_elements = list_required_values[1][0]
                remain_result = list_required_values[1][1]
                while sum_elements < i:
                    remain_result += list_required_values[0][1]
                    sum_elements += list_required_values[0][0]
                list_rimean_number.append(remain_result)
            else:
                list_rimean_number.append(remain_result)
        elif i in list_rimean_key:
            list_rimean_number.append(i)
        elif i in LIST_FOR_ONLY_MINUS:
            list_rimean_number.append(list_required_values[0][1] + list_required_values[1][1])
        result = "".join(str(i) for i in list_rimean_number)
    return result

def convert_rim_to_arabian(numb):
    work_list = [k for i in numb for k, v in DICT_NUMBERS.items() if v == i]
    result = 0
    for j in range(0, len(work_list) - 1):
        if work_list[j] >= work_list[j + 1]:
            result += work_list[j]
        else:
            result -= work_list[j]
    result += work_list[-1]
    return result

number_person = input("Введите римское или арабское число для конвертации: ")
if number_person.isdigit():
    if int(number_person) > 3999:
        print("С помощью римских цифр можно записать любое целое число, но не более 3999(MMMCMXCIX)")
    else:
        print(f"Конвертация арабского числа в римское: {convert_arabian_to_rim(number_person)}")
elif number_person.isalpha() and number_person.isupper():
    len_number_person = len(number_person)
    list_for_check_rimean_numbers = list(number_person)
    list_rimean_values = [i for i in DICT_NUMBERS.values()]
    cnt_numbers = 0
    for i in list_for_check_rimean_numbers:
    # Все ли введенные символы являются римскими цифрами
        if i in list_rimean_values:
            cnt_numbers += 1
    # Если все введенные символы являются римскими цифрами, то
    if len_number_person == cnt_numbers:
        print(f"Конвертация римского числа в арабское: {convert_rim_to_arabian(list_for_check_rimean_numbers)}")
else:
    print("This is a string")

# Написать функцию no_numbers которая удаляет из файла все цифры. Функция должна принимать путь к файлу.

def read_from_file(name_file):
    text_without_number = ''
    with open(name_file, 'r', encoding="utf-8") as some_file:
        list_string = some_file.readlines()
    for i in list_string:
        i = i.replace("\n", "")
        for j in i:
            if j.isalpha():
                text_without_number += j
        text_without_number += "\n"
        write_file(name_file, text_without_number)
    return text_without_number

def write_file(name_file, text_for_file):
    with open(name_file, 'w+', encoding="utf-8") as some_file:
        some_file.writelines(text_for_file)

file_for_read = "./pictures.txt"
try:
    lst_pictures = read_from_file(file_for_read)
except FileNotFoundError:
    print("Фаил отсутствует в директории.")
    fl = open(file_for_read, 'w', encoding="utf-8")
    fl.close()
    print("Фаил успешно создан.")

# Написать функцию реализующую шифрование Цезаря. Функция принимает 2 параметра, текст и сдвиг,
# возвращает зашифрованный текст.

import string

LETTERS = string.ascii_letters

def cezar_shifr(text, shift):
    result = ''
    for i in text:
        if i.isalpha():
            result += LETTERS[(LETTERS.find(i) + int(shift)) % len(LETTERS)]
        elif i.isdigit():
            ind_dig = int(i) + int(shift)
            if ind_dig > 9:
                ind_dig = int(ind_dig) - 9
                result += str(ind_dig)
            else:
                result += str(ind_dig)
    return result

txt_for_shifr = input("Необходимо ввести текст для шифрования: ")
shift_letters = input("Необходимо ввести сдвиг для текста или цифр: ")
mistake_text = ''
mistake_shift = ''
if not shift_letters.isdigit():
    mistake_shift = "Некорректный сдвиг."
for i in txt_for_shifr:
    if (i.isalpha() and i in list(LETTERS)) or i.isdigit():
        continue
    else:
        mistake_text = "Ошибка ввода."
        break
if mistake_shift == '' or mistake_text == '':
    print(cezar_shifr(txt_for_shifr, shift_letters))
else:
    print(f"Ошибки программы {mistake_text} {mistake_shift}")

# Написать функцию реализующую дешифровку Цезаря.

def cezar_deshifr(text, shift):
    result = ''
    for i in text:
        if i.isalpha():
            result += LETTERS[(LETTERS.find(i) - int(shift)) % len(LETTERS)]
        elif i.isdigit():
            ind_dig = int(i) - int(shift)
            if ind_dig < 1:
                ind_dig = int(ind_dig) + 9
                result += str(ind_dig)
            else:
                result += str(ind_dig)
    return result

# Зашифровать данные в файле шифрованием Цезаря и записать в новый файл.

def read_from_file(name_file):
    text_without_number = ''
    with open(name_file, 'r', encoding="utf-8") as some_file:
        list_string = some_file.readlines()
    for i in list_string:
        i = i.replace("\n", "")
        for j in i:
            print(j)
            if j.isalpha():
                text_without_number += j
        text_without_number += "\n"
        write_file(name_file, text_without_number)
    return text_without_number

# Зашифровать данные в файле шифрованием Цезаря и записать в новый файл.

import string

LETTERS = string.ascii_letters

def write_file(name_file, text_for_file):
    with open(name_file, 'w+', encoding="utf-8") as some_file:
        some_file.writelines(text_for_file)

def cezar_shifr(text, shift, name_file):
    result = ''
    for i in text:
        if i.isalpha():
            result += LETTERS[(LETTERS.find(i) + int(shift)) % len(LETTERS)]
        elif i.isdigit():
            ind_dig = int(i) + int(shift)
            if ind_dig > 9:
                ind_dig = int(ind_dig) - 9
                result += str(ind_dig)
            else:
                result += str(ind_dig)
    result += "\n"
    write_file(name_file, result)

def read_from_file(name_file, shift, name_file_write):
    text_from_file = ''
    with open(name_file, 'r', encoding="utf-8") as some_file:
        list_string = some_file.readlines()
    for i in list_string:
        i = i.replace("\n", "")
        text_from_file += i
        cezar_shifr(text_from_file, shift, name_file_write)

shift_letters = input("Необходимо ввести сдвиг для текста или цифр: ")
if not shift_letters.isdigit():
    print("Некорректный сдвиг.")
else:
    file_for_read = "./text_file.txt"
    file_for_write = "./text_shifr.txt"
    try:
        lst_pictures = read_from_file(file_for_read, shift_letters, file_for_write)
    except FileNotFoundError:
        print("Фаил отсутствует в директории.")
        fl = open(file_for_read, 'w', encoding="utf-8")
        fl.close()
        print("Фаил успешно создан.")