Almoço Barato

Você vai comer em um restaurante mas não está com muito dinheiro, então quer
selecionar os pratos do cardápio que cabem no seu orçamento.

Seu primeiro passo é escrever uma função que recebe o nome de prato e o preço dele 
e devolve um dicionário com as chaves **nome** e **valor**.

Em seguida, implemente uma função que recebe uma lista **pratos** com os pratos
do cardárpio, onde cada prato é um dicionário como descrito acima, e o valor máximo que você
deseja pagar. Essa função deve retornar uma lista com os índices dos elementos
de **pratos** cujo valor está dentro do seu orçamento.

A entrada de dados começa com um número inteiro **N**, indicando a
quantidade de pratos. Depois, seguem a descrição de **N** pratos,
onde o nome de um prato é dado em uma linha e o seu valor na próxima linha.

Por fim, vai ser fornecido um valor inteiro que é o valor do seu orçamento.

Use as funções mencionadas anterioremente e ao final imprima a lista
dos pratos que cabem no seu orçamento.

- Exemplo de Entrada

4
Lagosta à Thermidor
99
Filé com fritas
69
Frango Assado
18
Feijoada
25
25

- Exemplo de Saída

Pratos dentro do orçamento
Frango Assado 18
Feijoada 25

