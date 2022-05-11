n = int(input())
partidas = []

for i in range(n):
	partida = input().split()
	partidas.append({
		'mandante' : partida[0],
		'gols_mandante' : int(partida[1]),
		'gols_visitante' : int(partida[2]),
		'visitante' : partida[3]
	})
	
time = input()
pontos = 0

for partida in partidas:
	if (partida['mandante'] == time and partida['gols_mandante'] > partida['gols_visitante']) or (partida['visitante'] == time and partida['gols_visitante'] > partida['gols_mandante']):
		pontos = pontos + 3
	elif (partida['mandante'] == time or partida['visitante'] == time) and partida['gols_mandante'] == partida['gols_visitante']:
		pontos = pontos + 1
		
		
print(f"{time} tem {pontos} pontos")
