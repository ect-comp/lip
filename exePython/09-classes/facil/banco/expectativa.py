class Banco:
	
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.extrato = [saldo_inicial]

    def operacao (self, valor):
        if valor > 0:
            self.deposito(valor)
        else:
            self.retirada(valor)
            
        self.extrato.append(valor)
        
    def deposito (self, valor):
        self.saldo += valor

    def retirada (self, valor):
        self.saldo += valor
	
    def imprimeExtrato (self):
        print(f"Saldo inicial {self.extrato[0]}")
        for i in range(1, len(self.extrato)):
            valor = self.extrato[i]
            if valor > 0:
                print(f"+ {valor}")
            else:
                print(f"- {-valor}")

        print(f"Saldo final {self.saldo}")


banco = Banco(int(input()))

n = int(input())

for i in range(n):
	banco.operacao(int(input()))
    
banco.imprimeExtrato()
