### Linguagem de Programação
#### Funções III
---

### Linguagem de Programação
Aulas anteriores:
- Sintaxe em C++ para construção de funções (chamada, assinatura e definição)
- Função com tipo `void`
- Passagem de parâmetro por valor e por referência
---

### Objetivo da Aula
Explorar o conceito de entrada/saída nos parâmetros de funções
---

### Passagem de Parâmetros por Referência
- Uso de operador `&`
- Útil quando:
    - Uma função deve modificar os seus parâmetros
    - _Uma função deve retornar mais de um valor_
---

### Passagem de Parâmetros por Referência
Permite trabalhar com parâmetros:
- _De entrada_: parâmetros necessários para computar a função
- _De entrada e saída_: parâmetros necessários para computar a função e usados para armazenar os resultados da função
- _De saída_: parâmetros usados apenas para armazenar os resultados da função
---

### Passagem de Parâmetros por Referência
#### Exemplo com Parâmetro de Saída
- Parâmetro(s) pode(m) ser usado(s) para armazenar resultado(s) de uma função
- Exemplo: função que converte temperatura em graus Celsius para Fahrenheit,
  armazenando o resultado em um parâmetro de saída

```C++
void converte_temp(float c, float& f){
    f = 1.8*c + 32;
}
```
---

### Passagem de Parâmetros por Referência
#### Exemplo com Parâmetro de Saída
Chamada à função:

```C++
int main(){
    float ce, fa;
    cin >> ce;
    converte_temp(ce, fa);
    cout << "Temp. em Fahrenheit: " << fa << endl;
    return 0;
}
```
---

### Parâmetros de Funções
#### Exemplos
1. Função que gera um número aleatório:
    - `int rand();` `$\rightarrow$` nenhum parâmetro de entrada
2. Função que computa o produto entre dois números inteiros:
    - `int produto(int x, int y);` `$\rightarrow$` 2 parâmetros de entrada
    - `void produto(int x, int y, int& r);` `$\rightarrow$` 2 parâmetros de entrada e 1 de saída
---

### Parâmetros de Funções
#### Exemplos
3. Função que troca o valor de dois números inteiros:
    - `void troca(int& x, int& y);` `$\rightarrow$` 2 parâmetros de entrada e saída, ao mesmo tempo
4. Função que calcula o quociente e resto entre dois números inteiros:
    - `void quoc_resto(int& x, int& y);` `$\rightarrow$` 2 parâmetros de entrada e saída, ao mesmo tempo
    - `void quoc_resto(int x, int y, int& q, int& r);}` `$\rightarrow$` 2 parâmetros de entrada, 2 parâmetros de saída
---

### Funções com Múltiplas Saídas
- Funções com múltiplas saídas são em geral mais complexas
- Dica: dividir o problema
    - Identifique cada saída a ser computada pelo algoritmo
    - Verifique se é melhor implementar uma função auxiliar para calcular cada saída
    - Chame as funções auxiliares dentro da função solicitada
---

### Exercício 1
Implemente uma função que receba como parâmetros de entrada dois números inteiros `$x$` e `$y$`.
A sua função deve armazenar em um primeiro parâmetro de saída o fatorial
de `$x$`, o fatorial de `$y$` em um segundo parâmetro e `$x^y$` em um terceiro.

A função `main` deve ler dois números inteiros entre 0 e 10 do usuário,
passá-los como parâmetro para a função implementada e exibir as três saídas
da função.
---

### Exercício 1: Solução
```C++
int fatorial(int n);
int potencia(int b, int e);
void fat_pot(int x, int y, int& f1, int& f2, int& p);

int main(){
    int n1, n2, r1, r2, r3;
    cout << "Insira dois numeros:\n";
    cin >> n1 >> n2;
    fat_pot(n1, n2, r1, r2, r3);
    cout << "Fatorial1: " << r1 << endl;
    cout << "Fatorial2: " << r2 << endl;
    cout << "Potencia: " << r3 << endl;
    return 0;
}
int fatorial(int n){
    int i, r = 1;
    for(i = 1; i <= n; i++){
        r *= i;
    }
    return r;
}
int potencia(int b, int e){
    int i, r = 1;
    for(i = 1; i <= e; i++){
        r *= b;
    }
    return r;
}
void fat_pot(int x, int y, int& f1, int& f2, int& p){
    f1 = fatorial(x);
    f2 = fatorial(y);
    p = potencia(x, y);
}
```
---

### Exercício 2
A sequência de Collatz, é gerada pelas seguintes regras:
- O termo inicial é um número dado
- Se o termo atual for par, o próximo termo é igual ao atual dividido por dois
- Se o termo atual for ímpar, o próximo termo é igual a três
  vezes o atual mais um
- A sequência é encerrada quando o termo atual é igual a 1

Por exemplo, para um termo inicial igual a 10, a sequência gerada é
`10, 5, 16, 8, 4, 2, 1`.
---

### Exercício 2

Implemente uma função que receba como parâmetro de entrada um
número inteiro positivo denotando o primeiro termo da sequência.
A função a ser implementada deve armazenar em
parâmetros de saída o maior número que faz parte da sequência e também o total
de termos `n` que compõe a sequência.

Implemente a função `main` para testar o seu programa.
---

## Exercício 2: Solução
```C++
void maior_total_collatz(int t_ini, int& maior,
                         int& total);

int main(){
    int val_ini, val_maior, quant;
    cout << "Insira o valor inicial da sequencia:\n";
    cin >> val_ini;
    maior_total_collatz(val_ini, val_maior, quant);
    cout << "Maior valor: " << val_maior << endl;
    cout << "Total de termos: " << quant << endl;
    return 0;
}
void maior_total_collatz(int t_ini, int& maior,
                         int& total){
    int termo = maior = t_ini;
    total = 1;
    while(termo != 1){
        if(termo % 2 == 0){
            termo = termo/2;
        }
        else{
            termo = 3*termo + 1;
        }
        if(termo > maior){
            maior = termo;
        }
        total++;
    }
}
```
---

### Exercício 3
Implemente uma função chamada `imprime_info`,
que imprime na tela se uma letra
passada como parâmetro de entrada é uma vogal ou consoante e também
se ela é maiúscula ou minúscula.

Implemente funções utilitárias `eh_vogal`
e `eh_minuscula` e as use 
para construir a lógica da função `imprime_info`.

Implemente a função `main` para testar o seu programa,
assumindo que o usuário irá sempre digitar uma letra.
---

### Exercício 3: Solução Parcial
```C++
void imprime_info(char c){
    if(eh_vogal(c) && eh_minuscula(c)){
        cout << "Vogal minuscula\n";
    }
    if(!eh_vogal(c) && eh_minuscula(c)){
        cout << "Consoante minuscula\n";
    }
    if(eh_vogal(c) && !eh_minuscula(c)){
        cout << "Vogal maiuscula\n";
    }
    if(!eh_vogal(c) && !eh_minuscula(c)){
        cout << "Consoante maiuscula\n";
    }
}
```
Implemente as funções auxiliares e teste o seu programa.
---

### Sumário
Na aula de hoje:
- Parâmetros de entrada, saída e de entrada e saída
- Funções que chamam outras funções para simplificar a lógica de programas
---