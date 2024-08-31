#Distancia entre dos puntos
import os, math
while True:
	x1 = float (input ('Ingresa el valor de x1: '))
	y1 = float (input ('Ingresa el valor de y1: '))
	x2 = float (input ('Ingresa el valor de x2: '))
	y2 = float (input ('Ingresa el valor de y2: '))
	distancia=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
	print ('Valor de distancia: ' + repr (distancia))
	print ()
os.system ('pause')