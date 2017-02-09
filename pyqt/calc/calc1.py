import sys

from PyQt5 import QtCore, QtWidgets

# To show Qt framework messages.
QtCore.qInstallMessageHandler(lambda t, c, m: print(m))


class Calculator(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()

        lout = QtWidgets.QGridLayout()
        self.setLayout(lout)

        self.num = QtWidgets.QLCDNumber(20)
        self.num.display(0)
        b7 = QtWidgets.QPushButton('7')
        b8 = QtWidgets.QPushButton('8')
        b9 = QtWidgets.QPushButton('9')
        bp = QtWidgets.QPushButton('+')
        b4 = QtWidgets.QPushButton('4')
        b5 = QtWidgets.QPushButton('5')
        b6 = QtWidgets.QPushButton('6')
        bm = QtWidgets.QPushButton('-')
        b1 = QtWidgets.QPushButton('1')
        b2 = QtWidgets.QPushButton('2')
        b3 = QtWidgets.QPushButton('3')
        bl = QtWidgets.QPushButton('*')
        b0 = QtWidgets.QPushButton('0')
        be = QtWidgets.QPushButton('=')
        bc = QtWidgets.QPushButton('C')
        bd = QtWidgets.QPushButton('/')
        
        lout.addWidget(self.num, 0, 0, 1, 4)
        lout.addWidget(b7, 1, 0)
        lout.addWidget(b8, 1, 1)
        lout.addWidget(b9, 1, 2)
        lout.addWidget(bp, 1, 3)
        lout.addWidget(b4, 2, 0)
        lout.addWidget(b5, 2, 1)
        lout.addWidget(b6, 2, 2)
        lout.addWidget(bm, 2, 3)
        lout.addWidget(b1, 3, 0)
        lout.addWidget(b2, 3, 1)
        lout.addWidget(b3, 3, 2)
        lout.addWidget(bl, 3, 3)
        lout.addWidget(b0, 4, 0)
        lout.addWidget(be, 4, 1)
        lout.addWidget(bc, 4, 2)
        lout.addWidget(bd, 4, 3)
        
        b1.clicked.connect(self.on_1)
        b2.clicked.connect(self.on_2)
    
    @QtCore.pyqtSlot()
    def on_1(self):
        self.num.display(self.num.value() * 10 + 1)
    
    @QtCore.pyqtSlot()
    def on_2(self):
        self.num.display(self.num.value() * 10 + 2)


app = QtWidgets.QApplication(sys.argv)

calc = Calculator()
calc.setWindowTitle('Calculator')
calc.resize(400, 400)
calc.show()

sys.exit(app.exec_())
