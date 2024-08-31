#Division de un segmento entre una razón dada
import os, math
while True:
	x1 = float (input ('Ingresa el valor de x1: '))
	y1 = float (input ('Ingresa el valor de y1: '))
	x2 = float (input ('Ingresa el valor de x2: '))
	y2 = float (input ('Ingresa el valor de y2: '))
	r1 = float (input ('Ingresa el valor de r1: '))
	r2 = float (input ('Ingresa el valor de r2: '))
	xm = (x1+((r1/r2)*x2))/(1+(r1/r2))
	ym = (y1+((r1/r2)*y2))/(1+(r1/r2))
	print ('Punto divisor: (' + repr(xm) + ',' + repr(ym) + ')')
	print ()
os.system ('pause')