Partida

Você deve escrever uma classe para representar um partida entre duas equipes.
O construtor da sua classe deve receber os nomes das duas equipes, a equipe
mandante e a equipe visitante, e inicializar a pontuação das equipes com o
valor zero. 

Essa classe deve ter métodos para atualizar o número de pontos da equipe
visitante e da equipe mandante, não sendo possível diminuir a pontuação
atual de uma equipe.

Por fim, a classe também deve ter um método para imprimir o resultado de
uma partida conforme mostrado no exemplo de saída abaixo.

A entrada de dados começa com o nome da equipe mandante, seguida do nome
da equipe visitante, cada um em uma linha. Em seguida, há um número inteiro
**N** indicando o número de atualizações de pontos. As próximas **N** linhas
contêm uma letra maiúscula, onde *'M'* indica a equipe mandante e *'V'* a visitante,
e um valor inteiro indicando a nova pontuação da equipe correspondente.

Ao final, o seu programa deve imprimir o resultado da partida.
Veja o exemplo de entrada e saída abaixo.


- Exemplo de Entrada

América
ABC
3
M 1
V 2
M 2

- Exemplo de Saída

América 2 x 2 ABC

