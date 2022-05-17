doadores = []
total = 0
x = int(input())

ativo = True
while ativo:
	doacao = input().split()
	nome = doacao[0]
	valor = int(doacao[1])
	total += valor
	doadores.append(nome)
	
	if total >= x:
		ativo = False
	
	
print(f"Total arrecadado = {total}")

print("Obrigado")
for doador in sorted(doadores):
	print(doador)
