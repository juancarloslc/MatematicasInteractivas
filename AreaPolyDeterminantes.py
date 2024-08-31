#Area de un poligono por determinantes
import os, math
while True:
	xs = []
	ys = []
	area = 0
	v = int (input('cuantos vertices tiene el poligono? :'))
	for i in range (v):
		print(' Vertice numero ' + repr(i+1))
		x = float (input ('Ingresa el valor de x: '))
		xs.append(x)
		y = float (input ('Ingresa el valor de y: '))
		ys.append(y)
	for  i in range(len(xs)):
		if i == v-1:
			x1 = xs[i]
			x2 = xs[0]
			y1 = ys[i]
			y2 = ys[0]
		else:
			x1 = xs[i]
			x2 = xs[i+1]
			y1 = ys[i]
			y2 = ys[i+1]
		diagonales = (x1*y2)-(y1*x2)
		area += diagonales
	area = area/2
	
	print ('area: ' + repr(area))
	print ()
os.system ('pause')