from multiprocessing import Process, Queue
import os
from Read_Write_File import read_file
from Read_Write_File import write_file
from functools import reduce

# 1. Дан список с произвольнвми элементами. Проверить все ли элементы списка не уникальны.
# Первый вариант решения
lst_all = [1, 5, 7, 6, 8, 3]
uniculs = list(filter(lambda x: lst_all.count(x) > 1, lst_all))
if len(uniculs) > 0:
    print("Элементы списка не уникальны")
else:
    print("Элементы списка уникальны")


# 2. Написать функцию которая принимает номер тролейбусного билета и определяет счастливый
# (сумма первых трех цифр == сумма последних трех цифр) или нет, а так же предидущий и следующий счастливые билеты.
# Функция должна валидировать то что номер 6ти значный и если нет кидать исключение - NotValidTicketNumber
class MyError(Exception):
    def __init__(self, text):
        self.txt = text


def prev_happiness_ticket(number_ticket):
    result_prev = number_ticket
    res_ticket = "Не счастливый билет"
    ticket_prev = int(number_ticket)
    while res_ticket != "Счастливый билет":
        ticket_prev -= 1
        res_ticket = happiness_ticket(str(ticket_prev))
    if len(str(ticket_prev)) < 6:
        print("Предыдущего шестизначного счастливого билета нет")
    else:
        result_prev = ticket_prev
    return result_prev


def next_happiness_ticket(number_ticket):
    result_next = number_ticket
    res_ticket = "Не счастливый билет"
    ticket_next = int(number_ticket)
    while res_ticket != "Счастливый билет":
        ticket_next += 1
        res_ticket = happiness_ticket(str(ticket_next))
    if len(str(ticket_next)) > 6:
        print("Следующего шестизначного счастливого билета нет")
    else:
        result_next = ticket_next
    return result_next


def happiness_ticket(number_ticket):
    first_part_number = number_ticket[:3]
    second_part_number = number_ticket[3:]
    sum_first_elements = reduce(lambda x, results: int(x) + int(results), first_part_number)
    sum_second_elements = reduce(lambda x, results: int(x) + int(results), second_part_number)
    if sum_first_elements == sum_second_elements:
        result = "Счастливый билет"
    else:
        result = "Не счастливый билет"
    return result


def result_function(number_trolleybus_ticket):
    try:
        if number_trolleybus_ticket.isdigit:
            if len(str(number_trolleybus_ticket)) < 6 or len(str(number_trolleybus_ticket)) > 6:
                raise MyError(f"Количество цифр в числе должно быть ровно 6!"
                              f"В вашем номере {len(str(number_trolleybus_ticket))} числа")
        else:
            raise ValueError
    except ValueError:
        print("Неправильный тип переменной")
    except MyError as mr:
        print(mr)
    else:
        print(f"{happiness_ticket(number_trolleybus_ticket)}")
        print(f"Предыдущий счастливый билет {prev_happiness_ticket(number_trolleybus_ticket)}")
        print(f"Следующий счастливый билет {next_happiness_ticket(number_trolleybus_ticket)}")


numb_trolleybus_ticket = input("Определите номер троллейбусного билета? ")
result_function(numb_trolleybus_ticket)


# 3. В директории лежат входные текстовые файлы, проименованные следующим образом: in_<N>.dat, где
# N - натуральное число.
# Каждый файл состоит из двух строк. В первой строке - число, обозначающее действие, а во второй -
# числа с плавающей точкой, разделенные пробелом.
#
# Действия могут быть следующими:
#
# 1 - сложение
#
# 2 - умножение
#
# 3 - сумма квадратов
#
# Необходимо написать многопоточное приложение, которое выполнит требуемые
# действия над числами и сумму результатов запишет в файл out.dat.
# Название рабочей директории передается в виде аргумента рабочей строки.
def function_process(dirs, name_file, q):
    result = 0
    road_file = dirs + "/" + name_file
    str_file = read_file(road_file)
    action = str_file[0].replace("\n", "")
    list_number = str_file[1].split()
    list_float_number = [float(k) for k in list_number]
    if action == '1':
        sum_number = reduce(lambda x, res: x + res, list_float_number)
        result = sum_number
    if action == '2':
        mul_number = reduce(lambda x, y: x * y, list_float_number)
        result = mul_number
    if action == '3':
        double_list = [x * x for x in list_float_number]
        sum_double = reduce(lambda x, res: x + res, double_list)
        result = sum_double
    q.put(result)


directory = "./in.dat"
files = os.listdir(directory)
allProcess = []
sum_for_write_file = 0
queue = Queue()
for i in files:
    t = Process(target=function_process, args=(directory, i, queue))
    t.start()
    allProcess.append(t)
for p in allProcess:
    p.join()
    sum_for_write_file += queue.get()
write_file("./out.dat", str(sum_for_write_file))
