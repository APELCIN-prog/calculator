import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QCheckBox, QSpinBox


class CreatePassword(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.items = [False, False, False, False]
        self.lenght = 0

    def initUI(self):
        self.setGeometry(500, 100, 300, 350)
        self.setFixedSize(300, 350)
        self.setWindowTitle('Генератор паролей')

        self.password = QLabel(self)
        self.password.resize(280, 100)
        self.password.move(10, 10)

        self.create_btn = QPushButton('Сгенерировать пароль', self)
        self.create_btn.resize(280, 50)
        self.create_btn.move(10, 110)
        self.create_btn.clicked.connect(self.create_password)

        self.small_book_checkbox = QCheckBox('Использовать буквы нижнего регистра', self)
        self.small_book_checkbox.move(20, 170)
        self.small_book_checkbox.stateChanged.connect(self.state_changed_small_book_checkbox)

        self.big_book_checkbox = QCheckBox('Использовать буквы верхнего регистра', self)
        self.big_book_checkbox.move(20, 200)
        self.big_book_checkbox.stateChanged.connect(self.state_changed_big_book_checkbox)

        self.spechial_simbols_checkbox = QCheckBox('Использовать спец символы', self)
        self.spechial_simbols_checkbox.move(20, 230)
        self.spechial_simbols_checkbox.stateChanged.connect(self.state_changed_spechial_simbols_checkbox)

        self.nums_checkbox = QCheckBox('Использовать цифры', self)
        self.nums_checkbox.move(20, 260)
        self.nums_checkbox.stateChanged.connect(self.state_changed_nums_checkbox)

        self.text = QLabel('Длина:', self)
        self.text.move(20, 290)
        self.spin_box_len = QSpinBox(self)
        self.spin_box_len.resize(100, 20)
        self.spin_box_len.move(70, 290)

    def state_changed_small_book_checkbox(self):
        self.items[0] = not (self.items[0])

    def state_changed_big_book_checkbox(self):
        self.items[1] = not (self.items[1])

    def state_changed_spechial_simbols_checkbox(self):
        self.items[2] = not (self.items[2])

    def state_changed_nums_checkbox(self):
        self.items[3] = not (self.items[3])

    def create_password(self):
        try:
            res = []
            self.lenght = self.spin_box_len.value()
            flag = sum(self.items)
            for i in range(len(self.items)):
                if self.items[i]:
                    count = self.lenght - sum(self.items[i:]) - len(res) + 1
                    c = random.randint(1, count)
                    flag -= 1
                    if flag == 0:
                        c = count
                    for _ in range(c):
                        res.append(random.choice(DATA[i]))

            random.shuffle(res)
            self.password.setText(''.join(res))
        except:
            self.password.setText('ERROR')


small_book = 'abcdefghijklmnopqrstuvwxyz'
big_book = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
spechial_simbols = '!#$%^&*()?_-+'
DATA = [small_book, big_book, spechial_simbols, nums]


def generate_password(items, lenght):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CreatePassword()
    ex.show()
    sys.exit(app.exec())
