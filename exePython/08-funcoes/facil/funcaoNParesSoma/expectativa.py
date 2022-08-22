def listaPares (n):
    lista = []
    for i in range(2, n + 1, 2):
        lista.append(i)
    return lista

def somaLista (l):
    soma = 0
    for valor in l:
        soma += valor
    return soma


n = int(input())

print(somaLista(listaPares(n)))
