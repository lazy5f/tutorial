import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

# To show Qt messages.
QtCore.qInstallMessageHandler(lambda t, c, m: print(m))


class Sniek(QtWidgets.QWidget):
    """
    n, m: numbers of rows and columns of map
    """
    
    def __init__(self):
        super().__init__()
        
        # Read map.
        with open('1.map') as f:
            self.M = [list(l) for l in f.read().split('\n')]
        
        self.n, self.m = len(self.M), len(self.M[0])
        
        # Initial snake position
        self.S = [(i, self.m // 2) for i in range(self.n - 7, self.n - 1)]
        for i, j in self.S:
            self.M[i][j] = 'S'
    
    def paintEvent(self, e):
        painter = QtGui.QPainter()
        painter.begin(self)
        
        sz = self.size()
        win_w, win_h = sz.width(), sz.height()
        cw, ch = win_w / self.n, win_h / self.m
        
        painter.fillRect(0, 0, win_w, win_h, Qt.white)
        
        for i in range(self.n):
            for j in range(self.m):
                if self.M[i][j] == 'X':
                    painter.fillRect(QtCore.QRectF(cw * j, ch * i, cw, ch), Qt.darkGray)
                elif self.M[i][j] == 'S':
                    if (i, j) == self.S[0]:
                        painter.fillRect(QtCore.QRectF(cw * j, ch * i, cw, ch), Qt.green)
                    else:
                        painter.fillRect(QtCore.QRectF(cw * j, ch * i, cw, ch), Qt.blue)
        
        painter.end()


app = QtWidgets.QApplication(sys.argv)

s = Sniek()
s.setWindowTitle('Sniek')
s.resize(400, 400)
s.show()

sys.exit(app.exec_())
