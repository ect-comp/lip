pizzas = []
n = int(input())

for i in range(n):
	nome = input()
	preco = int(input())
	ingredientes = input().split()
	pizza = { 'nome' : nome, 'preco' : preco, 'ingredientes' : ingredientes }
	pizzas.append(pizza)
	
x = input()
	
achou = False
nome = ''
preco = 0

for pizza in pizzas:
	if x in pizza['ingredientes']:
		achou = True
		preco = min(preco, pizza['preco'])
		nome = pizza['nome']
		
if achou:
	print(nome)
else:
	print(f"Nenhuma pizza tem {x}")
