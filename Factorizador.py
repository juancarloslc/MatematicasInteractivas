print("Calculadora de factores")
a=0
b=2
while True:
		a=int(input("Ingrese un numero a factorizar:"))
		if a==1:
			print(1)
		while a>1:
			if a%b==0:
				print("      ",b)
				a=a/b
				b=2
			else:
				b=b+1