import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, \
    QDialog, QLineEdit

SCREEN_SIZE = [455, 600]
IMAGES = [None, 'image.png', 'image2.png', 'image3.png', 'image4.png', 'image5.png',
          'image6.png', 'image7.png']
ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


class CreateForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 100, SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 4)
        self.setWindowTitle('Загадай слово')
        self.text = QLabel('Загадай слово', self)
        self.text.move(70, 20)
        self.text_line = QLineEdit('', self)
        self.text_line.resize(SCREEN_SIZE[0] // 2 - 20, 20)
        self.text_line.move(10, 50)

        self.btn = QPushButton('Загадать', self)
        self.btn.resize(200, 50)
        self.btn.move(15, 80)
        self.btn.clicked.connect(self.check_word)

    def check_word(self):
        word = self.text_line.text().upper()
        if all(i.upper() in ALPHABET for i in word) and word and ' ' not in word:
            self.accept()

    def get_word(self):
        return self.text_line.text().upper()


class EndForm(QDialog):
    def __init__(self, is_win, parent=None):
        super().__init__(parent)
        self.is_win = is_win
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 200, SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 4)
        self.label = QLabel('', self)
        self.label.resize(200, 50)
        self.label.move(50, 50)
        self.label.setFont(QFont('Arial', 20))
        if self.is_win:
            self.label.setText('ПОБЕДА!')
        else:
            self.label.setText('ПОРАЖЕНИЕ!')
            self.label.move(20, 50)

        self.btn_end = QPushButton('Заново', self)
        self.btn_end.resize(100, 20)
        self.btn_end.move(60, 120)
        self.btn_end.clicked.connect(self.restart)

    def restart(self):
        self.accept()


class Gallows(QWidget):
    def __init__(self):
        super().__init__()
        self.errors = 0
        self.clears = 0
        self.word = ''
        self.books = []
        self.win = False
        self.initUI()

    def initUI(self):
        self.setGeometry(450, 100, *SCREEN_SIZE)

        self.btn_create = QPushButton('Загадать слово', self)
        self.btn_create.resize(100, 100)
        self.btn_create.move(10, 10)
        self.btn_create.clicked.connect(self.create_word)
        position = [10, 300]
        for i in range(len(ALPHABET)):
            btn = QPushButton(ALPHABET[i], self)
            btn.resize(50, 50)
            btn.move(*position)
            btn.clicked.connect(self.click)
            position[0] = position[0] + 55
            if position[0] + 50 >= SCREEN_SIZE[0]:
                position[0] = 10
                position[1] = position[1] + 55

    def click(self):
        button = self.sender()
        self.check(button.text())
        button.deleteLater()

    def check(self, later):
        if later.lower() in self.word.lower():
            for elem in self.books:
                if elem[1] == later:
                    elem[0].setText(later)
                    self.clears += 1
            if self.clears >= len(self.word):
                self.win = True
                self.create_end_form()
        else:
            self.errors += 1
            if self.errors >= 8:
                self.create_end_form()
                return
            self.pixmap = QPixmap(f'viselica_images/{IMAGES[self.errors]}')
            self.image = QLabel(self)
            self.image.move(200, 20)
            self.image.resize(200, 200)
            self.image.setPixmap(self.pixmap)
            self.image.setScaledContents(True)
            self.image.show()

    def create_end_form(self):
        dialog = EndForm(self.win, self)
        if dialog.exec():
            self.new_game = Gallows()
            self.new_game.show()
            self.close()

    def create_word(self):
        dialog = CreateForm(self)
        if dialog.exec():
            self.word = dialog.get_word()

            position = [10, 250]

            for i in range(len(self.word)):
                label = QLabel('X', self)
                label.resize(15, 15)
                label.setStyleSheet('background-color: gray; border: 1px solid red;')
                label.move(*position)
                label.setFont(QFont('Arial', 10))
                label.show()
                self.books.append([label, self.word[i]])
                position[0] = position[0] + 20


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gallows()
    ex.show()
    sys.exit(app.exec())
