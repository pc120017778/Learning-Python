# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 21:24:08 2016

@author: pc
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class My_first(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(100,600,800,600)
        self.setWindowTitle('图标')
        self.setWindowIcon(QIcon('web.png'))
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    fistui = My_first()
    sys.exit(app.exec_())
