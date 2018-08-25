import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Ico(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)    #前两个参数定义窗口位置,后两个定义窗口大小
        self.setWindowTitle("学习状态中")
        self.setWindowIcon(QIcon('bitbug_favicon.ico'))

        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(70, 30)
        qbtn.move(50, 50)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    # try:
    #     if len(sys.argv) < 2:
    #         raise ValueError
    #     else:
    #         title = " ".join(sys.argv[1:])
    # except ValueError:
    #     title = "学习状态中"

    # w = QWidget()
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle(title)
    # w.show()

    ex = Ico()
    sys.exit(app.exec_())
