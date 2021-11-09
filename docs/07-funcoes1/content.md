### Linguagem de Programação
#### Funções I
---

### Objetivo da Aula
- Motivar o uso de funções
- Apresentar as construções oferecidas em C++ para a implementação de programas
  com funções
---

### Função
- Variáveis guardam valores de diferentes tipos
    - `char`, `int`, `float`, `bool`
- E se pudéssemos atribuir não um valor, mas sim, _um trecho de código a um nome_,
  similar a uma variável?
- Isto é exatamente o que acontece com funções em linguagens de programação
---

### Função
- Função: conjunto de comandos (trecho de código) que juntos, desempenham uma tarefa em particular
- Uma função também pode ser chamada de subprograma
- Cada função recebe um nome e através deste, pode ser executada (chamada)
- Uso de funções organiza, simplifica e reduz programas
---

### Função
Exemplos de funções conhecidas: 
1. `sqrt`
2. `pow`
3. `sin`
4. `cos`
5. `tan`
6. `rand`
---

### Chamadas de Funções - Exemplo 1
O que faz o seguinte programa?
```C++
int main(){
    int x, r;
    cin >> x;
    r = sqrt(x);
    cout << x << ", " << r << endl;
    return 0;
}
```
---

### Chamadas de Funções - Exemplo 2
O que faz o seguinte programa?
```C++
int main(){
    float x, y;
    cin >> x >> y;
    cout << sin(x)/cos(y) << endl; 
    return 0;
}
```
---

### Programas que Chamam Funções
- Vocês já utilizaram funções em vários programas
- Em outras palavras:
    - Você enquanto programador foi _usuário de funções_
      implementadas por outro programador
    - O seu programa continha _chamadas_ de funções
- A chamada de uma função funciona exatamente como uma variável
    - Contém um valor que pode ser usado em expressões
---

### Programas que Chamam Funções
- Principal vantagem de chamar funções:
  **não é necessário saber como uma função está implementada para utilizá-la**
- Exemplo: função `cos(x)` computa o cosseno de `x` com o polinômio
  de MacLaurin:
`
\begin{equation*}
cos(x) = \sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n)!}x^{2n}
\end{equation*}
`
---

### Implementação de Funções
- Linguagens de programação estruturadas oferecem uma sintaxe para implementação de funções
- Entretanto, além da sintaxe, é preciso saber:
1. As entradas necessárias do subprograma (_parâmetros_ ou argumentos da função)
2. Como o subprograma deve operar (código da função)
3. O que o subprograma deve computar (saída da função)
---

### Implementação de Funções
> A implementação de uma função é dividida entre a sua _assinatura_
> e as instruções que compõem a sua _definição_
---

### Assinaturas de Funções
Sintaxe:
```
tipo_da_funcao nome_da_funcao(lista de parametros);
```
- Também chamadas de cabeçalhos ou protótipos da função
- Devem estar antes da função `main`
- `tipo_da_funcao` é o tipo do valor computado pela função:
  `int, char, float, bool` ou o novo tipo `void`
- `nome_da_funcao` segue as mesmas regras que usamos para nomear variáveis
- `lista de parametros` são variáveis das quais a função **depende** para computar o seu retorno
    - Devem ser declaradas com o tipo e nome de cada parâmetro, sendo cada
      parâmetro separado por vírgula
---

### Assinaturas de Funções
#### Exercício
Escrever assinaturas para as funções abaixo:
1. `sqrt`
2. `sin`
3. `pow`
4. `rand`
5. Função que converte temperatura em graus Celsius para Fahrenheit
6. Função que converte um número no caractere da tabela ASCII correspondente
7. Função que retorna o menor dentre três números reais
8. Função que retorna verdadeiro caso o número seja primo e falso caso contrário
---

### Assinaturas de Funções
#### Exercício: Solução
```
float sqrt(float x);
float sin(float x);
float pow(float b, float e);
int rand();
float converte_temp(float c);
char converte_caractere(int cod);
float menor(float a, float b, float c);
bool eh_primo(int num);
```
---

### Assinaturas de Funções
- A assinatura de uma função define uma relação entre suas entradas e sua saída
- Entrada:
    - Parâmetros da função
