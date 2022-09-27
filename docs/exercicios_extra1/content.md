### Linguagem de Programação
#### Unidade I - Exercícios
---

### Unidade I - Exercícios
#### Exercício 1

Implemente uma função:

- Parâmetro de entrada é um número inteiro $x$
- Parâmetro de saída: total de dígitos de $x$
- Parâmetro de saída: total de dígitos primos de $x$

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

Implemente uma função:

- Parâmetros de entrada: dois números inteiros $p$ e $q$
- Parâmetro de entrada: quantidade de termos da sequência $n$
- Parâmetro de saída: menor valor da sequência
- Parâmetro de saída: maior valor da sequência

Implemente a função main.

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

---

### Unidade I - Exercícios
#### Exercício 3

Implemente uma função:

- Parâmetro de entrada: ângulo x
- Parâmetro de saída: seno de x
- Parâmetro de saída: quantidade de termos que foi utilizada na aproximação 

A função deve somar todos os termos até que o valor absoluto de um termo seja menor do que 0.00001.

---

### Unidade I - Exercícios
#### Exercício 3
<!-- .slide: class="small_table" -->

Por exemplo, para $x = 3.14$, os termos que compõem o somatório na função
são:

| **i:** | **Termo:** | **i:** | **Termo:**   |
|--------|------------|--------|--------------|
| 1      | 3.14       | 11     | -0.00732944  |
| 3      | -5.15986   | 13     | 0.000463239  |
| 5      | 2.54371    | 15     | -2.17493e-05 |
| 7      | -0.597141  | 17     | 7.8838e-07   |
| 9      | 0.0817719  |        |              |

---

### Unidade I - Exercícios
#### Exercício 3

Último termo: 0.000000078838, é menor do que 0.00001,
resultando em 0.00159257 como seno de 3.14 com 9 termos.

---

### Unidade I - Exercícios
#### Exercício 3

A função main do seu programa deve ler um ângulo do usuário, chamar a função e exibir uma mensagem no formato mostrado abaixo.

Exemplo:
```cpp
Entrada: 0.35
Saída: sen 0.350000 = 0.342898 (4 termos)
```

---