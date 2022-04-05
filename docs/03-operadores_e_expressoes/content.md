### Linguagem de Programação
#### Operadores e Expressões
---

### Linguagem de Programação
- Aula anterior: variáveis e tipos básicos
- Aula de hoje: operadores e expressões
---

### Operadores e Operandos
- Compõem uma _expressão_
- Exemplo:

```C++
x + y
```
- Operador: `+`
- Operandos: `x` e `y`
---
 
### Operadores
Os operadores possuem uma precedência (quem será computado primeiro)
e estão divididos em grupos:
- Operador de atribuição
- Operadores aritméticos
- Operadores relacionais
- Operadores lógicos
---

### Expressões
- Sequências de operandos e operadores que especificam algo
  a ser calculado
- Em C++:
    - Expressões aritméticas
    - Expressões lógicas
---

### Operador de Atribuição
Operador `=` ("recebe")
- Atribui um determinado valor a uma variável
- `x = 0;` lê-se "x recebe zero"
- Sempre: variável à esquerda da atribuição e qualquer outra expressão à sua direita
---

### Operador de Atribuição
- Em sucessivas atribuições, o valor atual sobrescreve o valor antigo
- Exemplo: o que é impresso pelo programa a seguir?

```C++
int main(){
    int x; //declaracao
    x = 0; //atribuicao
    int y = 2, z = 3; //declaracao e inicializacao
    x = y = z; //atribuicao: direita para a esquerda
    cout << x << " " << y << " " << z << endl;
    return 0;
}
```
---

### Operadores Aritméticos
<!-- .slide: class="small_table" -->

- Formam expressões aritméticas: valor resultante é um número
- Operadores de mesma precedência são avaliados da esquerda para a direita

| Operador | Funcionalidade     | Precedência no Grupo |
|----------|--------------------|----------------------|
| ()       | Associar operandos | Primeiro             |
| +        | Adição             | Último               |
| -        | Subtração          | Último               |
| *        | Multiplicação      | Segundo              |
| /        | Divisão            | Segundo              |
| %        | Resto              | Segundo              |
---

### Expressões Aritméticas
Exemplos:
1. `1+2*3`
2. `1*2+3`
3. `(1+2)*3`
4. `1*2%3`
5. `((1*2)+3)*2`
---

### Programa com expressões

```C++
int main(){
    int x = 0;
    x + 45;
    x = x + 100;
    cout << x << endl;
    return 0;
}
```
O programa está sintaticamente correto?
Qual o valor impresso?
---

### Operadores Aritméticos de Atribuição
<!-- .slide: class="small_table" -->

Computam a expressão, aplicam o operador aritmético e atribuem o seu valor à variável à esquerda do op. de atribuição

| Operador | Expressão | Expressão Equivalente |
|----------|-----------|-----------------------|
| +=       | x += y  | x = x + y         |
| -=       | x -= y  | x = x - y         |
| *=       | x *= y  | x = x * y         |
| /=       | x /= y  | x = x/y           |
| %=       | x %= y  | x = x%y           |
---

### Operadores Aritméticos de Atribuição
Qual o valor final das variáveis a seguir, para `x = 1, y = 2, z = 3`?
1. `x += 2*2;`
2. `x += y -= z;`
3. `z %= y %= x;`
---

### Operações de Potência e Raíz Quadrada
- Em C++, não existem operadores para potência e raíz quadrada
- Estas operações são realizadas por chamadas a funções
    - `pow(b,e)` para potência (`b` elevado a `e`)
    - `sqrt(x)` para raíz quadrada de `x`
- Ambas as funções estão na biblioteca `cmath`
```C++
#include &lt;cmath&gt;
```
---

### Operador de Incremento/Decremento
<!-- .slide: class="small_table" -->

Operadores unários (só precisam de um operando)

| Operador      | Expressao | Expressao Equivalente |
|---------------|-----------|-----------------------|
| ++ pre-fixado | ++x       | x = x + 1             |
| ++ pos-fixado | x++       | x = x + 1             |
| -- pre-fixado | --x       | x = x - 1             |
| -- pos-fixado | x--       | x = x - 1             |
---

### Operador de Incremento/Decremento
- Precedência: mais alta do que a multiplicação/divisão/resto
- Diferença entre `++x` e `x++` (o mesmo para `--`):
    - O op. pré-fixado altera o valor primeiro e usa o novo valor na expressão
    - O op. pós-fixado usa o valor na expressão primeiro e só então o altera
- Por exemplo, para `x = 1, y = 2, z = 3`:
    1. `x = ++y;`, `x` recebe 3 e `y` fica igual a 3
    2. `x = y++;`, `x` recebe 2 e `y` fica igual a 3
    3. `x = y++*4;`
---

### Expressões Lógicas
- Expressões que possuem como resultado os valores 0 (falso) ou 1 (verdadeiro)
- Em C++, valores numéricos são interpretados como falso ou verdadeiro
    - O único valor a ser interpretado como falso é o 0
    - Qualquer outro é interpretado como 1 (ex. 1.000001, -10000, etc.)
- Estas expressões são muitas vezes a parte mais importante dos programas
---

### Expressões Lógicas
- Expressões lógicas são formadas por dois tipos de operadores:
    - Operadores relacionais
    - Operadores lógicos
---

### Operadores Relacionais
<!-- .slide: class="small_table" -->

Possuem precedência mais alta do que o operador de atribuição e mais baixa do que os operadores aritméticos

| Operador | Funcionalidade | Precedência no grupo |
|----------|----------------|----------------------|
| ==       | Igual          | Último               |
| !=       | Diferente      | Último               |
| <        | Menor          | Primeiro             |
| <=       | Menor ou igual | Primeiro             |
| >        | Maior          | Primeiro             |
| >=       | Maior ou igual | Primeiro             |
---

