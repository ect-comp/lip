l = int(input())
pizzas = []

for i in range(0, l):
	pizzas.append(input().split())

n = int(input())

novas = []
for i in range(0, l):
	pizza = []
	for ingrediente in pizzas[i]:
		if i % 2 == 0 and len(ingrediente) < n:
			pizza.append(ingrediente)
		elif i % 2 != 0 and len(ingrediente) > n:
			pizza.append(ingrediente)
			
	novas.append(pizza)

for nova in novas:
	print(nova)

