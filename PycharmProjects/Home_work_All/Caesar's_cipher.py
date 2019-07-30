# Зашифровать файл шифром цезаря, Сдвиг вводит пользователь

a_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
list_a_letters = list(a_letters)
work_list = []
try:
    with open('./text_file.txt', 'r', encoding='utf-8') as read_file:
        text_file = read_file.readlines()
except FileNotFoundError:
    print("Фаил отсутствует в директории.")
    text_for_write = ""
    with open('./text_file.txt', 'w', encoding='utf-8') as write_file:
        print("Фаил успешно создан, заполните его текстом для шифрования.\n"
              "Используйте пробел для записи нескольких строк в фаил")
        txt = input("Текст: ")
        work_txt = txt.split(" ")
        cntError = 0
        for i in work_txt:
            for j in i:
                if j in list_a_letters or j.isdigit():
                    pass
                else:
                    cntError += 1
        if cntError == 0:
            for i in work_txt:
                text_for_write += i + "\n"
            write_file.write(text_for_write)
            print("Данные записаны в фаил.")
        else:
            print("Введены недопустимые символы для шифрования.")
    print("Необходимо выполнить повторный запуск программного кода")
else:
    if text_file == []:
        print("Фаил пуст")
        text_for_write = ""
        with open('./text_file.txt', 'w', encoding='utf-8') as write_file:
            print("Заполните его текстом для шифрования.\n"
                  "Используйте пробел для записи нескольких строк в фаил")
            txt = input("Текст: ")
            work_txt = txt.split(" ")
            ctError = 0
            for i in work_txt:
                for j in i:
                    if j in list_a_letters or j.isdigit():
                        pass
                    else:
                        ctError += 1
            if ctError == 0:
                for i in work_txt:
                    text_for_write += i + "\n"
                write_file.write(text_for_write)
                print("Данные записаны в фаил.")
            else:
                print("Введены недопустимые символы для шифрования.")
        print("Необходимо выполнить повторный запуск программного кода")
    else:
        textError = ""
        shift = input("Необходимо ввести сдвиг для шифрования в виде целого числа: ")
        if shift.isdigit():
            for i in text_file:
                simb = i.find("\n")
                if simb != -1:
                    i = i.replace("\n", "")
                work_list.append(i)
            shifr_text_for_file = ""
            for i in work_list:
                for j in i:
                    if j in list_a_letters or j.isdigit():
                        if j in list_a_letters:
                            ind_let = list_a_letters.index(j) + int(shift)
                            if ind_let > len(list_a_letters) - 1:
                                ind_let = ind_let - len(list_a_letters)
                                shifr_text_for_file += list_a_letters[ind_let]
                            else:
                                shifr_text_for_file += list_a_letters[ind_let]
                        elif j.isdigit():
                            ind_dig = int(j) + int(shift)
                            if ind_dig > 9:
                                ind_dig = ind_dig - int(j)
                                shifr_text_for_file += str(ind_dig)
                            else:
                                shifr_text_for_file += str(ind_dig)
                    else:
                        textError = "Фаил содержит недопустимые символы для данного словаря."
                shifr_text_for_file += "\n"
            if textError != "":
                print(textError)
                txt_for_write = ""
                with open('./text_file.txt', 'w', encoding='utf-8') as write_file:
                    txt = input("Текст: ")
                    wrk_txt = txt.split(" ")
                    for i in wrk_txt:
                        txt_for_write += i + "\n"
                    write_file.write(txt_for_write)
                print("Необходимо выполнить повторный запуск программного кода")
            else:
                with open('./text_file.txt', 'w', encoding='utf-8') as write_file:
                    write_file.writelines(shifr_text_for_file[0:len(shifr_text_for_file) - 1])
        else:
            print("Внимание!!!")
            shift = input("Необходимо ввести сдвиг для шифрования в виде целого числа: ")
            if shift.isdigit():
                for i in text_file:
                    simb = i.find("\n")
                    if simb != -1:
                        i = i.replace("\n", "")
                    work_list.append(i)
                shifr_text_for_file = ""
                for i in work_list:
                    for j in i:
                        if j in list_a_letters or j.isdigit():
                            if j in list_a_letters:
                                ind_let = list_a_letters.index(j) + int(shift)
                                if ind_let > len(list_a_letters) - 1:
                                    ind_let = ind_let - len(list_a_letters)
                                    shifr_text_for_file += list_a_letters[ind_let]
                                else:
                                    shifr_text_for_file += list_a_letters[ind_let]
                            elif j.isdigit():
                                ind_dig = int(j) + int(shift)
                                if ind_dig > 9:
                                    ind_dig = ind_dig - int(j)
                                    shifr_text_for_file += str(ind_dig)
                                else:
                                    shifr_text_for_file += str(ind_dig)
                        else:
                            textError = "Фаил содержит недопустимые символы для данного словаря."
                    shifr_text_for_file += "\n"
                if textError != "":
                    print(textError)
                    text_for_write = ""
                    with open('./text_file.txt', 'w', encoding='utf-8') as write_file:
                        txt = input("Текст: ")
                        work_txt = txt.split(" ")
                        for i in work_txt:
                            write_file.write(text_for_write)
                    print("Необходимо выполнить повторный запуск программного кода")
                else:
                    shifr_text_for_file += "\n"
                    with open('./text_file.txt', 'w', encoding='utf-8') as write_file:
                        write_file.writelines(shifr_text_for_file[0:len(shifr_text_for_file) - 1])
            else:
                print("Сдвиг для шифрования вводится в виде целого числа")
finally:
    print("Успешный выход")