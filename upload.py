'''
github.com/razyar
'''

import sys
import os
from PyQt4 import QtCore, QtGui

class QDataViewer(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setGeometry(600, 400, 600, 400)
        self.setWindowTitle('iSpace Platform - Upload')
        self.quitButton = QtGui.QPushButton('Cancel', self)
        self.uploadButton = QtGui.QPushButton('Select', self)
        hBoxLayout = QtGui.QHBoxLayout()
        hBoxLayout.addWidget(self.quitButton)
        hBoxLayout.addWidget(self.uploadButton)
        self.setLayout(hBoxLayout)
        self.connect(self.quitButton,   QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
        self.connect(self.uploadButton, QtCore.SIGNAL('clicked()'), self.open)

    def open (self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        os.system('sudo cp %s /var/www/html/' % filename)

def main():
    app = QtGui.QApplication(sys.argv)
    mw = QDataViewer()
    mw.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
