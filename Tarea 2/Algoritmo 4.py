import random
# Algoritmo #4

# 4.Escribir un programa que llene un arreglo con 
# cinco números enteros consecutivos y haga una copia de ese arreglo en otro.


arreglo = []

random = random.randint(0,10)

for numero in range(5):
    arreglo.append(random+(numero+1))

arreglo_copia = arreglo


print(f'Arreglo Viejo:{arreglo}')
print(f'Arreglo Copia:{arreglo_copia}')

