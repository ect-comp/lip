numeros = []

numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))

numeros.remove(min(numeros))
numeros.remove(max(numeros))

print(numeros[0])


