from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5 import uic
import sys
import random


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.cl)

    def cl(self):
        self.wnd = Main1()
        self.wnd.show()
        self.close()


class Main1(QMainWindow):
    def __init__(self):
        super(Main1, self).__init__()
        self.setFixedSize(500, 500)
        #a =
        random.choice(range(0, 400))

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRects(qp)
        qp.end()

    def drawRects(self, qp):
        col = QColor(255, 255, 0)
        qp.setPen(col)
        qp.setBrush(QColor(255, 255, 0))
        for i in range(15):
            a = random.choice(range(0, 100))
            qp.drawEllipse(random.choice(range(0, 400)), random.choice(range(0, 400)), a, a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())