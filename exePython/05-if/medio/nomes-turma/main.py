n = int(input())

nomes = []

for _ in range(n):
    nomes.append(input())

unicos = []

for nome in nomes:
    if nome not in unicos:
        unicos.append(nome)

print(nomes)
print(unicos)

