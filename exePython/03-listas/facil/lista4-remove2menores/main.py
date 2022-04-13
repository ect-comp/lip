numeros = []

numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))

numeros.remove(min(numeros))
numeros.remove(min(numeros))

for numero in numeros:
	print(numero)


