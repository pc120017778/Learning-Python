# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 21:50:39 2016

@author: pc
"""

import sys
from PyQt5.QtWidgets import (QWidget,QToolTip,
                             QPushButton,QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',30))
        self.setToolTip('我的QWidget')
        
        btn = QPushButton('按我Press me',self)
        btn.setToolTip('QWidget')
        btn.resize(btn.sizeHint())
        btn.move(100,100)
        
        self.setGeometry(100,100,800,600)
        self.setWindowTitle('hahha')
        self.show()

if __name__ =='__main__':
    app=QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        
        