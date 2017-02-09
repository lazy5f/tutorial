import sys

from PyQt5 import QtCore, QtWidgets

# To show Qt framework messages.
QtCore.qInstallMessageHandler(lambda t, c, m: print(m))


app = QtWidgets.QApplication(sys.argv)

w = QtWidgets.QWidget()
w.setWindowTitle('Simple')
w.resize(400, 400)

c1 = QtWidgets.QPushButton('Push me!', w)
c1.move(50, 50)
QtWidgets.QLineEdit('Type here..', w, pos=QtCore.QPoint(50, 100))
QtWidgets.QCalendarWidget(w, pos=QtCore.QPoint(50, 150))

w.show()

sys.exit(app.exec_())
