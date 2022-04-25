nota = float(input())
faltas = int(input())

if nota >= 7.0 or (nota >= 5.0 and faltas <= 20):
    print("Aprovado")
elif nota >= 3.0 and faltas <= 20:
    print("Recuperação")
else:
    print("Reprovado")

