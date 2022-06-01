class Biblioteca:
	
	def __init__(self, nome):
		self.nome = nome
		self.catalogo = {}
		
	def adicionar (self, livro):
		self.catalogo[livro] = 'disponível'
		print(f"{livro} adicionado ao catálogo")
	
	def emprestar (self, livro):
		if livro in self.catalogo:
			if self.catalogo[livro] == 'disponível':
				self.catalogo[livro] = 'emprestado'
				print(f"{livro} emprestado")
			else:
				print(f"{livro} já foi emprestado")
		else:
			print(f"{livro} não está no catálogo")
			
	def imprimeCatalogo (self):
		print(self.nome)
		for chave, valor in self.catalogo.items():
			print(f"{chave} ({valor})")
			
			
bib = Biblioteca(input())

n = int(input())

for i in range(n):
	entrada = input().split()
	if entrada[0] == 'adicionar':
		bib.adicionar(entrada[1])
	elif entrada[0] == 'emprestar':
		bib.emprestar(entrada[1])
	elif entrada[0] == 'imprimir':
		bib.imprimeCatalogo()
	else:
		print("Comando inválido")
		break

