#!/usr/bin/python
import sys
from PyQt4 import QtCore, QtGui
from alkomat_ui import Ui_Dialog

licz=0;

class MyDialog(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.licz_button,QtCore.SIGNAL("clicked()"), self.liczB_dialog)
	def liczB_dialog(self):
		if len(self.ui.Piwo_ilosc.text()) == 0:
			self.ui.Piwo_ilosc.setText("0")
		if len(self.ui.Wino_ilosc.text()) == 0:
			self.ui.Wino_ilosc.setText("0")
		if len(self.ui.Wodka_ilosc.text()) == 0:
			self.ui.Wodka_ilosc.setText("0")
		if len(self.ui.Inne_ilosc.text()) == 0:
			self.ui.Inne_ilosc.setText("0")
		piwo_il = int(self.ui.Piwo_ilosc.text())
		wino_il = int(self.ui.Wino_ilosc.text())
		wodka_il = int(self.ui.Wodka_ilosc.text())
		inne_il = int(self.ui.Inne_ilosc.text())
		if len(self.ui.Piwo_ilosc.text()) == 0:
			self.ui.Piwo_ilosc.setText("0")
		if len(self.ui.Wino_ilosc.text()) == 0:
			self.ui.Wino_ilosc.setText("0")
		if len(self.ui.Wodka_ilosc.text()) == 0:
			self.ui.Wodka_ilosc.setText("0")
		if len(self.ui.Inne_ilosc.text()) == 0:
			self.ui.Inne_ilosc.setText("0")
		if 
		
		print self.ui.plec_wybor.currentIndex()
		print self.ui.czas_picia.value()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())
