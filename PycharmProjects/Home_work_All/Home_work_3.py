# Дан текст (любой, можете использовать - lorem ipsum). Посчитать количество слов и предложений в тексте.

data_text = "Возможно, сайт временно недоступен или перегружен запросами. Подождите некоторое время и попробуйте снова. "\
            "Если вы не можете загрузить ни одну страницу и проверьте настройки соединения с Интернетом. " \
            "Если ваш компьютер или сеть защищены межсетевым экраном или прокси-сервером и убедитесь, что Firefox " \
            "разрешён выход в Интернет."
sentence = data_text.replace("!", ".").replace("?", ".").split(". ")
words = data_text.replace("-", " ").replace(". ", " ").replace(", ", " ").replace("  ", " ").replace("   ", " ").split(" ")
print(f"Количество предложений в тексте равно: {len(sentence)}\n"
      f"Количество слов в тексте равно: {len(words)}")

# проверка решения
for i in enumerate(sentence, 1):
    print(i)
for i in enumerate(words, 1):
    print(i)

# Пользователь вводит число, если оно четное вывесть - “Even” если нет - “Odd”.

number = input("Введите число: ")
cnt_number = number.split(".")
if len(cnt_number) < 2:
    if number.isdigit():
        if int(number) % 2 == 0:
            print("Event")
        else:
            print("Odd")
    else:
        print("Введена строка")
else:
    print("Вы ввели вещественное число")

# Пользователь вводит значения через запятую, если количество значений меньше 10, отсортировать их от большего
# к меньшему, если больше то от меньшего к большему.

input_values = input("Введите значения через запятую: ")
input_values_clear = input_values.replace(".", ",").replace(" ", ",").replace("/", ",")
pars_values = input_values.split(",")
list_pars_values = [int(i) for i in pars_values if i.isdigit()]
if len(list_pars_values) != 0:
    if len(list_pars_values) < 10:
        print(sorted(list_pars_values))
    else:
        print(sorted(list_pars_values, reverse=True))
else:
    print("Вы ввели буквы вместо цифр")

# Пользователь вводит 2 числа, если первое больше второго,
# вывести их разность, если второе больше первого вывести их сумму, если числа равны, возвести первое в степень второго.

number_first = input("Введите первое число: ")
number_second = input("Введите второе число: ")
number_first_values = number_first.split(".")
number_second_values = number_second.split(".")
if len(number_first_values) < 2:
    if len(number_second_values) < 2:
        if number_first.isdigit() and number_second.isdigit():
            number_first = int(number_first)
            number_second = int(number_second)
            if number_first > number_second:
                print(number_first - number_second)
            elif number_second > number_first:
                print(number_first + number_second)
            else:
                print(number_first ** number_second)
        else:
            print("Введена строка")
    elif len(number_second_values) == 2:
        if number_first.isdigit() and number_second_values[0].isdigit() and number_second_values[1].isdigit():
            number_first = float(number_first)
            number_second = float(number_second)
            if number_first > number_second:
                print(number_first - number_second)
            elif number_second > number_first:
                print(number_first + number_second)
            else:
                print(number_first ** number_second)
elif len(number_first_values) == 2:
    if len(number_second_values) < 2:
        if number_first_values[0].isdigit() and number_first_values[1].isdigit() and number_second.isdigit():
            number_first = float(number_first)
            number_second = float(number_second)
            if number_first > number_second:
                print(number_first - number_second)
            elif number_second > number_first:
                print(number_first + number_second)
            else:
                print(number_first ** number_second)
        else:
            print("Введена строка")
    elif len(number_second_values) == 2:
        if number_first_values[0].isdigit() and number_first_values[1].isdigit() and number_second_values[0].isdigit() and number_second_values[1].isdigit():
            number_first = float(number_first)
            number_second = float(number_second)
            if number_first > number_second:
                print(number_first - number_second)
            elif number_second > number_first:
                print(number_first + number_second)
            else:
                print(number_first ** number_second)
        else:
            print("Введена строка")
else:
    print("Вы ввели строку")


# Пользователь вводит 3 числа, подставить и посчитать формулу: 2a - 8b / (a-b+c). Вывести результат.

