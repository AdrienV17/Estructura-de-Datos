# Algoritmo 6

# 6. Escribir un programa que 
# llene un arreglo con los veinte primeros números pares y calcule su suma.

arreglo = []

for numero in range(20):
    if numero%2 == 0:
        arreglo.append(numero)

suma = 0
for numero in arreglo:
    suma += numero

print(f'Arreglo: {arreglo}')
print(f'Suma: {suma}')
