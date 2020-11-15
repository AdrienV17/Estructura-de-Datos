# Algoritmo #2 

# 2.Escribir un programa que llene un arreglo 
# con los números pares comprendidos entre 1 y 100


arreglo = []

# [0,1,2,3,4,5...,99]
arreglo_lleno = range(100)

# bucle donde se agregan los numeros pares
for numero in arreglo_lleno:
    numero += 1
    if numero%2==0:
        arreglo.append(numero)

print('Numeros pares del 1 al 100')
for numero in arreglo:
    print(numero)