### Linguagem de Programação
#### Funções Recursivas - Exercícios
---

### Exercício 1
#### Função Recursiva: MDC

O Máximo Divisor Comum (MDC) entre 2 números $x$ e $y$
pode ser calculado da seguinte maneira:

- Repetir até que $y$ seja 0:
    - Faça $x$ receber o valor de $y$
    - Faça $y$ receber o valor do resto da divisão de $x$ por $y$
- Ao encerrar, o MDC será $x$

---

### Exercício 1
#### Função Recursiva: MDC

Implemente uma função recursiva que receba como parâmetros de entrada dois
números inteiros e retorne o MDC entre os dois números.

Implemente a função `main` para testar o seu programa,
lendo dois números inteiros do usuário e mostrando o resultado
na tela.

---

### Lista de Presença

<img src="https://chart.apis.google.com/chart?cht=qr&chs=300x300&chld=L%7C1&chl=https%3A%2F%2Fbit.ly%2F3wfVN08" alt="QR Code" border="0" />

<a href="https://bit.ly/3wfVN08"><p style="text-align:center;">https://bit.ly/3wfVN08</p></a>

---

### Exercício 2
#### Função Recursiva: Quantidade de Dígitos de um Número

Cada dígito que compõe um número inteiro pode ser acesso,
da direita para a esquerda, por sucessivas tomadas do resto
do número por 10 e divisões do número por 10.

---

### Exercício 2
#### Função Recursiva: Quantidade de Dígitos de um Número

Implemente uma função recursiva que receba como parâmetros de entrada um
número inteiro e retorne a quantidade de dígitos deste número.

Implemente a função `main` para testar o seu programa,
lendo um número inteiro do usuário e mostrando o resultado
na tela.

---

### Exercício 3
#### Função Recursiva: Produto entre Dois Números

O produto entre dois números $x$ e $y$ pode ser obtido
através de várias somas sucessivas. Por exemplo:

`
\begin{align*} 
2 \times 3 &= 2 + 2 \times 2 \\ 
2 \times 2 &= 2 + 2 \times 1 \\
2 \times 1 &= 2 + 2 \times 0 \\
2 \times 0 &= 0 
\end{align*}
`

---

### Exercício 3
#### Função Recursiva: Produto entre Dois Números

Implemente uma função recursiva que receba como parâmetros de entrada dois
números inteiros e retorne o produto entre os dois números.

Implemente a função `main` para testar o seu programa,
lendo dois números inteiros do usuário e mostrando o resultado
na tela.

---

### Exercício 4
#### Função Recursiva: Divisores de um Número

Implemente uma função recursiva que retorne
a quantidade de divisores de um número.

A função deve ter um único parâmetro de entrada.

Implemente a função `main` para testar o seu programa.

---

### Exercício 4
#### Função Recursiva: Divisores de um Número

Para que esta função contenha apenas um parâmetro
de entrada, utilize uma função auxiliar com dois parâmetros,
que realiza de fato o cálculo da quantidade de divisores:

```C++
//Função auxiliar: 
//calcula a quantidade de divisores.
//Esta função é realmente recursiva
int conta_div(int n, int i){
    //Deixado para o leitor :)
}

//Função com apenas um parâmetro:
//serve de fachada para a função
//auxiliar, que é realmente recursiva
int conta_divisores(int x){
    return conta_div(x, 1);
}
```
---