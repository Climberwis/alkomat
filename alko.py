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

#################################################
def promile(ui):
	info_dictio=promile_info(ui)
	alco_dictio=promile_alco(ui)
	if info_dictio['sex'] == 0:
		promile_man(info_dictio, alco_dictio)
	else:
		promile_woman(info_dictio, alco_dictio)

#################################################
def promile_info(ui):
	sex = ui.plec_wybor.currentIndex()
	height = ui.wzrost.value()
	weight = ui.masa.value()
	d_time = ui.czas_picia.value()
	stomach = ui.zoladek_picie.currentIndex()
	d_place = ui.gdzie_box.currentIndex()
	fine = ui.mandat_box.value()
	info_dictio = {'sex':sex, 'height':height, 'weight':weight, 'drinking_time': d_time, 'stomach': stomach, 'drinking_place': d_place, 'fine': fine}
	return info_dictio

#################################################	
def promile_alco(ui):
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
	beer_q = float(ui.Piwo_ilosc.text())
	wine_q = float(ui.Wino_ilosc.text())
	wodka_q = float(ui.Wodka_ilosc.text())
	other_q = float(ui.Inne_ilosc.text())
		
	alco_dictio = {'beer_q': beer_q, 'beer_a': beer_a, 'wine_q': wine_q, 'wine_a': wine_a, 'wodka_q': wodka_q, 'wodka_a': wodka_a, 
'other_q': other_q, 'other_a': other_a}
	return alco_dictio

#################################################
def promile_man(info_dictio, alco_dictio):
	mass=fluid_mass(0.7,0.9, info_dictio)
	alco_mass = alco_m(alco_dictio)
	alco_time = alco_t(alco_mass, info_dictio) #ile alko wchlania sie na 1 min
	dealco_time = dealco_t(alco_mass)

#################################################
def promile_woman(info_dictio, alco_dictio):
	mass=fluid_mass(0.6,0.85, info_dictio)
	alco_mass = alco_m(alco_dictio)
	alco_time = alco_t(alco_mass, info_dictio)


#################################################
def fluid_mass(x,y, info_dictio):
	ideal=(info_dictio['height']-100)*y
	if info_dictio['height'] > ideal:
		fluid = x*ideal + 0.2*(info_dictio['weight'] - ideal)
	else:
		fluid = x*ideal - 0.2*(info_dictio['weight'] - ideal)
	return fluid

#################################################
def alco_m(alco_dictio):
	beer_alco = alco_dictio['beer_a']*alco_dictio['beer_q']/100
	wine_alco = alco_dictio['wine_a']*alco_dictio['wine_q']/100
	wodka_alco = alco_dictio['wodka_a']*alco_dictio['wodka_q']/100
	other_alco = alco_dictio['other_a']*alco_dictio['other_q']/100
	alco = beer_alco + wine_alco + wodka_alco + other_alco
	alco *= 0.789
	return alco

#################################################
def alco_t(alco_mass, info_dictio):
	dalco_dtime_drink = alco_mass/(60*drink_t(info_dictio))
	return dalco_dtime_drink

#################################################
def dealco_t(alco_mass):
	time = 0.5
	mass = alco_mass
	while mass > 0:
		if mass > 5.8:
			time +=0.25
			mass = mass - 0.25*(10*mass)/(4.2+mass)
		else:
			time +=0.5
			mass = 0

#################################################
def drink_t(info_dictio):
	drink_time = info_dictio['drinking_time'] + 0.5 + info_dictio['stomach']
	return drink_time
