n = int(input())

cidades = []
for i in range(0, n):
	cidades.append(input())

cidades.sort()

for cidade in cidades:
	print(cidade)

