l = int(input())
pizzas = []

for i in range(0, l):
	pizzas.append(input().split())

n = int(input())

novas = []
for pizza in pizzas:
	nova = []
	tamanho_pizza = len(pizza)
	if tamanho_pizza >= n:
		for ingrediente in pizza:
			if len(ingrediente) > n:
				nova.append(ingrediente)
	else:
		nova.append(pizza[0])
		nova.append(pizza[-1])
			
	novas.append(nova)

for nova in novas:
	print(nova)

