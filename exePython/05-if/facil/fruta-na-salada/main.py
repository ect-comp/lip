n = 3
saladas = []

for _ in range(n):
    saladas.append(input().split())

favorita = input()
todas = True

for salada in saladas:
	if not favorita in salada:
		todas = False

if todas:
	print(f"{favorita} aparece em todas as saladas")
else:
	print(f"{favorita} não aparece em todas as saladas")
