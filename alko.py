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
