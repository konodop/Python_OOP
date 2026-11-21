class Book:
    """Класс, содержащий информацию о книге"""

    def __init__(self, title: str = None, author: str = None, pages: int = None) -> None:
        """ Метод инициализации объекта класса

        Args:
            :param title:    Название книги
            :param author:   Автор книги
            :param pages:    Количество страниц
        """
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
    def get_title(self) -> str:
        """Геттер названия

        Returns:
            str: название книги
        """

        return self.__title

    def get_author(self) -> str:
        """Геттер автора

        Returns:
            str: автор книги
        """

        return self.__author

    def get_page_count(self) -> int:
        """Геттер количества страниц

        Returns:
            str: количество страниц
        """

        return self.__pages

    def set_title(self, title: str) -> None:
        """Сеттер Названия

        Args:
            title: название
        """
        self.__title = title

    def set_author(self, author: str) -> None:
        """Сеттер автора

        Args:
            author: автор
        """
        self.__author = author

    def set_pages(self, pages: int) -> None:
        """Сеттер количества страниц

        Args:
            pages: количество страниц
        """
        self.__pages = pages

    # 4 задание
    def show_info(self) -> None:
        """Показывает всю информацию о книге"""

        print(f"Книга: {self.__title} \n Автор: {self.__author} \n Страниц: {self.__pages} \n")

    # 6 задание
    def check_difficulty(self) -> None:
        if self.__pages < 250:
            print("Не сложно")
        else:
            print("сложно")

    def calculate(self, days: int) -> None:
        """
        :param days: Количество дней за которое нужно прочитать книгу
        """
        print("Читать", round(self.__pages / days), "страниц в день")


class Main:
    """ Класс с двумя классами для демонстрации конструкторов методов и операций"""

    # 5 задание
    book1 = Book()
    book2 = Book("Война и мир", "Л. Н. Толстой", 1300)

    book1.show_info()
    book2.show_info()

    book1.set_title("Капитанская дочка")
    book1.set_author("А. С. Пушкин")
    book1.set_pages(320)

    book1.show_info()


# 7 задание

class Menu:
    """Класс с меню, и возможностью выбора действия пользователем действий"""

    def __init__(self):
        """ Метод инициализации объекта класса"""

        self.books = (Book("Мастер и Маргарита", "М. А. Булгаков", 480),
                      Book("Мцыри", "М. Ю. Лермонтов", 40))

    def run(self) -> None:
        """Метод запуска меню"""
        flag = 1

        while flag:
            print("Выберите команду")
            print("1. Показать все книги")
            print("2. Изменить данные книги")
            print("3. Рассчитать скорость чтения книги")
            print("4. Узнать сложность книги")
            print("0. Выход из программы")

            choice = input()

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
                print("Неверная команда")


if __name__ == '__main__':
    Main()

    menu = Menu()
    menu.run()
