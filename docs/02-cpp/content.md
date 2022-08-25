### Linguagem de Programação
#### Introdução à linguagem C++
---

### Objetivos da Disciplina
- Desenvolver a capacidade de implementar algoritmos em uma linguagem de programação estruturada e conceitos relacionados
    - Desenvolver programas com funções e tipos estruturados
    - Linguagem utilizada: **C++**
---

### Programação
Esta capacidade será aplicada na resolução de problemas como:
- Resolução de funções matemáticas (possivelmente com vetores e matrizes)
- Simulação de sistemas
- Processamento de grandes volumes de dados
- etc.
---

### Programação
- Programação envolve:
    1. Compreender o problema a ser resolvido
    2. Elaborar uma sequência de comandos/instruções conhecidos
    3. Escrever um programa na linguagem escolhida em um arquivo chamado código fonte (possui terminação .cpp)
---

### Programação: Processo de Compilação

<img src="compilador.png" width=600/>

- **Compilação**: transformação de código fonte em um programa
- **Código fonte**: formato legível por humanos, formado por
comandos/instruções
- **Programa**: formato legível por máquinas (arquivo binário)
---

### Programação: Representação de um Raciocínio
- Linguagem escolhida tem um formato próprio, denominado sintaxe
- Portanto, aprender programação se resume a:
    1. Dominar a sintaxe da linguagem de programação utilizada
    2. Dominar raciocínio lógico e a sua transcrição em um programa
- Caso esteja sintaticamente correto, o código fonte é compilado em um programa
---

### Programação

Programando na linguagem C++

---

### C++: Primeiro Programa

```C++
int main(){
    return 0;
}
```
---

### C++: Primeiro Programa **Útil** 

```C++
#include &lt;iostream&gt;

using namespace std;

int main(){
    cout << "LiP: programando em C++\n";
    return 0;
}
```
---

### C++: Comando de Saída
- Comando de saída `cout`: imprime na tela o que vem após
  o `<<`
- Isto requer a inclusão da biblioteca `iostream`
(com a diretiva `#include`)
---

### C++: Espaços em Branco

Espaços em branco não alteram o programa:

```C++
#include &lt;iostream&gt;

using namespace std;

int main(){
cout << "LiP: programando em C++\n";
return 0;
}
```

Entretanto, mantenha sempre o seu código indentado
(facilita a leitura)
---

### C++: Comentários de Código

```C++
#include &lt;iostream&gt;

using namespace std;

int main(){
    //A proxima linha imprime uma frase
    cout << "LiP: primeiro programa" << endl;

    /* O proximo comando nao e processado pelo
       compilador, pois e um comentario
       de linha */
    //cout << "ECT/UFRN" << endl;

    return 0;
}
```
---

### C++: Variáveis
- Nomes dados a endereços de memória do computador
- Utilizadas para armazenar valores de diferentes tipos
- Variáveis precisam ser declaradas antes de serem utilizadas

<img src="variaveis.png" width=400/>
---

### C++: Sintaxe de Declaração de Variáveis
```c++
tipo_da_variavel nome_da_variavel;
```
- `tipo_da_variavel` pode ser:
    - `bool`: declara um booleano (verdadeiro ou falso)
    - `int`: declara um número inteiro
    - `float`: declara um número real
    - `char`: declara **um único** caractere
---

### C++: Sintaxe de Declaração de Variáveis
- `nome_da_variavel` deve obedecer às regras:
    1. deve começar com uma letra ou `_` (underline ou underscore)
    2. deve ser composto por letras, dígitos ou `_`
    3. não pode ser uma palavra reservada (p. ex. `if`)
---

### C++: Declaração de Variáveis
#### Exercício

Em um editor de texto, declare variável:
1. Chamada de `x` para armazenar um inteiro
2. Chamada de `temp` para armazenar uma temperatura
3. Para armazenar o resultado de uma média aritmética
4. Para armazenar o sexo de uma pessoa
5. Para armazenar se um motor está ligado ou desligado
---

### C++: Declaração de Variáveis
#### Solução

```
1. int x;
2. float temp;
3. float media;
4. char sexo;
5. bool ligado;
```
---

### Lista de Presença

<img src="https://chart.apis.google.com/chart?cht=qr&chs=300x300&chld=L%7C1&chl=https%3A%2F%2Fbit.ly%2F3pIH7Ut" alt="QR Code" border="0" />

