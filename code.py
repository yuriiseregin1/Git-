from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5 import uic
import sys
import random


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setFixedSize(400, 400)
        self.btn = QPushButton(self)
        self.btn.move(150, 150)
        self.btn.resize(50, 50)
        self.btn.setText('Кнопка')
        self.btn.clicked.connect(self.cl)

    def cl(self):
        self.wnd = Main1()
        self.wnd.show()
        self.close()


class Main1(QWidget):
    def __init__(self):
        super(Main1, self).__init__()
        self.setFixedSize(500, 500)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRects(qp)
        qp.end()

    def drawRects(self, qp):
        print(2)
        col = QColor(255, 255, 0)
        qp.setPen(col)
        print(3)
        qp.setBrush(QColor(random.choice(range(0, 255)), random.choice(range(0, 255)), random.choice(range(0, 255))))
        print(4)
        for i in range(15):
            qp.setBrush(
                QColor(random.choice(range(0, 255)), random.choice(range(0, 255)), random.choice(range(0, 255))))
            a = random.choice(range(0, 100))
            qp.drawEllipse(random.choice(range(0, 400)), random.choice(range(0, 400)), a, a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())