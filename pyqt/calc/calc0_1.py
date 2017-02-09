import sys

from PyQt5 import QtCore, QtWidgets

# To show Qt framework messages.
QtCore.qInstallMessageHandler(lambda t, c, m: print(m))


class Calculator(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        vlout = QtWidgets.QVBoxLayout()
        self.setLayout(vlout)
        
        hlout = QtWidgets.QHBoxLayout()
        c1 = QtWidgets.QPushButton('Push me!')
        self.ledit = QtWidgets.QLineEdit('Type here..')
        hlout.addWidget(c1)
        hlout.addWidget(self.ledit)
        
        c3 = QtWidgets.QCalendarWidget()
        vlout.addLayout(hlout)
        vlout.addWidget(c3)
        
        c1.clicked.connect(self.on_clicked)
    
    @QtCore.pyqtSlot()
    def on_clicked(self):
        self.ledit.setText(self.ledit.text() + ' You clicked the button.')


app = QtWidgets.QApplication(sys.argv)

calc = Calculator()
calc.setWindowTitle('Simple')
calc.resize(400, 400)
calc.show()

sys.exit(app.exec_())
