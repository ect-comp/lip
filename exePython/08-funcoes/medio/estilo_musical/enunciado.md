Seleção de Músicas

Você está fazendo uma seleção musical, onde quer selecionar somente
as músicas de certos estilos musicais.

Para isso, você deve inicialmente criar uma função que
recebe o nome de uma música e o estilo musical dela
e devolve um dicionário com as chaves **nome** e **estilo**.

Em seguida, implemente uma função que recebe as listas **musicas**
e **estilos**, onde os elementos de **musicas** são um dicionário com
os campos **nome** e **estilo**, e os elementos de **estilos**
são nomes de estilos musicais. Essa função deve retornar uma lista com
os nomes das músicas que são de algum estilo presente na lista **estilos**.

A entrada de dados começa com um número inteiro **N**, indicando a
quantidade de músicas. Depois, seguem a descrição de **N** músicas,
onde o nome de uma música é dado em uma linha e o estilo na linha
seguinte.

Em seguida, temos um número inteiro **M** e a descrição de **M**
estilos musicais.

Use as funções mencionadas anterioremente e ao final imprima a lista
de músicas que pertecem a algum dos estilos mencionados.


- Exemplo de Entrada

4
Aquarela
mpb
Asa Branca
forró
Leãozinho
mpb
Índios
rock
3
rock
jazz
mpb

- Exemplo de Saída

Aquarela
Leãozinho
Índios

