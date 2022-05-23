pizzas = []

while True:
	nome = input()
	if nome == 'sair':
		break
	preco = int(input())
	ingredientes = input().split()
	pizza = { 'nome' : nome, 'preco' : preco, 'ingredientes' : ingredientes }
	pizzas.append(pizza)
	
print("Pizzas Pedidas:")
for pizza in pizzas:
	print(f"{pizza['nome']} (R$ {pizza['preco']}): {pizza['ingredientes']}")
