Tempo no Sinal

Você está indo para a universidade de ônibus e deseja estimar o
tempo que o ônibus vai ficar parado nos sinais. Para fazer essa
estimativa, você deve se basear em uma série de informações sobre
os sinais de trânsito.

As informações sobre um sinal de trânsito devem ser representadas como
um dicionário com os seguintes campos:
- estado: indica a cor do sinal, que pode ser 'vermelho', 'verde' ou 'amarelo'
- tamanho\_fila: indica o número de carros que estão na sua frente pra passar o sinal


O seu programa deve ler um valor inteiro **N** e em seguida ler as
informações sobre **N** sinais, onde os dados de um sinal são fornecidos
em uma linha, separados por espaços, seguindo o formato:
Estado Tamanho\_Fila

Em seguida, o seu programa deve ler três valores inteiros, que indicam,
respectivamente, o tempo em segundos que leva para:
	- um sinal amarelo ficar vermelho
    - um sinal vermelho ficar verde
    - um carro que está na sua frente atravessar o sinal


Assuma que o ônibus somente pode atravessar um sinal verde.
Para atravessar um sinal, é necessário esperar todos os carros
na frente do ônibus atravessarem o sinal. Assuma que se um
sinal está verde, sempre é possível passar por ele antes de
ele fechar.


- Exemplo de Entrada

3
verde 2
amarelo 3
vermelho 0
1 5 2


- Exemplo de Saída

21 segundos

No exemplo acima, o primeiro sinal está verde, então o tempo gasto nele
será somente o tempo dos dois carros na frente do ônibus atravessarem o
sinal (2 * 2 = 4 segundos). O segundo sinal está amarelo, então o tempo
gasto nele será o tempo de esperar o sinal ficar vermelho, mais o tempo do
sinal vermelho ficar verde, mais o tempo dos 3 carros na frente do ônibus
passarem o sinal (1 + 5 + (2 * 3) = 12 segundos). O terceiro sinal está
vermelho e o ônibus vai demorar apenas 5 segundos para atravessá-lo, já
que não há nenhum carro na frente. No total, o ônibus vai demorar
4 + 12 + 5 = 21 segundos para atravessar todos dos sinais.