### Expressões Lógicas
#### Com Operadores Relacionais
Exemplos:
1. `1 > 2` 
2. `'a' < 'b'`
3. `x == x`
4. `x = 5*2 > 4 == 2+3 > 1`
---

### Operadores Lógicos
<!-- .slide: class="small_table" -->

Possuem precedência mais baixa do que os operadores relacionais (exceto a negação, que tem precedência igual ao op. de incremento)

| Operador | Funcionalidade        | Precedencia no grupo |
|----------|-----------------------|----------------------|
| !        | Negacao (nao logico)  | Primeiro             |
| \|\|     | Disjuncao (ou logico) | Ultimo               |
| &&       | Conjuncao (e logico)  | Segundo              |
---

### Operador Lógico de Negação (Não Lógico)
#### Tabela Verdade
<!-- .slide: class="small_table" -->

Negação: inverte o valor lógico do operando (op. unário)

| x | !x |
|---|----|
| 0 | 1  |
| 1 | 0  |
---

### Operador Lógico de Disjunção (OU Lógico)
#### Tabela Verdade
<!-- .slide: class="small_table" -->

Disjunção: falso quando os dois operandos são falsos

| x | y | x \|\| y |
|---|---|----------|
| 0 | 0 | 0        |
| 0 | 1 | 1        |
| 1 | 0 | 1        |
| 1 | 1 | 1        |
---

### Operador Lógico de Conjunção (E Lógico)
#### Tabela Verdade
<!-- .slide: class="small_table" -->

Conjunção: verdadeiro quando os dois operandos são verdadeiros

| x | y | x && y |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 0      |
| 1 | 0 | 0      |
| 1 | 1 | 1      |
---

### Expressões Lógicas
#### Com Todos os Operadores
Exemplos (para `x = 1, y = 2, z = 3`):
1. `y-x == false`
2. `x > 0 && x < z+10`
3. `z >= y || true`
4. `x != 1 || x != 2`
---

### Expressões Lógicas
#### Exemplo de Expressão Mal Construída
A expressão abaixo é sintaticamente correta
mas é logicamente incorreta.
O que há de errado com ela? Como consertar?

```C++
int i = 3, j = 2, k = 1;
bool expr;

expr = (i > j > k);
```

---

### Expressões Lógicas
#### Exemplo de Expressão Mal Construída
Forma correta da expressão anterior:

```C++
int i = 3, j = 2, k = 1;
bool expr;

expr = (i > j  && j > k);
```

---

### Precedência
#### Ordem geral
1. Parênteses
2. Operador de incremento/não lógico
3. Operadores aritméticos
4. Operadores relacionais
5. Operadores lógicos
6. Atribuição
---

### Verificando o Valor de Expressões Lógicas

Utilize o ```cout``` com a expressão
lógica inteira entre parênteses para
verificar o seu valor em programas:

```C++
int main(){
    int i = 1, j = 2, k = 3;

    cout << (i + j < k || 5 >= k) << endl;

    return 0;
}
```
---

### Conversão de Tipos I
Em C++, o tipo do resultado de uma expressão aritmética é sempre convertido no tipo do operando com maior precisão (com maior capacidade de armazenamento)
---

### Conversão de Tipos I
Exemplo:
```C++
char ch;
int i;
float f;

result = (ch/i) + (f*i); 
```
- `ch/i` é uma expressão com tipo `int`
- `f*i` é uma expressão com tipo `float`
- `(ch/i) + (f*i)` é uma expressão com tipo `float`
- `result` tem portanto tipo `float`
---

### Conversão de Tipos II
Em C++, o tipo da expressão do lado direito de uma atribuição é convertido no tipo do lado esquerdo apenas quando este tem menor precisão
---

### Conversão de Tipos II
Exemplos:
```C++
float g = 9.8;
//valor de g e convertido para int
int x = g;
```
```C++
int x = 3, y = 3, z = 4;
//valor da expressao NAO e convertido para float
float media = (x + y + z)/3;
```
---

### Conversão de Tipos III
Em C++, é possível forçar uma expressão a ser interpretada como um tipo informado
---

### Conversão de Tipos III
Sintaxe do *typecast*: 
```C++
novo_tipo(expressao);
```
ou
```C++
(novo_tipo) expressao;
```
Exemplos:
```C++
int x = 3, y = 3, z = 4;
float media = float(x + y + z)/3;
```
---

### Exercício

Implemente um programa que leia do usuário um caractere.
O programa deve imprimir na tela o número inteiro
da tabela ASCII correspondente ao caractere informado.
Dica: utilize o operador de conversão.

---

### Exercício: Solução
```
#include &lt;iostream&gt;
using namespace std;
int main(){
    char car;
    cout << "insira um caractere:\n";
    cin >> car;
    cout << "Num. ASCII: " << int(car) << endl;
    return 0;
}
```
---

### Exercício

Forneça valores para as variáveis
e calcule os resultados das expressões a seguir.
Implemente um programa para verificar as suas respostas:

```C++
int x, y, z;
char car;

1. car && (x || y)
2. (x > y && y > z) || (x == z)
3. expressao verdadeira quando x nao eh 0 e nem 1
   e y nao eh 0 e nem -1
```
---

### Desafio

Implemente um programa que leia do usuário um número inteiro.
O seu programa deve imprimir na tela o sucessor do número,
exceto se ele for o número 11. Neste caso, o próprio número
deve ser impresso.
**Você não deve utilizar nenhum comando condicional.**
---

### Sumário
Checklist da aula:
- Operador de atribuição
- Operadores aritméticos
- Operadores lógicos
- Operadores relacionais
- Operador de *typecast*
- Expressões aritméticas e lógicas
- Ordem de precedência e avaliação de expressões
---