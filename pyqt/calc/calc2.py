import sys

from PyQt5 import QtCore, QtWidgets


class Calculator(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()

        lout = QtWidgets.QGridLayout()
        self.setLayout(lout)

        self.num = QtWidgets.QLCDNumber(20)
        self.num.display(0)
        lout.addWidget(self.num, 0, 0, 1, 4)
        
        for i, T in enumerate([(7, 8, 9, '+'), (4, 5, 6, '-'), (1, 2, 3, '*'), (0, '=', 'C', '/')]):
            for j, t in enumerate(T):
                b = QtWidgets.QPushButton(str(t))
                b.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                b.clicked.connect(self.on_input)
                lout.addWidget(b, i + 1, j)
        
        self.last_val, self.last_op, self.reset = 0, '+', False
    
    @QtCore.pyqtSlot()
    def on_input(self):
        t = self.sender().text()
        
        if '0' <= t <= '9':
            if self.reset:
                prev = 0
                self.reset = False
            else:
                prev = self.num.value() * 10
            
            self.num.display(prev + eval(t))
            
        elif t == 'C':
            self.last_val = 0
            self.num.display(0)
            
        elif t == '=':
            cur = self.num.value()
            self.num.display(eval(str(self.last_val) + self.last_op + str(cur)))
            self.last_val, self.reset = cur, True
            
        else:  # t == '+' or '-' or '*' or '-'
            self.last_val, self.last_op, self.reset = self.num.value(), t, True


app = QtWidgets.QApplication(sys.argv)

calc = Calculator()
calc.setWindowTitle('Calculator')
calc.resize(400, 400)
calc.show()

sys.exit(app.exec_())
