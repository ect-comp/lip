aniversarios = {}

ativo = True
while ativo:
	nome = input()
	if nome == 'sair':
		ativo = False
	else:
		data = input().split()
		aniversarios[nome] = data
	
mes = input()
print(f"Aniversariantes de {mes}")
for pessoa, niver in aniversarios.items():
	if niver[1] == mes:
		print(f"{niver[0]} {pessoa}")
		
