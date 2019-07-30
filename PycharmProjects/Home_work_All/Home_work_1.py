# Задание 1:
# Пользователь вводит свое имя и возраст
# вывести строку в формате - “Hello {username} your age is {age}”,
# заменить текст в фигурных скобках на значения введенные пользователем.

#username = input("Name:")
#age = int(input("Age:"))
#print(f"Hello {username} your age is {age}")

# Задание 2:
# Пользователь вводит число,
# вывести его в 132 степени и
# Показать его остаток от деления на 3.
# Вывод должен быть в одну строку с пояснениями.

#number = int(input("Input number:"))
#print(f"123 степень числа = {number ** 123}\nОстаток от деления числа на 3 = {number % 3}")

# Задание 3:
# Пользователь вводит 2 числа
# вывести каждую математическую операцию для этих чисел.
# Каждая новая операция должна быть выведена с новой строки с  пояснением.

#number_first = int(input("Input first number:"))
#number_second = int(input("Input second number:"))
#print(f"Сложение  (x + y): {number_first + number_second}\n"
#      f"Вычитание (x - y): {number_first - number_second}\n"
#      f"Умножение (x * y): {number_first * number_second}\n"
#      f"Деление   (x / y): {number_first / number_second}\n"
#      f"Остаток от деления   (x % y):  {number_first % number_second}\n"
#      f"Возведение в степень (x ** y): {number_first ** number_second}\n"
#      f"Получение целой части от деления (x // y): {number_first // number_second}\n"
#      f"Преобразование в отрицательное число (-x): {- number_first}, {- number_second}\n"
#      f"Увеличение приоритета расчета   (x+(x-y)): {(number_first + (number_first - number_second))}")

# Задание 4:
# Пользователь вводит 3 числа,
# подставить и посчитать формулу: 2a - 8b / (a-b+c).
# Вывести результат.

#number_first =  int(input("Input a:"))
#number_second = int(input("Input b:"))
#number_third =  int(input("Input c:"))
#print(f"2a - 8b / (a-b+c) = {2 * number_first - 8 * number_second / (number_first - number_second + number_third)}")

# Задание 5:
# Пользователь вводит строку и число,
# вывести повторение строки равное введенному числу.
# Вывод должен быть в одну строку.

#strng = input("Input string:")
#umber = int(input("Input number:"))
#print(f"Повторение строки, равное введенному числу: '{strng * number}'")

# Задание 6:
# Даны числа 125 и 437
# вывести их остатки от деления на 2, 3, 10, 22 с пояснениями.

#number_first  = 125
#number_second = 437
#print(f"Остаток от деления числа {number_first} на:\n"
#      f"2  => {number_first % 2}\n"
#      f"3  => {number_first % 3}\n"
#      f"10 => {number_first % 10}\n"
#      f"22 => {number_first % 22}\n"
#      f"\n"
#      f"Остаток от деления числа {number_second} на:\n"
#      f"2  => {number_second % 2}\n"
#      f"3  => {number_second % 3}\n"
#      f"10 => {number_second % 10}\n"
#      f"22 => {number_second % 22}\n")

# Задание 7:
# Пользователь вводит 2 числа,
# вывести целую часть от деления одного на другое

#number_first = int(input("Input first number:"))
#number_second = int(input("Input second number:"))
#print(f"Целая часть от деления = {number_first // number_second}")

# Задание 8:
# Пользователь  вводит 3 строки.
# Вывести их в одну строку разделенные пробелом.
# В этой задаче метод print может принимать только один параметр.

#strng_first  = input("Input first  string:")
#strng_second = input("Input second string:")
#strng_third  = input("Input third  string:")
#strng_total = strng_first + " " + strng_second + " " + strng_third
#print(strng_total)

# Задание 9:
# Даны два числа first = 15, second = 43,
# записать first в second, a second в first.
# Вывести

first = 15
second = 43
first, second = second, first
print(f"First  = {first}\n"
      f"Second = {second}")