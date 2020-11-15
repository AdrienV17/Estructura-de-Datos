# Algoritmo 7

# Escribir un programa que solicite cinco números, 
# los almacene en un arreglo y luego calcule la media aritmética de esos números.

arreglo = []

print('Necesitamos 5 numeros para la media aritmetica')

for numero in range(5):
    numero = float(input('Escriba un numero \n'))
    arreglo.append(numero)

suma = 0
for numero in arreglo:
    suma += numero

promedio = suma/5

print(f'Arreglo dado por el cliente:{arreglo}')
print(f'Media Aritmetica:{promedio}')