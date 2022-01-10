### Linguagem de Programação
#### Funções e Vetores
---

### Na Aula Anterior

Matrizes em C++
- Declaração
- Acesso aos elementos
- Inicialização
- Exercícios
---

### Objetivo da Aula
Introduzir o uso de funções que operam sobre matrizes
- Sintaxe
- Exercícios
---

### Funções e Matrizes
>>> É possível passar matrizes como parâmetro de funções
- Útil para realizar blocos de código repetitivos ou para a construção de programas maiores
---

### Funções e Matrizes
Além da matriz a ser passada como parâmetro, é necessário:
- Passar outros dois parâmetros, relativos ao número de linhas e colunas da matriz
- A sintaxe para matrizes tem uma diferença sutil em relação à sintaxe utilizada com vetores
---

### Função com Matrizes
#### Matrizes para Uso em Funções
Para passar matrizes como parâmetros de funções em C++, é necessário:
1. A declaração de uma constante global com o número máximo de linhas/colunas de uma matriz (constante `MAX`, inicializada com um número grande)
2. Que todas as matrizes do programa sejam declaradas com esta constante no número de linhas e colunas
3. Informar no protótipo da função que cada matriz passada como parâmetro tem
`MAX` colunas
---

### Função com Matrizes
#### Matrizes para Uso em Funções
- Isto acontece por causa de uma limitação da linguagem C++, que exige que o número de colunas de uma matriz passada como parâmetro seja constante
- Os programas implementados podem não usar todas as `MAX` linhas e `MAX` colunas das matrizes
---

### Função com Matrizes
#### Matrizes para Uso em Funções - Função `main`
O programa declara matriz com tamanho máximo 100 x 100, mas usa
`nl` x `nc` elementos
```C++
const int MAX = 100;
int main(){
    int mat[MAX][MAX], nl, nc, i, j;
    cin >> nl >> nc;

    for(i = 0; i < nl; i++){
        for(j = 0; j < nc; j++){
            cin >> mat[i][j];
        }
    }

    return 0;
}
```

A linha `const int MAX = 100;` é equivalente a<br>
`\#define MAX 100`
---

### Declaração de Função com Matrizes
#### Sintaxe
Exemplo com uma matriz como parâmetro:
```C++
tipo_func nome_func(tipo_matriz nome_matriz[][MAX],
                    int n_linhas, int n_cols){
    corpo da funcao
}
```
---

### Declaração de Função com Matrizes
#### Sintaxe
Em relação às declarações de funções usadas anteriormente:

- `tipo_matriz` é o tipo da matriz passada como parâmetro:<br>
  `int, char, float, bool`.
- `nome_matriz` é o nome da matriz passada como parâmetro. Observe que o
  primeiro `[]` é em branco e o segundo `[]` deve ter
  obrigatoriamente o nr. máximo de colunas (no caso, `MAX`)
- `n_linhas` é número de linhas da matriz
- `n_cols` é número de colunas da matriz
---

### Declaração de Função com Matrizes
Caso haja mais de uma matriz, é necessário utilizar parâmetros que indiquem o número de linhas e colunas de cada uma delas
---

### Declaração de Função com Matrizes
#### Exercícios
Escrever assinatura da função:
1. Que imprime uma matriz de inteiros na tela
2. Que recebe uma matriz de caracteres e retorna quantos dos elementos na matriz são iguais a um caractere passado como parâmetro
3. Que recebe duas matrizes de inteiros de mesmo tamanho e retorna o maior valor dentre todos, seja ele da primeira ou da segunda matriz
---

### Declaração de Funções com Matrizes
#### Exercícios: Solução
```C++
void imprime_matriz(int mat[][MAX], int nl, int nc);
int conta_ocorrencias(char mat[][MAX], int nl, int nc,
                      char c);
int computa_maior(int mat1[][MAX], int mat2[][MAX],
                  int nl, int nc);
```
---

### Funções com Matrizes
#### Chamada de Funções
Nas chamadas às funções, matrizes são passadas
como parâmetros utilizando apenas o seu nome (sem colchetes).
Exemplo:
```C++
const int MAX = 100;
void imprime_mat(int mat[][MAX], int nl, int nc);
int main(){
    int m[MAX][MAX], i, j, nl = 2, nc = 4;
    for(i = 0; i < nl; i++){
        for(j = 0; j < nc; j++){
        m[i][j] = nc*i+j+1;
        }
    }
    imprime_mat(m, nl, nc);
    return 0;
}
```
---

### Funções com Matrizes
#### Passagem de Parâmetros
- Toda matriz passada para funções como parâmetro
  é passada por **referência**
- Isto significa dizer que as alterações realizadas nas
  matrizes se tornam visíveis fora do corpo da função
---

### Funções com Matrizes
#### Linhas de uma Matriz como Vetores
Funções que aceitam um vetor como parâmetro
aceitam que uma linha da matriz seja passada na sua chamada.
Exemplo:

```C++
void imprime_vet(int v[], int n);
int main(){
    int nl, nc, i, j, mat[MAX][MAX];
    ...
    imprime_vet(mat[0], nc); //vetor linha 0 da matriz mat
}
```
---

### Exercícios:
Implemente as definições das funções:
1. Que imprime uma matriz de inteiros na tela
2. Que recebe uma matriz de caracteres e retorna quantos dos elementos na matriz são iguais a um caractere passado como parâmetro
3. Que recebe duas matrizes de inteiros de mesmo tamanho e retorna o maior valor dentre todos, seja ele da primeira ou da segunda matriz
---

### Sumário
Na aula de hoje:
- Sintaxe de implementação de funções com vetores e matrizes
- Exercícios
---