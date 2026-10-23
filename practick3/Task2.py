class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nГод: {self.year}"


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nГод: {self.year}\nФормат: {self.format}"


my_book = Book('Колобок', 'Пушкин', '1912')
my_ebook = Ebook('Колобок', 'Пушкин', '1912', 'pdf')
print(my_book.info())
print()
print(my_ebook.info())
