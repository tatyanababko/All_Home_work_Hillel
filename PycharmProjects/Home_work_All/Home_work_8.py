# Написать декоратор который будет выводить на экран время выполнения функции.

import time
import math


def decorator_function(func):
    def wrapper(*args, **kwargs):
        start_function = time.time()
        return_value = func(*args, **kwargs)
        end_function = time.time()
        print(f'Время выполнения функции: {end_function - start_function}')
        return return_value
    return wrapper

@decorator_function
def create_geomet_generator(b0, q, n):
    for n in range(1, n + 1):
        yield b0 * math.pow(q, n - 1)

first_term_gprogres = int(input("Введите первый член геометрической прогрессии b1 = "))
denominator = int(input("Введите знаменатель геометрической прогрессии q = "))
numb_term = int(input("Какое количество членов геометрической прогресии необходимо вывести на экран? n = "))
for i in create_geomet_generator(first_term_gprogres, denominator, numb_term):
    print(i)

# Сформировать убывающий массив из чисел, которые делятся на 3. Длину вводит пользователь.

def decreasing_array(len_mass):
    div_on_three = [3 * i for i in range(1, int(len_mass))]
    div_on_three.reverse()
    return div_on_three

decreasing_number_array = input("Определите длину массива, который необходимо вывести на экран: ")
if decreasing_number_array.isdigit():
    print(decreasing_array(decreasing_number_array))
else:
    print("Введена строка")

# Написать декоратор skip который не выполняет функцию.
# Декоратор может принимать параметр который выдаст функция вместо реального результата.


def skip(param):
    def for_func(f):
        def wrapper(*args, **kwargs):
            return 10 * int(param) * int(f(*args, **kwargs))
        return wrapper
    return for_func


@skip(param=3)
def function_array(indes):
    return 2*int(indes)


parametr = input("Определите параметр: ")
if parametr.isdigit():
    print(function_array(parametr))
else:
    print("Введена строка")

# Напишите генератор генерирующий последовательность треугольных чисел.

def triangle_generator(n):
    for j in range(1, int(n) + 1):
        yield j * (j - 1) / 2

len_generetor = input("Введите количество треугольных чисел, которое необходимо вывести на экран: ")
if len_generetor.isdigit():
    for i in triangle_generator(len_generetor):
        print(i)
else:
    print("Введена строка")