n = int(input())

lista = []
for i in range(n):
	lista.append(input())

unica = []
for elemento in lista:
	if not elemento in unica:
		unica.append(elemento)

print(len(unica))

