# Function for work with regular

import re


def pattern_dates(text):
    # Шаблон для получения даты в формате DD-MM-YYYY
    pattern = '\d{2}-\d{2}-\d{4}'
    full_dates = re.findall(pattern, text)
    return full_dates


def pattern_years(text):
    # Шаблон для получения года в формате - YYYY
    pattern = '[1-9]{1}\d{3}'
    years = re.findall(pattern, text)
    return years


def pattern_numbers(text):
    # Шаблон для получения отрицательных, положительных чисел и чисел с плавающей точкой
    pattern = '[-+]?\d*\.\d+|[-+]?\d+'
    numbers = re.findall(pattern, text)
    return numbers


def pattern_negative_numbers(text):
    # Шаблон для получения целых отрицательных чисел и отрицательных чисел с плавающей точкой
    pattern = '[-]\d*\.\d+|[-]\d+'
    numbers = re.findall(pattern, text)
    return numbers


def pattern_float_numbers(text):
    # Шаблон для получения целых не отрицательных чисел и не отрицательных чисел с плавающей точкой
    pattern = '^\d*\.\d+$'
    numbers = re.findall(pattern, text)
    return numbers


def pattern_proper_names(text):
    # Шаблон для получения слов, которые начинаются с большой буквы
    pattern = '[А-Я][а-я]*'
    names = re.findall(pattern, text)
    return names