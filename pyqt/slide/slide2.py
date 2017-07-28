import sys
from random import choice
import urllib.request

from PyQt5 import QtCore, QtGui, QtWidgets

# To show Qt framework messages.
QtCore.qInstallMessageHandler(lambda t, c, m: print(m))


D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
S = 200


class Slide(QtWidgets.QWidget):
    
    def __init__(self, r):
        super().__init__()
        
        self.T, self.xr, self.xc = [[0, 1, 2], [3, 4, 5], [6, 7, None]], 2, 2
        
        self.img = QtGui.QPixmap()
        url = 'http://r.ddmcdn.com/s_f/o_1/cx_462/cy_245/cw_1349/ch_1349/w_720/APL/uploads/2015/06/caturday-shutterstock_149320799.jpg'
        self.img.loadFromData(urllib.request.urlopen(url).read())
        
        # Shuffle initially.
        for _ in range(r):
            while True:
                dr, dc = choice(D)
                xr1, xc1 = self.xr + dr, self.xc + dc
                if 0 <= xr1 < 3 and 0 <= xc1 < 3:
                    break
            
            self.T[self.xr][self.xc], self.T[xr1][xc1] = self.T[xr1][xc1], None
            self.xr, self.xc = xr1, xc1
    
    def paintEvent(self, e):
        w_3, h_3 = self.img.width() / 3, self.img.height() / 3
        
        qp = QtGui.QPainter()
        qp.begin(self)
        
        for r in range(3):
            for c in range(3):
                t = self.T[r][c]
                if t is not None:
                    qp.drawPixmap(c * S, r * S, S, S, self.img,
                                  (t % 3) * w_3, (t // 3) * h_3, w_3, h_3)
                
                qp.drawRect(c * S, r * S, S, S)
        
        qp.end()
    
    def mousePressEvent(self, e):
        xr1, xc1 = e.y() // S, e.x() // S
        
        for dr, dc in D:
            if self.xr + dr == xr1 and self.xc + dc == xc1:
                self.T[self.xr][self.xc], self.T[xr1][xc1] = self.T[xr1][xc1], None
                self.xr, self.xc = xr1, xc1
        
                self.update()
                break


app = QtWidgets.QApplication(sys.argv)

s = Slide(100)
s.setWindowTitle('Slide')
s.show()

sys.exit(app.exec_())
