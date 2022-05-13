alunos = [
	{ 'nome' : 'Joao',  'idade' : 20, 'disciplinas' : ['LiP', 'Calculo I', 'PLE II'] },
	{ 'nome' : 'Maria', 'idade' : 19, 'disciplinas' : ['LoP', 'Fisica I', 'CTS'] },
	{ 'nome' : 'Rosa',  'idade' : 32, 'disciplinas' : ['VGA', 'Fisica I', 'Química'] },
]
	
for aluno in alunos:
	for chave, valor in aluno.items():
		print(f"{chave} = {valor}")
	print("")
		
