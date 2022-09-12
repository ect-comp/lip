### Linguagem de Programação
#### Funções - Exercícios
---

### Funções I - Exercícios
#### Exercício 1

Implemente uma função chamada `eh_multiplo`, que
deve receber como parâmetro dois números inteiros
$x$ e $y$.

A função deve retornar verdadeiro se $x$ for múltiplo
de $y$ ou falso caso contrário.

Implemente a função `main`, de forma que ela leia do usuário dois números
inteiros, chame a função e exiba uma mensagem informando se o primeiro
número lido é múltiplo do segundo ou não.

---

### Funções I - Exercícios
#### Exercício 1

Exemplo:
```cpp
Entrada: 18 6
Saída: 18 e multiplo de 6
```

---

### Funções I - Exercícios
#### Exercício 1 - Solução

```C++
bool eh_multiplo(int x, int y);
int main(){
    int num1, num2;
    cout << "Insira o 1o. numero:\n";
    cin >> num1;
    cout << "Insira o 2o. numero:\n";
    cin >> num2;

    if(eh_multiplo(num1, num2) == true){
        cout << num1 << " e multiplo de " << num2 << endl;
    }
    else{
        cout << num1 << " nao e multiplo de " << num2 << endl;
    }
    return 0;
}
bool eh_multiplo(int x, int y){
    return x % y == 0;
}
```
---

### Funções I - Exercícios
#### Exercício 2

Implemente uma função chamada `eh_primo`, que receba como parâmetro um número inteiro.

A função deve retornar verdadeiro caso o número seja primo ou falso
caso contrário.

Implemente a função `main`, de forma que ela leia do usuário um número
inteiro, chame a função e exiba uma mensagem informando se o número
lido é primo ou não.

---

### Funções I - Exercícios
#### Exercício 2

Exemplo:
```cpp
Entrada: 17
Saída: 17 e primo
```

---

### Funções I - Exercícios
#### Exercício 2 - Solução

```C++
bool eh_primo(int x);
int main(){
    int num;
    cout << "Insira um numero inteiro:\n";
    cin >> num;

    if(eh_primo(num) == true){
        cout << num << " e primo\n";
    }
    else{
        cout << num << " nao e primo\n";
    }
    return 0;
}
bool eh_primo(int x){
    int i, cont = 0;

    for(i = 1; i <= x; i++){
        if(x % i == 0){
            cont++;
        }
    }
    return (cont == 2);
}
```
---

### Lista de Presença

<img src="https://chart.apis.google.com/chart?cht=qr&chs=300x300&chld=L%7C1&chl=https%3A%2F%2Fbit.ly%2F3RFDJpZ" alt="QR Code" border="0" />

<a href="https://bit.ly/3RFDJpZ"><p style="text-align:center;">https://bit.ly/3RFDJpZ</p></a>

---

### Linguagem de Programação
#### Exercício 3

Implemente uma função que receba como parâmetro um número inteiro.

A função deve retornar a soma dos dígitos do parâmetro informado.

Implemente a função `main`, de forma que ela leia do usuário um número
inteiro positivo, chame a função e exiba uma mensagem informando a soma
dos dígitos do número lido.

---

### Funções I - Exercícios
#### Exercício 3

Exemplo:
```cpp
Entrada: 10543
Saída: 10543 tem soma igual a 13
```

---

### Funções I - Exercícios
#### Exercício 3 - Solução

```C++
int soma_digitos(int x);
int main(){
    int num, r;
    cout << "Insira um numero inteiro:\n";
    cin >> num;

    r = soma_digitos(x);
    cout << num << " tem soma igual a " << r << endl;

    return 0;
}
int soma_digitos(int x){
    int d, soma = 0;

    while(x > 0){
        d = x % 10;
        soma += d;
        x = x/10;
    }

    return soma;
}
```
---

### Linguagem de Programação
#### Exercício 4

Implemente uma função que receba como parâmetros
dois números inteiros.

A função deve retornar qual o MDC (Máximo Divisor Comum)
entre os dois parâmetros informados.

Implemente a função `main`, de forma que ela leia do usuário dois números
inteiros positivos, chame a função e exiba uma mensagem informando
o MDC entre os dois números lidos.

---