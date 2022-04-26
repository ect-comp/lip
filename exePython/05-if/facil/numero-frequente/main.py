n = 3
numeros = []

for _ in range(n):
    numeros.append(input().split())

frequente = input()
contador = 0

for numero in numeros:
	if frequente in numero:
		contador = contador + 1

if contador == n - 1:
	print(f"{frequente} é um número frequente")
else:
	print(f"{frequente} não é um número frequente")
