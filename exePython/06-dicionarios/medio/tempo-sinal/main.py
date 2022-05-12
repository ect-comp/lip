n = int(input())
sinais = []

for i in range(n):
	sinal = input().split()
	sinais.append({
		'estado' : sinal[0],
		'tamanho_fila' : int(sinal[1]),
	})
	
tempos = input().split()
tempo_amarelo = int(tempos[0])
tempo_vermelho = int(tempos[1])
tempo_carro = int(tempos[2])
segundos = 0

for sinal in sinais:
	if sinal['estado'] == 'amarelo':
		segundos = segundos + tempo_amarelo + tempo_vermelho
	elif sinal['estado'] == 'vermelho':
		segundos = segundos + tempo_vermelho
	segundos += sinal['tamanho_fila'] * tempo_carro
		
		
print(f"{segundos} segundos")
