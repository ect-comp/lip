### Linguagem de Programação
#### Unidade I - Exercícios
---

### Unidade I - Exercícios
#### Exercício 1

Implemente uma função que receba como parâmetro de entrada um número inteiro $x$.
A função a ser implementada deve armazenar em um parâmetro de saída o total
de dígitos de $x$ e em um segundo, o total de dígitos primos de $x$.

A função main do seu programa deve ler um número inteiro positivo do usuário e
chamar a função implementada, exibindo uma mensagem com o resultado.

---

### Unidade I - Exercícios
#### Exercício 1

Exemplo:
```cpp
Entrada: 1337
Saída: 4 digito(s) sendo 3 primo(s)
```

---

### Lista de Presença

<img src="https://chart.apis.google.com/chart?cht=qr&chs=300x300&chld=L%7C1&chl=https%3A%2F%2Fbit.ly%2F3S9PtRA" alt="QR Code" border="0" />

<a href="https://bit.ly/3S9PtRA"><p style="text-align:center;">https://bit.ly/3S9PtRA</p></a>

---

### Unidade I - Exercícios
#### Exercício 2

Uma sequência $a_0, a_1, a_2,..., a_i, ..., a_{n-1}$
é definida matematicamente por

`
\[
\begin{cases}
    a_0 = p,\\
    a_1 = q,\\
    a_i = a_{i-2} - 3a_{i-1},\\
\end{cases}
\]
`
onde $p$ e $q$, o primeiro e segundo termos da sequência (respectivamente),
são constantes.

---

### Unidade I - Exercícios
#### Exercício 2

Implemente uma função que receba como parâmetro de entrada dois números inteiros $p$ e $q$, denotando o primeiro e segundo termos da sequência, além de um número inteiro $n$, denotando a quantidade de termos da sequência ($n$ será sempre maior que 2).
A função a ser implementada deve armazenar em dois parâmetros de saída
o menor e o maior números entre todos os n termos da sequência.

A função main deve ler do usuário os dois primeiros termos e a
quantidade de termos da sequência, imprimindo na tela em seguida
o menor e o maior termos da sequência, de acordo com o resultado
computado pela função.

---

### Unidade I - Exercícios
#### Exercício 2

Exemplo:
```cpp
Entrada: 3 1 7
Saída: Menor: -33, Maior: 10
```

---

### Unidade I - Exercícios
#### Exercício 3

A função matemática $sen(x)$ pode ser aproximada pela série infinita abaixo:

`
\[
sen(x) = \frac{x^1}{1!}-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}...
\]
`

Implemente uma função que receba como parâmetro de entrada o ângulo x. Esta função deve armazenar em um primeiro parâmetro de saída o seno do ângulo x . Em um segundo parâmetro, a função deve armazenar a quantidade de termos que foi utilizada na aproximação, sabendo que a sua função deve somar todos os termos até que o valor absoluto de um termo seja menor do que 0.00001.

---

### Unidade I - Exercícios
#### Exercício 3

Por exemplo, para $x = 3.14$, os termos que compõem o somatório na função
são:

| i: | Termo:       |
|----|--------------|
| 1  | 3.14         |
| 3  | -5.15986     |
| 5  | 2.54371      |
| 7  | -0.597141    |
| 9  | 0.0817719    |
| 11 | -0.00732944  |
| 13 | 0.000463239  |
| 15 | -2.17493e-05 |
| 17 | 7.8838e-07   |

---

Como o último termo (0.000000078838) é menor do que 0.00001, a função para de calcular o somatório no 9o. termo e calcula 0.00159257 como seno de 3.14.

### Unidade I - Exercícios
#### Exercício 3

A função main do seu programa deve ler um ângulo do usuário, chamar a função e exibir uma mensagem no formato mostrado abaixo.

Exemplo:
```cpp
Entrada: 0.35
Saída: sen 0.350000 = 0.342898 (4 termos)
```

---