<a href="https://bit.ly/3pIH7Ut"><p style="text-align:center;">https://bit.ly/3pIH7Ut</p></a>

---

### C++: Valor Inicial de Variáveis
O que é impresso no seguinte programa?

```C++
#include &lt;iostream&gt;

using namespace std;

int main(){
    int x;
    cout << "o valor de x e: " << x << endl;
    return 0;
}
```
---

### C++: Inicialização de Variáveis
- Ao serem declaradas em C++, as variáveis são inicializadas com valores aleatórios (lixo em memória)
- C++ oferece o recurso de inicializar uma variável ao mesmo tempo em que ela é declarada
- Por exemplo:
    - `float media = 0;` declara e inicializa a `media` com `0`
    - `char sexo = 'M';` declara e inicializa a `sexo` com `M`
---

## C++: Tipo `char`
- Valores devem ser atribuídos com aspas simples: `'`
- Variáveis `char` armazenam **um único** caractere
    - Letra: `'a'`, `'e'`, `'Z'`, etc.
    - Dígito: `'5'`, `'2'`, etc.
    - Símbolo: `']'`, `'/'`, `';'`, etc.
- Caracteres especiais:
    - `'\n'`: quebra de linha
    - `'\t'`: tabulação horizontal
    - `'\0'`: delimitador de final de cadeia de caracteres
---

### C++: Tipo `char`
- Todo caractere está presente na tabela ASCII (lê-se "ásqui"):
    - Associa um número inteiro diferente para cada caractere
    - [Imagem com a tabela](http://www.jimprice.com/ascii-0-127.gif)
---

### C++: Tipo `char`
- Não se decora a tabela ASCII, mas é importante saber que:
    - O alfabeto maiúsculo está em sequência na tabela, ou seja, se o inteiro
      correspondente ao caractere `'A'` é igual a `x`, o correspondente
      a `'B'` é igual a `x+1`, `'C'` é `x+2`, etc.
    - O mesmo acontece para o alfabeto minúsculo: `'a'` é `y`, `'b'` é `y+1`...
    - O mesmo para os números: `'1'` é `z`, `'2'` é `z+1`...
    - O alfabeto maiúsculo tem valores menores que os do alfabeto
      minúsculo
---

### C++: Entrada de Dados
Comando de entrada `cin`: atribui valor lido do teclado
às variáveis após o `>>`:

```C++
#include &lt;iostream&gt;
using namespace std;
int main(){
    int x = 0;
    cout << "digite um valor: ";
    cin >> x;
    cout << "o valor digitado foi " << x << endl;
    return 0;
}
```
---

### Exercício
Implemente um programa que lê um número inteiro e um
caractere e imprime o texto
`"O inteiro eh X e o caractere eh Y"`
seguido por uma quebra de linha, sendo `X` e `Y`
o inteiro e o caractere respectivamente.
---

### Exercício: Solução
```
#include &lt;iostream&gt;
using namespace std;
int main(){
    int num;
    char carac;
    cout << "insira um num. inteiro:\n";
    cin >> num;
    cout << "insira um caractere:\n";
    cin >> carac;
    cout << "O inteiro eh " << num
         << " e o caractere eh "
         << carac << endl;
    return 0;
}
```
---

### C++: Operadores

- Operador de atribuição: `=`
- Operadores aritméticos: `+`, `-`, `*`, `/`
- Operadores relacionais: `>`, `>=`, `<`, `<=`, `==`, `!=`
- Operadores lógicos: `!` (negação), `||` (ou), `&&` (e)

Você verá mais sobre operadores na aula que vem
---

### Exercício
Implemente um programa que lê dois números inteiros.
O programa deve armazenar em uma variável booleana
o resultado da comparação `X == Y`,
sendo `X` e `Y` os dois inteiros lidos.
Em seguida, o programa deve imprimir a variável
booleana.
---

### Exercício: Solução
```
#include &lt;iostream&gt;
using namespace std;
int main(){
    int x, y;
    bool iguais;
    cout << "insira dois num. inteiros:\n";
    cin >> x >> y;
    iguais = x == y;
    cout << "Iguais: " << iguais << endl;
    return 0;
}
```
---

### Sumário
- Na aula de hoje, você viu:
    - Estrutura de um programa em C++
    - Declaração e inicialização de variáveis
    - Tipos básicos
    - Comandos de entrada e saída
    - Operadores
---