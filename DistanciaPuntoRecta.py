#Distancia de un punto a una recta
import os, math
while True:
	x1 = float (input ('Ingresa el valor de x1: '))
	y1 = float (input ('Ingresa el valor de y1: '))
	A = float (input ('Ingresa el valor de A: '))
	B = float (input ('Ingresa el valor de B: '))
	C = float (input ('Ingresa el valor de C: '))
	distancia=(abs((A*x1)+(B*y1)+C))/(math.sqrt((A)*(A)+(B)*(B)))
	print ('Valor de distancia: ' + repr (distancia))
	print ()
os.system ('pause')