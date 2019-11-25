import sys
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
import random


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.resize(self.pushButton.sizeHint())
        self.pushButton.clicked.connect(self.btn_pressed)

        self.pic = None
        self.qp = QPainter()

    def draw_temp(self):
        self.update()

    def draw(self, circle):
        if circle:
            for _ in range(1, 9):
                d = random.randint(5, 60)
                self.pen = QPen(QColor(random.randint(0, 255),
                               random.randint(0, 255), random.randint(0, 255)),
                                d, Qt.DashDotLine, Qt.RoundCap, Qt.RoundJoin)
                self.qp.setPen(self.pen)
                self.qp.drawEllipse(random.randint(0, 600),
                                    random.randint(0, 600), d, d)

    def btn_pressed(self):
        self.pic = True
        self.draw_temp()

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw(self.pic)
        self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())