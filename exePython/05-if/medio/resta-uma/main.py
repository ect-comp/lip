n = int(input())
l1 = []
for i in range(n):
	l1.append(input())

for i in range(1, n):
	if i % 2 != 0: #remove maior elemento
		nomeMaior = l1[0]
		for nome in l1:
			if len(nome) > len(nomeMaior):
				nomeMaior = nome
		l1.remove(nomeMaior)
	else: #remove menor elemento
		nomeMenor = l1[0]
		for nome in l1:
			if len(nome) < len(nomeMenor):
				nomeMenor = nome
		l1.remove(nomeMenor)

print(l1[0])
