from datetime import datetime
from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nГод: {self.year}"

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        return isinstance(other, Book) and other.title == self.title

    @property
    def age(self):
        return datetime.now().year - self.year

    @age.setter
    def age(self, value):
        self.year = datetime.now().year - value

    @classmethod
    def from_string(cls, data):
        title, author, year = data.split(';')
        return cls(title, author, int(year))

    def print_info(self):
        print(self.info())


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nГод: {self.year}\nФормат: {self.format}"


my_book = Book('Колобок', 'Пушкин', 1912)
my_ebook = Ebook('Колобок', 'Пушкин', 1912, 'pdf')
book2 = Book.from_string('Красная шапочка;Пушкин;1949')

book2.print_info()
