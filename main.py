import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QLabel
from PyQt6.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 100, 370, 610)
        self.setFixedSize(370, 610)
        self.setWindowTitle('Калькулятор')

        self.flag_point = False
        self.flag_commands = False
        # Первая линия
        self.btn_clear = QPushButton('C', self)
        self.btn_clear.resize(350, 80)
        self.btn_clear.move(10, 520)
        self.btn_clear.setFont(QFont('Arial', 40))
        self.btn_clear.clicked.connect(self.clear)


        # Вторая линия
        self.btn_point = QPushButton(',', self)
        self.btn_point.resize(80, 80)
        self.btn_point.move(10, 430)
        self.btn_point.setFont(QFont('Arial', 40))
        self.btn_point.clicked.connect(self.add_simvol)

        self.btn_0 = QPushButton('0', self)
        self.btn_0.resize(80, 80)
        self.btn_0.move(100, 430)
        self.btn_0.setFont(QFont('Arial', 40))
        self.btn_0.clicked.connect(self.add_simvol)

        self.btn_equally = QPushButton('=', self)
        self.btn_equally.resize(80, 80)
        self.btn_equally.move(190, 430)
        self.btn_equally.setFont(QFont('Arial', 40))
        self.btn_equally.clicked.connect(self.print_result)

        self.btn_plus = QPushButton('+', self)
        self.btn_plus.resize(80, 80)
        self.btn_plus.move(280, 430)
        self.btn_plus.setFont(QFont('Arial', 40))
        self.btn_plus.clicked.connect(self.add_simvol)

        # Третья линия
        self.btn_1 = QPushButton('1', self)
        self.btn_1.resize(80, 80)
        self.btn_1.move(10, 340)
        self.btn_1.setFont(QFont('Arial', 40))
        self.btn_1.clicked.connect(self.add_simvol)

        self.btn_2 = QPushButton('2', self)
        self.btn_2.resize(80, 80)
        self.btn_2.move(100, 340)
        self.btn_2.setFont(QFont('Arial', 40))
        self.btn_2.clicked.connect(self.add_simvol)

        self.btn_3 = QPushButton('3', self)
        self.btn_3.resize(80, 80)
        self.btn_3.move(190, 340)
        self.btn_3.setFont(QFont('Arial', 40))
        self.btn_3.clicked.connect(self.add_simvol)

        self.btn_minus = QPushButton('-', self)
        self.btn_minus.resize(80, 80)
        self.btn_minus.move(280, 340)
        self.btn_minus.setFont(QFont('Arial', 40))
        self.btn_minus.clicked.connect(self.add_simvol)

        # Четвёртая линия
        self.btn_4 = QPushButton('4', self)
        self.btn_4.resize(80, 80)
        self.btn_4.move(10, 250)
        self.btn_4.setFont(QFont('Arial', 40))
        self.btn_4.clicked.connect(self.add_simvol)

        self.btn_5 = QPushButton('5', self)
        self.btn_5.resize(80, 80)
        self.btn_5.move(100, 250)
        self.btn_5.setFont(QFont('Arial', 40))
        self.btn_5.clicked.connect(self.add_simvol)

        self.btn_6 = QPushButton('6', self)
        self.btn_6.resize(80, 80)
        self.btn_6.move(190, 250)
        self.btn_6.setFont(QFont('Arial', 40))
        self.btn_6.clicked.connect(self.add_simvol)

        self.btn_multiply = QPushButton('*', self)
        self.btn_multiply.resize(80, 80)
        self.btn_multiply.move(280, 250)
        self.btn_multiply.setFont(QFont('Arial', 40))
        self.btn_multiply.clicked.connect(self.add_simvol)

        # Пятая линия
        self.btn_7 = QPushButton('7', self)
        self.btn_7.resize(80, 80)
        self.btn_7.move(10, 160)
        self.btn_7.setFont(QFont('Arial', 40))
        self.btn_7.clicked.connect(self.add_simvol)

        self.btn_8 = QPushButton('8', self)
        self.btn_8.resize(80, 80)
        self.btn_8.move(100, 160)
        self.btn_8.setFont(QFont('Arial', 40))
        self.btn_8.clicked.connect(self.add_simvol)

        self.btn_9 = QPushButton('9', self)
        self.btn_9.resize(80, 80)
        self.btn_9.move(190, 160)
        self.btn_9.setFont(QFont('Arial', 40))
        self.btn_9.clicked.connect(self.add_simvol)

        self.btn_div = QPushButton('/', self)
        self.btn_div.resize(80, 80)
        self.btn_div.move(280, 160)
        self.btn_div.setFont(QFont('Arial', 40))
        self.btn_div.clicked.connect(self.add_simvol)

        self.res_text = QLabel('0', self)
        self.res_text.resize(350, 150)
        self.res_text.move(10, 10)
        self.res_text.setFont(QFont('Arial', 40))

        self.stroca = ''

    def add_simvol(self):
        text = self.sender().text()
        if self.stroca == '' and (text == ',' or text in COMANDS):
            return

        s = self.stroca + text

        check_s = s
        for i in COMANDS: check_s = check_s.replace(i, '*')
        for i in NUMS: check_s = check_s.replace(i, '1')

        if '01' in check_s and ',' not in check_s:
            return
        if '*' in check_s:
            list_check_s = check_s.split('*')
            if (list_check_s[-1].count(',') > 1) or ('00' in list_check_s[-1] and ',' not in list_check_s[-1]):
                return
        else:
            if (check_s.count(',') > 1) or ('00' in check_s and ',' not in check_s):
                return


        if text in COMANDS and self.flag_commands:
            self.flag_commands = False
            self.flag_point = False
            self.stroca += text
            self.show_stroca()
        elif text == ',' and self.flag_point:
            self.flag_point = False
            self.flag_commands = False
            self.stroca += text
            self.show_stroca()
        elif text in NUMS or text == '0':
            self.flag_commands = True
            self.flag_point = True
            self.stroca += text
            self.show_stroca()


    def clear(self):
        self.stroca = ''
        self.res_text.setText('0')

    def print_result(self):
        self.stroca = self.stroca.replace(',', '.')
        res = eval(self.stroca)
        self.stroca = str(res)
        self.stroca = self.stroca.replace('.', ',')
        self.show_stroca()

    def show_stroca(self):
        self.res_text.setText(self.stroca)


COMANDS = ['+', '-', '*', '/']
NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMVOLS = ['.']

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())