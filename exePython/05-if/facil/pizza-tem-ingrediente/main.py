ingredientes = []

for _ in range(4):
    ingredientes.append(input())

ingrediente = input()

if ingrediente in ingredientes:
    print(f"Pizza já tem {ingrediente}")
else:
    print(f"Colocando {ingrediente} na pizza")

