#!/usr/bin/python
import sys
from PyQt4 import QtCore, QtGui
def validate(value):
	if len(value)==0:
		value=0
		return QtCore.QString.number(value)
	int_value=int(value)
	if int_value<0:
		value=0
		return QtCore.QString.number(value)
	else:
		return QtCore.QString(value)

def promile(ui):
	sex = ui.plec_wybor.currentIndex()
	height = ui.wzrost.value()
	weight = ui.masa.value()
	drinking_time = ui.czas_picia.value()
	stomach = ui.zoladek_picie.currentIndex()
	drinking_place = ui.gdzie_box.currentIndex()
	try:	
		beer_a = float(ui.piwo_procent.text())
	except:
		beer_a = 0.0
		ui.piwo_procent.setText("0")
	try:
		wine_a = float(ui.wino_procent.text())
	except:
		wine_a = 0.0
		ui.wino_procent.setText("0")
	try:		
		wodka_a = float(ui.wodka_procent.text())
	except:
		wodka_a = 0.0
		ui.wodka_procent.setText("0")
	try:
		other_a = float(ui.inne_procent.text())
	except:
		other_a = 0.0
		ui.inne_procent.setText("0")
	fine = ui.mandat_box.value()
	
