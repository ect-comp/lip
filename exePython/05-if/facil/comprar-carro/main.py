cor = input()
preco = int(input())

if cor == 'amarelo':
    print("Vai comprar")
elif (cor == 'azul' or cor == 'verde') and preco <= 20:
    print("Vai comprar")
else:
    print("Não vai comprar")

