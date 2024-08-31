#Perimetro de poligonos en el plano
import os, math
while True:
	xs = []
	ys = []
	perimetro = 0
	distancia = 0
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
		distancia=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
		perimetro += distancia
	
	print ('perimetro: ' + repr(perimetro))
	print ()
os.system ('pause')