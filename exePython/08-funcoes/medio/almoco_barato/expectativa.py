def cria_prato (nome, valor):
	return { 'nome' : nome, 'valor' : valor }


def seleciona_baratos (pratos, orcamento):
	baratos = []
	for i in range(0, len(pratos)):
		if pratos[i]['valor'] <= orcamento:
			baratos.append(i)
	return baratos


pratos = []
n = int(input())
for i in range(n):
	nome = input()
	valor = int(input())
	prato = cria_prato(nome, valor)
	pratos.append(prato)

orcamento = int(input())
baratos = seleciona_baratos(pratos, orcamento)
print("Pratos dentro do orçamento")
for barato in baratos:
	print(f"{pratos[barato]['nome']} {pratos[barato]['valor']}")
