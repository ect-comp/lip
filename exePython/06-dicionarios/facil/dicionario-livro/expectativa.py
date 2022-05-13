livro = {
	'titulo' : 'Curso intenstivo de Python',
	'autor' : 'Eric Matthes',
	'preco' : 44.50,
	'capitulos' : [
		{ 'titulo' : 'Introdução', 'paginas' : 9 },
		{ 'titulo' : 'Comando if', 'paginas' : 11},
		{ 'titulo' : 'Dicionários', 'paginas' : 20}
	]
}
	
print(f"titulo = {livro['titulo']}")
print(f"autor = {livro['autor']}")
print(f"preco = {livro['preco']}")
print("Capitulos")
for capitulo in livro['capitulos']:
	print(f"titulo = {capitulo['titulo']}")
	print(f"paginas = {capitulo['paginas']}")
