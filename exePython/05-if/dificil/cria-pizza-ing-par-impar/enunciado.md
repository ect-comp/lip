Cria Pizzas

Paolo quer criar novos sabores de pizza e decidiu usar a seguinte estratégia:
a partir da lista de ingredientes de uma pizza, ele vai selecionar alguns
ingredientes para criar uma nova pizza.

Dada uma lista de pizzas, para as pizzas com pelo menos **N** ingredientes
Paolo vai fazer uma nova pizza utilizando os ingredientes cujo nome tenha
mais de **N** letras. Já para as pizzas com menos do que **N** ingredientes,
Paolo vai fazer uma nova pizza utilizando somente o primeiro e o último ingredientes.

O seu programa deve ler um valor inteiro **L** e em seguida uma lista de **L** pizzas,
cada uma em uma linha, onde cada pizza é formada por uma lista de ingredientes. Em seguida,
seu programa deve ler um valor inteiro **N**.

Seu programa deve imprimir as **L** pizzas que Paolo criou usando a estratégia anterior.

Cada lista de ingredientes será fornecida em uma linha e os ingredientes
serão separados por espaços. Assuma que cada pizza terá pelo menos 2 ingredientes.


- Exemplo de Entrada 1:
3
queijo cogumelo ovos presunto
pimenta milho queijo
queijo mel brócolis pão
4

- Exemplo de Saída 1:
\['queijo', 'cogumelo', 'presunto'\]
\['pimenta', 'queijo'\]
\['queijo', 'brócolis'\]

