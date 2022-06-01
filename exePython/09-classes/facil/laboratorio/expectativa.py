class Laboratorio:
	
	def __init__(self, nome, capacidade):
		self.nome = nome
		self.capacidade = capacidade
		self.aberto = False
		self.lotacao = 0
		
	def entrar (self, n):
		if self.aberto and self.lotacao + n <= self.capacidade:
			self.lotacao += n
	
	def sair (self, n):
		if self.aberto and self.lotacao >= n:
			self.lotacao -= n
			
	def abrir (self):
		self.aberto = True
		
	def fechar (self):
		self.aberto = False
			
	def imprimeEstado (self):
		estado = 'aberto'
		if not self.aberto:
			estado = 'fechado'
			
		print(f"{self.nome} ({estado}): {self.lotacao} pessoas")


lab = Laboratorio(input(), int(input()))

e = int(input())

for i in range(e):
	entrada = input().split()
	if entrada[0] == 'abrir':
		lab.abrir()
	elif entrada[0] == 'fechar':
		lab.fechar()
	elif entrada[0] == 'entrar':
		lab.entrar(int(entrada[1]))
	elif entrada[0] == 'sair':
		lab.sair(int(entrada[1]))
	else:
		print("Comando inválido")
		break
		
	lab.imprimeEstado()
