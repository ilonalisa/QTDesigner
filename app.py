from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.uic import loadUi
from random import choice

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('QTDesigner1.ui', self)
        self.pushButton.clicked.connect(self.generate_password)
        self.label_2.setText("")

    def generate_password(self):
        password_len = 8
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        numbers = '1234567890'
        symbols = "!@#$%^&*()_+-=<>/:''.,"
        password = ""

        for x in range(password_len):
            if self.checkBox.isChecked():  # Використовувати алфавіт
                password += choice(alphabet)
            if self.checkBox_2.isChecked():  # Використовувати числа
                password += choice(numbers)
            password += choice(symbols)

        self.label_2.setText(password)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
