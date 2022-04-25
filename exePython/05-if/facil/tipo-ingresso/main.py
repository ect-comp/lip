idade = int(input())
ocupacao = input()

if idade < 10 or idade > 70:
    print("Ingresso gratuito")
elif (idade < 30 and ocupacao == 'estudante') or ocupacao == 'professor':
    print("Ingresso com desconto")
else:
    print("Ingresso normal")

