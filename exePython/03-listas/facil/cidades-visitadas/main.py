n = int(input())

cidades = []
for i in range(0, n):
	cidades.append(input())

cidades.reverse()

for cidade in cidades:
	print(cidade)

