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

### TESTE
```
<foo ... />
```
---

### C++: Primeiro Programa

```C++
int main(){
    return 0;
}
```
---

### C++: Primeiro Programa **Útil** 

```
#include <iostream>

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

```cpp
#include <iostream>

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
#include <iostream>

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

<img src="variaveis.png" width=250/>

- Variáveis precisam ser declaradas antes de serem utilizadas
---

### C++: Sintaxe de Declaração de Variáveis
```c++
tipo_da_variavel nome_da_variavel;
```
- `tipo_da_variavel` pode ser:
    - `bool`: declara um booleano (assume verdadeiro ou falso)
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

### C++: Valor Inicial de Variáveis
O que é impresso no seguinte programa?

```
#include <iostream>

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
- Sintaxe:

```c++
tipo_da_variavel nome_da_variavel = valor_inicial;
```
- `= é o operador de atribuição
---