n = 3
turmas = []

for _ in range(n):
    turmas.append(input().split(','))

nome = input()
alguma = False

for turma in turmas:
	if nome in turma:
		alguma = True

if alguma:
	print(f"Tem {nome} em alguma turma")
else:
	print(f"Nenhuma turma tem {nome}")
