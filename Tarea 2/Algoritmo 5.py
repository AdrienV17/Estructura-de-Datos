import random
# Algoritmo 5

# 5.Escribir un programa que llene un arreglo de 10 números enteros \
# aleatorios comprendidos entre 50 y 100, copie en otro 
# arreglo esos números multiplicados por 0,5 y muestre ambos arreglos.

arreglo = []

for numero in range(10):
    numero = random.randint(50,100)
    arreglo.append(numero)

arreglo_multiplicado = []
for numero in arreglo:
    numero = numero*0.5
    arreglo_multiplicado.append(numero)

print(f'Arreglo Viejo:{arreglo}')
print(f'Arreglo Multiplicado por 0.5:{arreglo_multiplicado}')
