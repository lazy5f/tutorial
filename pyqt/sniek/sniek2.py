import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRectF

# To show Qt messages.
QtCore.qInstallMessageHandler(lambda t, c, m: print(m))


class Sniek(QtWidgets.QWidget):
    """
    state: ready or started or terminated
    
    M: map
    n, m: numbers of rows and columns of map
    
    S: position of each piece of snake (from head to tail)
    d: direction of head
    """
    
    S_READY, S_STARTED, S_TERMINATED = 0, 1, 2
    
    D = {Qt.Key_Up: (-1, 0), Qt.Key_Down: (1, 0), Qt.Key_Left: (0, -1), Qt.Key_Right: (0, 1)}
    
    def __init__(self):
        super().__init__()
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.tick)
        
        self.get_ready()
    
    def get_ready(self):
        self.state, self.d = self.S_READY, self.D[Qt.Key_Up]
        
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
                    painter.fillRect(QRectF(cw * j, ch * i, cw, ch), Qt.darkGray)
                elif self.M[i][j] == 'S':
                    if (i, j) == self.S[0]:
                        painter.fillRect(QRectF(cw * j, ch * i, cw, ch), Qt.green)
                    else:
                        painter.fillRect(QRectF(cw * j, ch * i, cw, ch), Qt.blue)
        
        painter.setFont(QtGui.QFont('Arial', win_w / 10))
        
        if self.state == self.S_READY:
            painter.drawText(QRectF(0, 0, win_w, win_h), Qt.AlignCenter, 'READY')
        elif self.state == self.S_TERMINATED:
            painter.drawText(QRectF(0, 0, win_w, win_h), Qt.AlignCenter, 'YOU DIED!')
        
        painter.end()
    
    def keyPressEvent(self, e):
        if self.state == self.S_STARTED:
            x = self.D.get(e.key())
            if x and x[0] * self.d[0] + x[1] * self.d[1] == 0:
                self.d = x
        
        elif e.key() == Qt.Key_Space:
            if self.state == self.S_READY:
                self.timer.start(100)
                self.state = self.S_STARTED
            
            elif self.state == self.S_TERMINATED:
                self.get_ready()
                self.update()
    
    def tick(self):
        # Get next position of head.
        i, j = self.S[0][0] + self.d[0], self.S[0][1] + self.d[1]
        
        # Check.
        if self.M[i][j] == 'X' or self.M[i][j] == 'S':
            self.timer.stop()
            self.state = self.S_TERMINATED
        
        else:
            # Add first piece
            self.S.insert(0, (i, j))
            self.M[i][j] = 'S'
            
            # Erase last piece.
            i, j = self.S.pop()
            self.M[i][j] = ' '
        
        self.repaint()


app = QtWidgets.QApplication(sys.argv)

s = Sniek()
s.setWindowTitle('Sniek')
s.resize(400, 400)
s.show()

sys.exit(app.exec_())
