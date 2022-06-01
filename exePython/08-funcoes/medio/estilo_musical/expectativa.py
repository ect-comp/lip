def cria_musica (nome, estilo):
	return { 'nome' : nome, 'estilo' : estilo }

def seleciona_musicas (musicas, estilos):
	selecionadas = []
	for musica in musicas:
		if musica['estilo'] in estilos:
			selecionadas.append(musica['nome'])

	return selecionadas



musicas = []
n = int(input())
for i in range(n):
	nome = input()
	estilo = input()
	musica = cria_musica(nome, estilo)
	musicas.append(musica)

estilos = []
m = int(input())
for i in range(m):
	estilos.append(input())


selecionadas = seleciona_musicas(musicas, estilos)
for musica in selecionadas:
	print(musica)
