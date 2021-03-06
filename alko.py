#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
def validate(value):
	try:
		if len(value)==0:
			value=0
			return QtCore.QString.number(value)
		float_value=float(value)
		if float_value<0:
			value=0
			return QtCore.QString.number(value)
		else:
			return QtCore.QString(value)
	except:
		return QtCore.QString("0")

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
		if beer_a > 100:
			beer_a = 100
			ui.piwo_procent.setText("100")
	except:
		beer_a = 0.0
		ui.piwo_procent.setText("0")
	try:
		wine_a = float(ui.wino_procent.text())
		if wine_a > 100:
			wine_a = 100
			ui.wino_procent.setText("100")
	except:
		wine_a = 0.0
		ui.wino_procent.setText("0")
	try:		
		wodka_a = float(ui.wodka_procent.text())
		if wodka_a > 100:
			wodka_a = 100
			ui.wodka_procent.setText("100")
	except:
		wodka_a = 0.0
		ui.wodka_procent.setText("0")
	try:
		other_a = float(ui.inne_procent.text())
		if other_a > 100:
			other_a = 100
			ui.inne_procent.setText("100")
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
	money = money_f(alco_dictio, info_dictio)
	alco_p(alco_mass, info_dictio, mass, money)

#################################################
def promile_woman(info_dictio, alco_dictio):
	mass=fluid_mass(0.6,0.85, info_dictio)
	alco_mass = alco_m(alco_dictio)
	money = money_f(alco_dictio, info_dictio)
	alco_p(alco_mass, info_dictio, mass, money)


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
def money_f(alco_dictio, info_dictio):
	if  info_dictio['drinking_place'] == 0:
		x = 1
	elif info_dictio['drinking_place'] == 1:
		x = 1.5
	elif info_dictio['drinking_place'] == 2:
		x = 4
	beer_money = x*3*alco_dictio['beer_q']/500
	wine_money = x*12*alco_dictio['wine_q']/700
	wodka_money = x*20*alco_dictio['wodka_q']/500
	other_money = x*15*alco_dictio['other_q']/500
	fine_money = info_dictio['fine']
	money = beer_money + wine_money + wodka_money + other_money + fine_money
	return money

#################################################
def alco_p(alco_mass, info_dictio, mass, money):
	if alco_mass == 0:
		message_box(0, 0, 0, 0, 0)
		return
	promile = 0.0
	drink_time = 0.25
	full_time = 0.25
	max_promile = 0.0
	time = drink_t(info_dictio)
	dalco_dtime_drink = alco_mass/(4*time)
	alco = dalco_dtime_drink
	promile = alco/mass
	while promile>0:
		if drink_time < time:
			drink_time += 0.25
			alco += dalco_dtime_drink
		if alco >= 5.8:
			alco = alco - 0.25*(10*alco)/(4.2+alco)
		else:
			alco -= 1.5
		full_time += 0.25
		promile = alco/mass
		if drink_time == time:
			drink_time +=0.5	
			max_promile = promile
		if promile < 0:
			promile = 0
	full_time-=time
	message_box(max_promile, money, full_time, alco_mass, time)

#################################################
def message_box(max_promile, money, full_time, alco_mass, time):
	workin_day = (160*money/3100)/8
	message = QtGui.QMessageBox()
	detailed_string = 'Spożyłeś '  + str("%.2f" % round(alco_mass,2)) + ' g czystego alkoholu.\n'
	detailed_string += 'Będziesz trzeźwieć ' + str(full_time) + ' godzin od zakończenia picia.\n' 
	detailed_string += 'Najwyższą zawartość alkoholu we krwi miałeś w ' +str(time) + ' h od rozpoczęcia picia i wynosiła ona ' 
	detailed_string += str("%.2f" % round(max_promile,2)) + ' promili .\n'
	detailed_string += 'Na picie wydałeś ok. ' + str(money) + 'PLN, przeciętnie obywatel Polski potrzebuje na to pracować ok. ' 
	detailed_string += str("%.2f" % round(workin_day,2)) + ' dni.'
	detailed_string1 = detailed_string.decode('utf8')
	message.setText(detailed_string1)
	message.exec_()
#################################################
def drink_t(info_dictio):
	drink_time = info_dictio['drinking_time'] + 0.5 + info_dictio['stomach']
	return drink_time
