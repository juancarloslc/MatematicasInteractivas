#Division de un segmento entre una razón dada
import os, math
while True:
	x1 = float (input ('Ingresa el valor de x1: '))
	y1 = float (input ('Ingresa el valor de y1: '))
	x2 = float (input ('Ingresa el valor de x2: '))
	y2 = float (input ('Ingresa el valor de y2: '))
	m = (y2-y1)/(x2-x1)
	a =  math.degrees(math.atan(m))
	
	print ('pendiente: ' + repr(m) + ' Angulo: ' + repr(a))
	print ()
os.system ('pause')