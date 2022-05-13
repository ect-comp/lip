### Linguagem de Programação
#### Funções Recursivas - Exercícios
---

### Exercício 1
#### Função Recursiva: MDC

O Máximo Divisor Comum (MDC) entre 2 números $x$ e $y$
pode ser calculado da seguinte maneira:

- Repetir até que $y$ seja 0:
    - Faça $x$ ser igual a $y$
    - Faça $y$ ser igual ao resto da divisão de $x$ por $y$
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

### Exercício 1
#### Função Recursiva: MDC - Solução

```C++
int calcula_mdc(int x, int y){
    if(y == 0){
        return x;
    }
    else{
        return calcula_mdc(y, x%y);
    }
}

int main(){
    int n1, n2;

    cout << "Insira dois nrs. inteiros:\n";
    cin >> n1 >> n2;

    cout << "MDC: " << calcula_mdc(n1, n2) << endl;

    return 0;
}
```
---

### Lista de Presença

<img src="https://chart.apis.google.com/chart?cht=qr&chs=300x300&chld=L%7C1&chl=https%3A%2F%2Fbit.ly%2F3wfVN08" alt="QR Code" border="0" />

<a href="https://bit.ly/3wfVN08"><p style="text-align:center;">https://bit.ly/3wfVN08</p></a>

---

### Exercício 2
#### Função Recursiva: Quantidade de Dígitos de um Número

Implemente uma função recursiva que receba como parâmetros de entrada um
número inteiro e retorne a quantidade de dígitos deste número.

Implemente a função `main` para testar o seu programa,
lendo um número inteiro do usuário e mostrando o resultado
na tela.

---

### Exercício 2
#### Função Recursiva: Quantidade de Dígitos de um Número - Solução

```C++
int conta_digitos(int x){
    if(x < 10){
        return 1;
    }
    else{
        return 1 + conta_digitos(x/10);
    }
}

int main(){

    int num;

    cout << "Insira um nr. inteiro:\n";
    cin >> num;

    cout << num << " possui " << conta_digitos(num) << " digitos\n";

    return 0;
}
```
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

### Exercício 3
#### Função Recursiva: Produto entre Dois Números - Solução

```C++
int calcula_prod(int x, int y){
    if(y == 0){
        return 0;
    }
    else{
        return x + calcula_prod(x, y-1);
    }
}

int main(){
    int n1, n2;

    cout << "Insira dois nrs. inteiros:\n";
    cin >> n1 >> n2;

    cout << "Produto: " << calcula_prod(n1, n2) << endl;

    return 0;
}
```
---

### Exercício 4
#### Função Recursiva: Divisores de um Número

Implemente uma função recursiva que retorne
a quantidade de divisores de um número.

A função deve ter um único parâmetro de entrada.

Implemente a função `main` para testar o seu programa.

---

### Exercício 4
#### Função Recursiva: Divisores de um Número - Solução

```C++
int conta_div(int n, int i){
    //Deixado para o leitor :)
}

//Função com apenas um parâmetro:
//serve de fachada para a função
//que é realmente recursiva
int conta_divisores(int x){
    return conta_div(x, 1);
}

int main(){
    int num;

    cout << "Insira um nr. inteiro:\n";
    cin >> num;

    cout << "Divisores de " << num
         << ": " << conta_divisores(num) << endl;

    return 0;
}
```
---