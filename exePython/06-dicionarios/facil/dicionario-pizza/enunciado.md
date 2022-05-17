Pedidos de Pizzas

Escreva um programa para armazenar os pedidos de pizzas de uma pizzaria.
Cada pizza deve ser um dicionário com as seguintes chaves:
- nome: cujo valor associado deve ser uma string
- preco: cujo valor associado deve ser um valor inteiro
- ingredientes: uma lista com os ingredientes da pizza

O seu programa deve ler os pedidos de pizza do usuário até que o usuário
forneça o valor 'sair' para o nome de uma pizza. 

Cada pedido consiste em três linhas da entrada, onde na primeira linha
temos o nome da pizza, na segunda o preço e na terceira os ingredientes da pizza.

Seu programa deve imprimir uma listagem de todos os pedidos de pizza
seguindo o formato abaixo:


- Exemplo de Entrada

Marguerita
30
queijo tomate manjericão
Palmito
40
queijo palmito azeitona
Frango
35
queijo frango cebola milho
sair

- Exemplo de Saída

Pizzas Pedidas:
Marguerita (R$ 30): \['queijo', 'tomate', 'manjericão'\]
Palmito (R$ 40): \['queijo', 'palmito', 'azeitona'\]
Frango (R$ 35): \['queijo', 'frango', 'cebola', 'milho'\]
