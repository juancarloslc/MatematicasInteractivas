#Punto medio entre dos coordenadas
import os, math
while True:
	x1 = float (input ('Ingresa el valor de x1: '))
	y1 = float (input ('Ingresa el valor de y1: '))
	x2 = float (input ('Ingresa el valor de x2: '))
	y2 = float (input ('Ingresa el valor de y2: '))
	xm = (x1+x2)/2
	ym = (y1+y2)/2
	print ('Punto medio: (' + repr(xm) + ',' + repr(ym) + ')')
	print ()
os.system ('pause')