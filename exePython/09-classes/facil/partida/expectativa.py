class Partida:
	
	def __init__(self, nome_mandante, nome_visitante):
		self.nome_mandante = nome_mandante
		self.nome_visitante = nome_visitante
		self.pt_mandante = 0
		self.pt_visitante = 0
		
	def atualizaPontuacaoMandante (self, pt):
		if self.pt_mandante <= pt:
			self.pt_mandante = pt
	
	def atualizaPontuacaoVisitante (self, pt):
		if self.pt_visitante <= pt:
			self.pt_visitante = pt
			
	def imprimeResultado (self):
		print(f"{self.nome_mandante} {self.pt_mandante} x {self.pt_visitante} {self.nome_visitante}")


partida = Partida(input(), input())

n = int(input())

for i in range(n):
	entrada = input().split()
	equipe = entrada[0]
	pt = int(entrada[1])
	if equipe == 'M':
		partida.atualizaPontuacaoMandante(pt)
	else:
		partida.atualizaPontuacaoVisitante(pt)
		
partida.imprimeResultado()
