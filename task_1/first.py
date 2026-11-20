class Book:
    def __init__(self, title: str = None, author: str = None, pages: int = None):
        # 1 и 2 задание
        if title or author or pages:

            if title:
                self.__title = title

            if author:
                self.__author = author

            if pages:
                self.__pages = pages

        else:
            self.__title = "Без названия"
            self.__author = "Неизвестен"
            self.__pages = 0

    # 3 задание
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_page_count(self):
        return self.__pages

    def set_title(self, title: str):
        self.__title = title

    def set_author(self, author: str):
        self.__author = author

    def set_page_count(self, page_count: int):
        self.__pages = page_count

    # 4 задание
    def show_info(self):
        print(f"Книга: {self.__title} \n Автор: {self.__author} \n Страниц: {self.__pages} \n")

    # 6 задание
    def check_difficulty(self):
        if self.__pages < 250:
            print("Не сложно")
        else:
            print("сложно")

    def find_reading_speed(self, days: int):
        print("Читать", round(self.__pages / days), "страниц в день")


class Main:
    # 5 задание
    book1 = Book()
    book2 = Book("Война и мир", "Л. Н. Толстой", 1300)

    book1.show_info()
    book2.show_info()

    book1.set_title("Капитанская дочка")
    book1.set_author("А. С. Пушкин")
    book1.set_page_count(320)

    book1.show_info()


# 7 задание

class Menu:
    def __init__(self):
        self.books = (Book("Мастер и Маргарита", "М. А. Булгаков", 480),
                      Book("Мцыри", "М. Ю. Лермонтов", 40))

    def start(self):
        flag = 1
        while flag:
            print("Выберите команду")
            print("1. Показать все книги")
            print("2. Изменить данные книги")
            print("3. Рассчитать скорость чтения книги")
            print("4. Узнать сложность книги")
            print("0. Выход из программы")

            choice = input("Выберите действие: \n")

            if choice == "1":
                print("Список книг:")
                for bok in self.books:
                    bok.show_info()

            elif choice == "2":
                now = int(input("Введите номер книги: ")) + 1
                t = input("Введите новое название: ")
                a = input("Введите нового автора: ")
                p = int(input("Введите количество страниц: "))
                self.books[now].set_title(t)
                self.books[now].set_author(a)
                self.books[now].set_page_count(p)
                print("Данные изменены")

            elif choice == "3":
                now = int(input("Введите номер книги: ")) + 1
                days = int(input("Введите количество дней за которое нужно прочитать книгу "))
                self.books[now].calculate(days)

            elif choice == "4":
                now = int(input("Введите номер книги: ")) + 1
                self.books[now].check_difficulty()

            elif choice == "0":
                print("Конец работы")
                flag = 0

            else:
                print("Неверная команда, попробуйте снова.")


if __name__ == '__main__':
    Main()

    menu = Menu()
    menu.start()