- Saída:
    - Tipo da função
- Observações:
    - Algumas funções não necessitam de entrada
    - É possível utilizar parâmetros da função para armazenar saída (próximas aulas)
---

### Definição de Funções
Sintaxe:
```
tipo_da_funcao nome_da_funcao(lista de parametros){
    corpo da funcao
}
```
- Uma função é definida quando programamos o seu comportamento com instruções válidas (`corpo da funcao`)
- A definição de uma função deve vir após a função `main`
---

### Definição de Funções
Exemplo:
Programa que converte temperatura em graus Celsius para Fahrenheit, sabendo-se que
`
\begin{equation*}
f(c) = 1,8c + 32
\end{equation*}
`
1. Sem usar função
2. Utilizando função
---

### Definição de Funções
Exemplo:
Função que converte temperatura em Celsius para Fahrenheit:
```C++
float converte_temp(float c){
    return 1.8*c + 32;
}
```
---

### Definição de Funções
- A lista de parâmetros define variáveis locais (visíveis somente dentro da função)
- Qualquer instrução é permitida no corpo da função, inclusive
  chamadas a outras funções (ou a ela mesma)
- Comando `return`:
    - Usado junto com qualquer expressão válida em C++
    - Converte a expressão no tipo de retorno da função
    - Termina execução da função e retorna a execução
      do programa para a instrução seguinte
      à chamada
---

### Definição de Funções
Variáveis locais de uma função:
- Variáveis que podem ser declaradas dentro da função
- Não existem fora da função
- Variável local com mesmo nome de outra variável:
  não são as mesmas!
- Cada parâmetro da função também é uma variável local
---

### Definição de Funções
Exemplo anterior com variável local:
```C++
float converte_temp(float c){
    float f;
    f = 1.8*c + 32;
    return f;
}
```
---

### Função `main`
Neste ponto da disciplina, você deve ser capaz de
entender o porquê de todo programa
ter `int main()` e `return 0` :)
---

<!--
### Execução de Funções
#### Exercício
Depure o código a seguir para vários valores de `x`:
```C++
int funcao(int x, int y);
int main(){
    int n1, n2;
    cin >> n1 >> n2;

    cout << funcao(n1, n2) << endl;
    return 0;
}
int funcao(int x, int y){
    if(x < y){
        return x;
    }
    else{
        return y;
    }
}
```
---

### Programas com Funções
#### Exercício
Escrever programas completos para:
1. Ler um caractere digitado pelo usuário e convertê-lo no número de
   acordo com a tabela ASCII, utilizando função.
   Após chamar a função, o número resultante deve ser exibido.
2. Ler três números reais digitados pelo usuário e computar a média entre eles,
   utilizando função.
   Após chamar a função, a média deve ser exibida.
3. Ler um número inteiro digitado pelo usuário e imprimir uma mensagem informando
   se ele é primo, utilizando função.
   Após chamar a função, a mensagem correspondente ("é primo" ou "não é primo")
   deve ser exibida.
---
-->

### Programa com Função
#### Exercício

> Implemente uma função chamada `eh_primo`, que receba como parâmetro um número inteiro.
> A função deve retornar verdadeiro caso o número seja primo ou falso
> caso contrário.

> A função `main` é dada e contém o código do _programa usuário_ da função
> que você deve implementar (slide a seguir).
---

### Programa com Função
#### Exercício: Programa Usuário da Função

```C++
int main(){
    int num;
    cout << "Insira um numero inteiro:\n";
    cin >> num;

    if(eh_primo(num) == true){
        cout << num << " eh primo\n";
    }
    else{
        cout << num << " nao eh primo\n";
    }
    return 0;
}

```
---

### Programa com Função
#### Exercício: Solução

```C++
bool eh_primo(int x);
int main(){
    int num;
    cout << "Insira um numero inteiro:\n";
    cin >> num;

    if(eh_primo(num) == true){
        cout << num << " eh primo\n";
    }
    else{
        cout << num << " nao eh primo\n";
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

### Sumário
Na aula de hoje:
- Chamada de funções
- Assinatura de funções
- Definição de funções
Elementos importantes: 
- Tipo de retorno
- Lista de parâmetros
- Comando `return`
---