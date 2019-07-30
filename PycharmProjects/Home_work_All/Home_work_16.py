# Реализовать калькулятор аля как в windows, НЕ инженерный. exe не обязателен, но будет + если сделаете


from tkinter import *
from tkinter import ttk

import re


def check_error_function(text):
    text_error = "Некорректный формат для расчета"
    check_error = 0
    if len(text) != 0:
        result = text
        if text[0].isdigit():
            for it in text:
                if it not in work_text_button:
                    value_entry.delete(0, END)
                    value_entry.insert(END, text_error)
                    check_error += 1
                    result = ""
        else:
            value_entry.delete(0, END)
            value_entry.insert(END, text_error)
            check_error += 1
            result = ""
    else:
        result = ""
    return result


def result_function(txt):
    work_text = check_error_function(txt)
    if work_text != "":
        simbol = [s for s in work_text if s in ["+", "-"]]
        new_work_text = re.split('[+ -]', work_text)
        ind_elements = 0
        for n in new_work_text:
            if n.find("/") != -1 or n.find("*") != -1:
                simbol_in_simbol = [nn for nn in n if nn in ["/", "*"]]
                number_in_simbol = re.split('[/ *]', n)
                list_number_in_simbol = [float(lns) for lns in number_in_simbol]
                result_operation = list_number_in_simbol[0]
                ind_operation = 0
                for jr in range(1, len(list_number_in_simbol)):
                    if simbol_in_simbol[ind_operation] == "*":
                        result_operation *= list_number_in_simbol[jr]
                        ind_operation += 1
                    elif simbol_in_simbol[ind_operation] == "/":
                        if list_number_in_simbol[jr] != 0.0:
                            result_operation /= list_number_in_simbol[jr]
                            ind_operation += 1
                        else:
                            value_entry.delete(0, END)
                            value_entry.insert(END, "Деление на ноль = ")
                            result_operation = 0.0
                new_work_text[ind_elements] = result_operation
                ind_elements += 1
            else:
                ind_elements += 1
        new_index_elements = 0
        list_float_new_work_text = [float(lfnwt) for lfnwt in new_work_text]
        new_result_operation = list_float_new_work_text[0]
        for nwt in range(1, len(list_float_new_work_text)):
            if simbol[new_index_elements] == "+":
                new_result_operation += list_float_new_work_text[nwt]
                new_index_elements += 1
            elif simbol[new_index_elements] == "-":
                new_result_operation -= list_float_new_work_text[nwt]
                new_index_elements += 1
        result = new_result_operation
    else:
        result = ""
    return result


def get_set_text_from_button(simb):
    if simb in text_button and simb not in exclusion_elements:
        value_entry.insert(END, simb)
    else:
        if simb == "=":
            text_operation = value_entry.get()
            value_entry.delete(0, END)
            result = result_function(text_operation)
            if result != "":
                value_entry.insert(END, result)
                text_operation += "="
                text_operation += str(result)
                text_operation += "\n"
                text_box.insert(END, text_operation)
        elif simb == "c":
            value_entry.delete(0, END)
        elif simb == "ce":
            value_entry.delete(0, END)
            text_box.delete('1.0', END)


app = Tk()

# Внешний вид
app.title("Простой режим калькулятора")
app.geometry("650x360+300+200")
app.configure(background='#c6c6c6')

# Верхняя часть для отображения арифметических операций
text_box = Text(app, width=80, height=5, background='#c6c6c6')
text_box.grid(row=1, column=0, columnspan=6, ipadx=1, ipady=6, padx=1, pady=10, sticky=W + E)

scroll = Scrollbar(app, command=text_box.yview)
scroll.grid(row=1, column=5, columnspan=1, sticky=E)

text_box.config(yscrollcommand=scroll.set)

# Поле ввода
value_entry = Entry(app, width=80)
value_entry.focus_set()
value_entry.grid(row=2, column=0, columnspan=6, ipadx=1, ipady=6, padx=1, pady=10, sticky=W + E)

# Нижняя панель кнопок

text_button = ["7", "8", "9", "/", "c", "ce", "4", "5", "6", "*", "-", "+", "1", "2", "3",  "0", ".", "="]
work_text_button = ["7", "8", "9", "/", "4", "5", "6", "*", "-", "+", "1", "2", "3",  "0", "."]
exclusion_elements = ["c", "ce", "="]
arifm_operations = ["/", "*", "-", "+"]
cnt = 0
for i in range(3, 6):
    for j in range(0, 6):
        btn = ttk.Button(app, text=text_button[cnt], command=lambda x=text_button[cnt]: get_set_text_from_button(x))
        btn.grid(row=i, column=j, columnspan=1, ipadx=1, ipady=6, padx=1, pady=10, sticky=W + E)
        cnt += 1

app.resizable(0, 0)
app.mainloop()
