Laboratório

Você deve escrever uma classe para representar um laboratório.
Essa classe deve ter campos para representar o nome do laboratório, se ele
está aberto ou não, a capacidade máxima do laboratório e a sua lotação atual.

O construtor da sua classe deve receber o nome do laboratório e a sua capacidade
máxima. Inicialmente o laboratório deve estar fechado e sem ninguém.

Essa classe deve ter métodos para abrir/fechar o laboratório e para as
pessoas entrarem/saírem do laboratório. Somente é possível entrar//sair do
laboratório quando ele está aberto. Você deve guarantir que a lotação atual
do laboratório seja sempre válida.

Por fim, sua classe também deve ter um método para imprimir o estado atual
do laboratório, conforme mostrado abaixo.

A entrada de dados começa com uma linha contendo o nome do laboratório, seguida
de uma linha com a capacidade máxima do laboratório. Depois há um número inteiro
**E** indicando uma quantidade de eventos. Cada evento é fornecido em uma linha
separada e pode possuir um dos seguintes formatos:
- 'abrir': abre o laboratório
- 'fechar': fecha o laboratório
- 'entrar' **N**: indica que **N** pessoas querem entrar no laboratório. Isso só
é possível se o laboratório estiver aberto e a entrada dessas pessoas não extrapolar
a lotação do laboratório. Caso não haja espaço para as **N** pessoas que desejam entrar,
então ninguém entra.
- 'sair' **N**: indica que **N** pessoas querem sair do laboratório. Isso só é
possível se o laboratório estiver aberto e houver **N** pessoas dentro do laboratório.
Se há menos do que **N** pessoas no laboratório, então ninguém sai.


Após cada evento, o seu programa deve imprimir o estado atual do laboratório.
Veja o exemplo de entrada e saída abaixo.


- Exemplo de Entrada

Lab Info
4
5
abrir
entrar 3
entrar 3
fechar
sair 1

- Exemplo de Saída

Lab Info (aberto): 0 pessoas
Lab Info (aberto): 3 pessoas
Lab Info (aberto): 3 pessoas
Lab Info (fechado): 3 pessoas
Lab Info (fechado): 3 pessoas
