# Algoritmo #3

# 3.Escribir un programa que llene un arreglo con los números comprendidos 
# entre 0 y 100 divisibles por 2


arreglo = []

# [0,1,2,3,4,5...,99]
arreglo_lleno = range(100)

# bucle donde se agregan los numeros pares
for numero in arreglo_lleno:
    numero += 1
    if numero%2==0:
        arreglo.append(numero)

print('Numeros pares del 0 al 100 divisibles por 2')
for numero in arreglo:
    print(numero)