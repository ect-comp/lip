### Linguagem de Programação
#### Multiplicação de Matrizes
---

### Multiplicação de Matrizes

Uma operação importante em programação,
que geralmente é parte da solução de problemas computacionais
mais complexos, é a de multiplicar matrizes:

`
\begin{equation*}
    R = A.B
\end{equation*}
`

---

### Multiplicação de Matrizes
#### Dimensões das Matrizes

Lembre-se que, para `$R = A.B$` ser possível:

- `$A$` precisa ter `$n$` colunas
- `$B$` precisa ter `$n$` linhas

Além disso:

- O número de linhas de `$A$` será o número
  de linhas da matriz resultante `$R$`
- O número de colunas de `$B$` será o número
  de colunas da matriz resultante `$R$`

---

### Multiplicação de Matrizes
#### Dimensões das Matrizes

Em outras palavras:

- Sendo `$A$` uma matriz `$M \times N$`
- Sendo `$B$` uma matriz `$N \times O$`

A matriz resultante `$R$` terá tamanho `$M \times O$`

---

### Multiplicação de Matrizes
#### Cálculo do Produto

Podemos relembrar como se calcula `$R = A.B$`
através do seguinte exemplo:

`
\begin{equation*}
    \begin{bmatrix}
    0 & 1 & -1 & 0\\
    2 & 3 &  1 & 1
    \end{bmatrix}
    \begin{bmatrix}
    1 & 1 & 0\\
    0 & 1 & 1\\
    0 & 0 & 2\\
    0 & 0 & 3
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 & 1 & -1\\
    0 & 9 &  8
    \end{bmatrix}
\end{equation*}
`

---

### Multiplicação de Matrizes
#### Cálculo do Produto

Especificamente, observe que a 1a. linha
de `$R$` é dada por: 

`
\begin{align*}
R_{0,0} & = A_{0,0}.B_{0,0} + A_{0,1}.B_{1,0} + A_{0,2}.B_{2,0} + A_{0,3}.B_{3,0}\\
R_{0,1} & = A_{0,0}.B_{0,1} + A_{0,1}.B_{1,1} + A_{0,2}.B_{2,1} + A_{0,3}.B_{3,1}\\
R_{0,2} & = A_{0,0}.B_{0,2} + A_{0,1}.B_{1,2} + A_{0,2}.B_{2,2} + A_{0,3}.B_{3,2}\\
\end{align*}
`

---

### Multiplicação de Matrizes
#### Cálculo do Produto

E a 2a. linha de `$R$` é dada por: 

`
\begin{align*}
R_{1,0} & = A_{1,0}.B_{0,0} + A_{1,1}.B_{1,0} + A_{1,2}.B_{2,0} + A_{1,3}.B_{3,0}\\
R_{1,1} & = A_{1,0}.B_{0,1} + A_{1,1}.B_{1,1} + A_{1,2}.B_{2,1} + A_{1,3}.B_{3,1}\\
R_{1,2} & = A_{1,0}.B_{0,2} + A_{1,1}.B_{1,2} + A_{1,2}.B_{2,2} + A_{1,3}.B_{3,2}\\
\end{align*}
`

---

### Multiplicação de Matrizes
#### Cálculo do Produto

Ou seja, podemos dizer que um valor `$R_{i,j}$`
pode ser calculado pelo seguinte somatório:

`
\begin{equation*}
    R_{i,j} = \sum_{k=0}^{n-1}A_{i,k}B_{k,j},
\end{equation*}
`
onde `$n$` é o número de colunas de `$A$` (e de linhas
de `$B$`)

---

### Lista de Presença

<img src="https://chart.apis.google.com/chart?cht=qr&chs=300x300&chld=L%7C1&chl=https%3A%2F%2Fbit.ly%2F3UddhoR" alt="QR Code" border="0" />

<a href="https://bit.ly/3UddhoR"><p style="text-align:center;">https://bit.ly/3UddhoR</p></a>

---

### Multiplicação de Matrizes
#### Cálculo do Produto

Alternativamente, observe que cada valor `$R_{i,j}$`
é igual ao produto interno entre:

- O vetor linha `$i$` da matriz `$A$`
- O vetor coluna `$j$` da matriz `$B$`

---

### Multiplicação de Matrizes
#### Implementação de Função

A implementação da função para calcular o produto
entre duas matrizes deve:

- Conter duas matrizes como parâmetros de entrada (e as suas dimensões)
- Conter uma matriz como parâmetro de saída (e as suas dimensões)

---

### Multiplicação de Matrizes
#### Implementação de Função

Então, você pode escolher entre duas estratégias:

1. Computar cada valor `$R_{i,j}$` individualmente, utilizando o somatório
2. Para cada valor `$R_{i,j}$`, calcular o produto interno
   entre o vetor linha `$i$` de `$A$` e o vetor coluna `$j$` de `$B$`

---

### Multiplicação de Matrizes
#### Implementação de Função

- As duas formas requerem dois laços para percorrer todas
  as posições `$R_{i,j}$` da matriz resultante
- Para cada `$R_{i,j}$` sendo calculado, você precisará:
    - De outro laço para calcular o somatório (estratégia 1) **ou**
    - De uma chamada a uma função que calcula o produto interno
      entre dois vetores (estatégia 2)

---

### Multiplicação de Matrizes
#### Acessando Vetores de uma Matriz

Um truque pode ser usado para a estratégia 2, tornando
a implementação bem mais fácil:

> Em C++, dada uma matriz `M`, você pode
> utilizar `M[i]` para passar a linha `$i$`
> da matriz para funções que aceitam vetores
> como parâmetro

---

### Multiplicação de Matrizes
#### Acessando Vetores de uma Matriz

Ou seja, cada linha de uma matriz pode
ser passada para a função:

```C++
int produto_interno(int v1[], int v2[], int n);
```

---

### Multiplicação de Matrizes
#### Acessando Vetores de uma Matriz

> Como somente é possível passar vetores linha,
> para passar os vetores coluna da segunda
> matriz, você pode passar os vetores linha da matriz
> transposta

Então:
1. Calcule a transposta da matriz `$B$`
2. Para cada `$R_{i,j}$`, chame a função `produto_interno`
   passando a linha `$i$` de `$A$` e a linha `j$` de `$B^t$`

---

### Multiplicação de Matrizes
#### Exercício 1. Função para Produto de Matrizes

Implemente uma função que receba como parâmetros de entrada duas matrizes de
números inteiros.
A função a ser implementada deve armazenar em um parâmetro de saída a matriz
resultante da multiplicação entre as duas matrizes.

A função main deve ler o tamanho de cada matrizes, cada um dos seus elementos
e exibir na tela a matriz computada pela função.

---

### Multiplicação de Matrizes
#### Exercício 2. Modificação na Função

Ao invés de assumir sempre que a multiplicação
matricial será possível (ou seja, que o nr. de colunas
de `$A$` será igual ao nr. de linhas de `$B$`), modifique
a função, de modo que ela cheque esta condição e retorne
verdadeiro caso a multiplicação possa ser realizada ou
falso caso contrário.

---

### Multiplicação de Matrizes
#### Exercício 3. Informar se Matriz é Ortogonal

Diz-se que uma matriz quadrada `$A$` é ortogonal
se a condição `$A^t.A = I$`, com `$I$` sendo a matriz
identidade, for satisfeita.

Utilizando a função implementada no exercício anterior,
implemente um programa que leia uma matriz quadrada de números
inteiros e informe se tal matriz é ou não ortogonal.

---