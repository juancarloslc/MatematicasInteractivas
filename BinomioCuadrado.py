import random
import string

numero = random.randint(1, 16)
print(numero)
letra = random.choice(string.ascii_lowercase)
print(letra)

print("     ",letra,"²+",2*numero,letra,"+",numero*numero)