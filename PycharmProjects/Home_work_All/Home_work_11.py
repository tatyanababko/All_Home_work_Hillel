# Описать класс «домашняя библиотека».
# Предусмотреть возможность работы:
# 1. С произвольным числом книг;
# 2. Поиска книги по какому-либо признаку (например, по автору или по году издания);
# 3. Добавления книг в библиотеку;
# 4. Удаления книг из нее;
# 5. Сортировки книг по разным полям.


from Read_Write_File import read_file_pickle
from Read_Write_File import write_file_pickle
from Constants import NAME_FILE_DB
from Constants import PARAMETRS_FOR_DICT


class HomeLibrary:
    def __init__(self, autors, title, tome, publishing, year):
        self.autors = autors
        self.title = title
        self.tome = tome
        self.publishing = publishing
        self.year = year

    def add_book(self):
        values = [self.autors, self.title, self.tome, self.publishing, self.year]
        filds = dict(zip(PARAMETRS_FOR_DICT, values))
        try:
            work_data = read_file_pickle(NAME_FILE_DB)
        except FileNotFoundError:
            write_file_pickle(NAME_FILE_DB, filds)
        except EOFError:
            if values:
                write_file_pickle(NAME_FILE_DB, filds)
            else:
                print("Необходимо создать объект класса")
        else:
            if isinstance(work_data, list):
                work_lst = [data for data in work_data]
            else:
                work_lst = [work_data]
            if filds not in work_lst:
                work_lst.append(filds)
                write_file_pickle(NAME_FILE_DB, work_lst)
            else:
                print("Книга с такими параметрами уже существует")

    @staticmethod
    def del_book(*args):
        work_lst = []
        values = [i for i in args]
        filds = dict(zip(PARAMETRS_FOR_DICT, values))
        try:
            work_data = read_file_pickle(NAME_FILE_DB)
        except FileNotFoundError:
            print("Файла с данными не существует")
        except EOFError:
            print("Фаил пуст")
        else:
            if isinstance(work_data, list):
                work_lst = [data for data in work_data if data != filds]
            else:
                if work_data != filds:
                    work_lst.append(work_data)
            write_file_pickle(NAME_FILE_DB, work_lst)

    @staticmethod
    def search_book(*args):
        values = [i for i in args]
        filds = dict(zip(PARAMETRS_FOR_DICT, values))
        restrictions = {key: value for key, value in filds.items() if value}
        try:
            work_data = read_file_pickle(NAME_FILE_DB)
        except FileNotFoundError:
            print("Файла с данными не существует")
        except EOFError:
            print("Фаил пуст")
        else:
            if isinstance(work_data, list):
                for i in work_data:
                    if all(k in i and i[k] == restrictions[k] for k in restrictions):
                        print(i)
            else:
                if all(k in work_data and work_data[k] == restrictions[k] for k in restrictions):
                    print(work_data)

    @staticmethod
    def sort_book(key_sort):
        try:
            work_data = read_file_pickle(NAME_FILE_DB)
        except FileNotFoundError:
            print("Файла с данными не существует")
        except EOFError:
            print("Фаил пуст")
        else:
            if isinstance(work_data, list):
                if key_sort == '1':
                    work_data.sort(key=lambda dictionary: dictionary[PARAMETRS_FOR_DICT[0]])
                if key_sort == '2':
                    work_data.sort(key=lambda dictionary: dictionary[PARAMETRS_FOR_DICT[1]])
                if key_sort == '3':
                    work_data.sort(key=lambda dictionary: dictionary[PARAMETRS_FOR_DICT[4]])
                print(work_data)
            else:
                print("В библиотеке всего одна книга")


def menu_about_book():
    print("Введите данные о книге:")
    aut_book = input("Автор книги: ")
    titl_book = input("Название книги: ")
    tom_book = input("Том книги: ")
    publish_book = input("Издание книги: ")
    years_book = input("Год издания: ")
    return aut_book, titl_book, tom_book, publish_book, years_book


def menu_sort_book():
    key_sort = input("1. Сортировка по автору книги\n"
                     "2. Сортировка по названию книги\n"
                     "3. Сортировка по году издания\n"
                     "Выберите действие, которое необходимо выполнить: ")
    return key_sort


def main_menu():
    action = input("1. Добавить новую книгу\n"
                   "2. Удалить книгу из библиотеки\n"
                   "3. Найти книгу\n"
                   "4. Отсортировать книги:\n"
                   "Выберите действие, которое необходимо выполнить: ")
    if action == "1":
        autor_book, title_book, tome_book, publishing_book, year_book = menu_about_book()
        books = HomeLibrary(autor_book, title_book, tome_book, publishing_book, year_book)
        books.add_book()
    elif action == "2":
        autor_book, title_book, tome_book, publishing_book, year_book = menu_about_book()
        HomeLibrary.del_book(autor_book, title_book, tome_book, publishing_book, year_book)
    elif action == "3":
        autor_book, title_book, tome_book, publishing_book, year_book = menu_about_book()
        HomeLibrary.search_book(autor_book, title_book, tome_book, publishing_book, year_book)
    elif action == "4":
        key_for_sort = menu_sort_book()
        HomeLibrary.sort_book(key_for_sort)


main_menu()
