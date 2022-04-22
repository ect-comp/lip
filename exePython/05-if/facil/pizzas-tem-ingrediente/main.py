n = int(input())

pizzas = []

for _ in range(n):
    ingredientes = [input(), input(), input()]
    pizzas.append(ingredientes)

ingrediente = input()

contador = 0
for pizza in pizzas:
    if ingrediente in pizza:
        contador = contador + 1

print(contador)

