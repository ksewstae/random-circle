import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor
from random import randint


class Design(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(600, 600)
        self.setWindowTitle('Случайные окружности')
        self.paint_btn = QPushButton('Нарисуй\nокружность', self)
        self.paint_btn.resize(150, 100)
        self.paint_btn.move(225, 250)


class YellowCircle(Design):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.paint_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        radius = randint(0, 300)
        qp.drawEllipse(randint(0, 600 - radius), randint(0, 600 - radius),
                       radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circle = YellowCircle()
    circle.show()
    sys.exit(app.exec())