#!/usr/bin/python
import sys
from PyQt4 import QtCore, QtGui

from alkomat_ui import Ui_Dialog

class MyDialog(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.licz_button,QtCore.SIGNAL("clicked()"), self.liczB_dialog)
		
	def liczB_dialog(self):
		print "DUPA"



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())
