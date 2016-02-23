#!/usr/bin/python
import sys
import alko
from PyQt4 import QtCore, QtGui
from alkomat_ui import Ui_Dialog

class MyDialog(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.licz_button,QtCore.SIGNAL("clicked()"), self.liczB_dialog)

	def liczB_dialog(self):
		piwo_li = alko.validate(self.ui.Piwo_ilosc.text())
		wino_li = alko.validate(self.ui.Wino_ilosc.text())
		wodka_li = alko.validate(self.ui.Wodka_ilosc.text())
		inne_li = alko.validate(self.ui.Inne_ilosc.text())
		self.ui.Piwo_ilosc.setText(piwo_li)
		self.ui.Wino_ilosc.setText(wino_li)
		self.ui.Wodka_ilosc.setText(wodka_li)
		self.ui.Inne_ilosc.setText(inne_li)
		alko.promile(self.ui)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())
