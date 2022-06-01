def cria_lutador (nome, peso):
	return { 'nome' : nome, 'peso' : peso }

def lutadores_desclassificados (lutadores, peso_max):
	desclassificados = []
	for lutador in lutadores:
		if lutador['peso'] > peso_max:
			desclassificados.append(lutador['nome'])

	return desclassificados


lutadores = []
n = int(input())
for i in range(n):
	lutador = input().split()
	lutador = cria_lutador(lutador[0], int(lutador[1]))
	lutadores.append(lutador)

peso_max = int(input())

eliminados = lutadores_desclassificados(lutadores, peso_max)
for eliminado in sorted(eliminados):
	print(eliminado)
