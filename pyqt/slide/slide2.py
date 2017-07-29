"""
Slide puzzle using clicking
"""

import sys
from random import randrange
import urllib.request

from PyQt5 import QtCore, QtGui, QtWidgets

# To show Qt framework messages.
QtCore.qInstallMessageHandler(lambda t, c, m: print(m))


# All possible moves
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# Size of tile, image URL, number of random moves for initial shuffle
S = 100
IMG_URL = 'http://r.ddmcdn.com/s_f/o_1/cx_462/cy_245/cw_1349/ch_1349/w_720/APL/uploads/2015/06/caturday-shutterstock_149320799.jpg'
SHUFFLE_N = 5


class Slide(QtWidgets.QWidget):
    """
    T[r][c]: tiles at row r and column c
    xr, xc: row and colume of empty tile (None)
    """
    
    def __init__(self):
        super().__init__(windowTitle='Slide')
        
        self.T = [[0, 1, 2], [3, 4, 5], [6, 7, None]]
        self.xr, self.xc = 2, 2
        
        # Shuffle initially.
        for _ in range(SHUFFLE_N):
            while True:
                dr, dc = D[randrange(4)]
                if 0 <= self.xr + dr < 3 and 0 <= self.xc + dc < 3:
                    break
            
            tr, tc = self.xr + dr, self.xc + dc
            self.T[self.xr][self.xc], self.T[tr][tc] = self.T[tr][tc], None
            self.xr, self.xc = tr, tc
        
        # Load image.
        self.img = QtGui.QPixmap()
        self.img.loadFromData(urllib.request.urlopen(IMG_URL).read())
        assert self.img.width() > 0 and self.img.height() > 0
    
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        
        # Image size / 3
        iw_3, ih_3 = self.img.width() / 3, self.img.height() / 3
        
        # Draw image segments and frame.
        for r in range(3):
            for c in range(3):
                if self.T[r][c] is not None:
                    # Get image segment position and draw it.
                    ir, ic = self.T[r][c] // 3, self.T[r][c] % 3
                    qp.drawPixmap(c * S, r * S, S, S, self.img,
                                  ic * iw_3, ir * ih_3, iw_3, ih_3)
                
                qp.drawRect(c * S, r * S, S, S)
        
        # Draw reference image at right.
        qp.drawPixmap(3 * S + 50, 0, S * 3, S * 3, self.img)
        
        qp.end()
    
    def mousePressEvent(self, e):
        # Get click position in tiles.
        r, c = e.y() // S, e.x() // S
        
        # Check valid selection.
        if 0 <= r < 3 and 0 <= c < 3 and abs(self.xr - r) + abs(self.xc - c) == 1:
            # Move a tile at (r, c) to (xr, xc).
            self.T[self.xr][self.xc], self.T[r][c] = self.T[r][c], None
            self.xr, self.xc = r, c
            
            # Let Qt redraw tiles.
            self.update()
            
            # Check completed.
            if self.T == [[0, 1, 2], [3, 4, 5], [6, 7, None]]:
                QtWidgets.QMessageBox.information(self, 'Slide', 'Good')


app = QtWidgets.QApplication(sys.argv)

s = Slide()
s.show()

sys.exit(app.exec_())