number_first = input("Введите a: ")
number_second = input("Введите b: ")
number_three = input("Введите c: ")
point_number_first = number_first.find(".")
point_number_second = number_second.find(".")
point_number_three = number_three.find(".")
if point_number_first == -1 and point_number_second == -1 and point_number_three == -1:
    if number_first.isdigit() and number_second.isdigit() and number_three.isdigit():
        number_first = int(number_first)
        number_second = int(number_second)
        number_three = int(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first != -1 and point_number_second == -1 and point_number_three == -1:
    split_number_first = number_first.split(".")
    if split_number_first[0].isdigit() and split_number_first[1].isdigit() and number_second.isdigit() and number_three.isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first == -1 and point_number_second != -1 and point_number_three == -1:
    split_number_second = number_second.split(".")
    if split_number_second[0].isdigit() and split_number_second[1].isdigit() and number_first.isdigit() and number_three.isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first == -1 and point_number_second == -1 and point_number_three != -1:
    split_number_three = number_three.split(".")
    if split_number_three[0].isdigit() and split_number_three[1].isdigit() and number_first.isdigit() and number_second.isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first != -1 and point_number_second != -1 and point_number_three == -1:
    split_number_first = number_first.split(".")
    split_number_second = number_second.split(".")
    if split_number_first[0].isdigit() and split_number_first[1].isdigit() and split_number_second[0].isdigit() \
                                       and split_number_second[1].isdigit() and number_three.isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first != -1 and point_number_second == -1 and point_number_three != -1:
    split_number_first = number_first.split(".")
    split_number_three = number_three.split(".")
    if split_number_first[0].isdigit() and split_number_first[1].isdigit() and split_number_three[0].isdigit() \
                                       and split_number_three[1].isdigit() and number_second.isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first == -1 and point_number_second != -1 and point_number_three != -1:
    split_number_second = number_second.split(".")
    split_number_three = number_three.split(".")
    if split_number_second[0].isdigit() and split_number_second[1].isdigit() and split_number_three[0].isdigit() \
                                        and split_number_three[1].isdigit() and number_first.isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first != -1 and point_number_second != -1 and point_number_three != -1:
    split_number_first = number_first.split(".")
    split_number_second = number_second.split(".")
    split_number_three = number_three.split(".")
    if split_number_first[0].isdigit() and split_number_first[1].isdigit() and split_number_second[0].isdigit() \
                                       and split_number_second[1].isdigit() and split_number_three[0].isdigit() and split_number_three[1].isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
else:
    print("Введена строка")

# Дан список из целых чисел длиной N подсчитать количество четных чисел в списке

spisok_numbers = [5, 7, 8, 9, 2, 3, 6, 56, 34, 28, 86]
count_number = 0
for i in spisok_numbers:
    if i % 2 == 0:
        count_number += 1
print(count_number)

# Дан список целых чисел длиной N отсортировать список, не используя метода sort или sorted.
# (Пожалуйста не гуглите решение, постарайтесь сделать сами)

ind = 0
spisok_numbers = [7, 2, 3, 7, 6, 5, 4, 3, 13, 2]
work_spisok = []
while ind <= len(spisok_numbers) - 1:
    work_spisok = spisok_numbers[ind:len(spisok_numbers)]
    min_element = min(work_spisok)
    ind_min_element = work_spisok.index(min_element)
    work_spisok[0], work_spisok[ind_min_element] = work_spisok[ind_min_element], work_spisok[0]
    spisok_numbers[ind:len(spisok_numbers)] = work_spisok
    ind += 1
else:
    print(spisok_numbers)

# Рассчитать последовательность фибоначчи, длину ряда задает пользователь.

f0_element = 0
f1_element = 1
cnt_element = input("Какое количество элементов вывести на экран? ")
list_fibonachchi = [f0_element, f1_element]
ind = 1
while ind < int(cnt_element) - 1:
    fn_element = f0_element + f1_element
    list_fibonachchi.append(fn_element)
    f0_element, f1_element = f1_element, fn_element
    ind += 1
else:
    print(list_fibonachchi)

# Пользователь вводит целое число, определить простое ли оно.

number = input("Введите число: ")
float_number = number.split(".")
if len(float_number) == 2:
    if float_number[0].isdigit() and float_number[1].isdigit():
        print("Простыми числами могут быть только целые числа")
    else:
        print("Введена строка")
elif len(float_number) == 1:
    if number.isdigit():
        number = int(number)
        sqrt_number = int(number ** (1/2))
        cnt = 0
        for i in range(2, sqrt_number + 1):
            if (number % i) == 0:
                cnt += 1
        if cnt > 0:
            print("Составное число")
        else:
            print("Простое число")
    else:
        print("Введена строка")
else:
    print("Введена строка")



