class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nГод: {self.year}"


my_book = Book('Колобок', 'Пушкин', '1912')
print(my_book.info())