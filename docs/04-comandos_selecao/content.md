<section data-center=true>

### Linguagem de Programação
#### Comandos de Seleção
---

<section data-transition="zoom">

### Linguagem de Programação
- Aulas anteriores:
    - Variáveis e tipos básicos
    - Como modificar variáveis: operadores e expressões
    - Tipos diferentes em uma mesma expressão
- Aula de hoje: comandos de seleção
    - Comando `if-else`
    - Comando `switch-case`
    - Operador ternário `? :`
---

### Comandos de Seleção
- Desviam o fluxo de execução de um programa
- Permitem a execução de uma ou mais instruções (bloco de código)
  quando uma determinada expressão for verdadeira
---

### Comando `if`
Sintaxe:

```C++
if(condicao){
    comando1;
    ...
    comandoN;
}
```
---

### Comando `if`
- Comando de seleção simples: depende apenas de uma condição
- A condição é qualquer expressão (inclusive expressões
  aritméticas ou constantes)
- A condição é sempre avaliada como expressão lógica
    - Verdadeiro: qualquer valor diferente de zero
    - Falso: zero
---

### Comando `if`
#### Exemplo
Programa que lê um número digitado pelo usuário
e imprime a frase `"Numero invalido"`
caso o usuário digite zero:

```C++
int main(){
    int x;
    cin >> x;
    if(x == 0){
        cout << "Numero invalido" << endl;
    }
    return 0;
}
```
---

### Comando `if`
#### Exemplos Atípicos
- Comando `if` que sempre executa:

```C++
if(1){
    cout << "Sempre imprime" << endl;
}
```

- Uso incorreto de operadores:

```C++
if(x = 0){ //ha um problema aqui
    cout << "Numero invalido" << endl;
}
```
---

### Comando `if`

Exercício: faça um programa que lê uma letra digitada pelo usuário
e imprime a frase `"Vogal minuscula digitada"`  caso o usuário digite uma vogal
minúscula
---

### Comando `if`
#### Exercício: Solução
```C++
int main(){
    char c;
    cin >> c;
    if(c == 'a' || c == 'e' || c == 'i' ||
       c == 'o' || c == 'u'){
        cout << "Vogal minuscula digitada" << endl;
    }
    return 0;
}
```
---

### Comando `if-else`
Sintaxe:

```C++
if(condicao){
    comandoI.1;
    ...
    comandoI.N;
}
else{
    comandoE.1;
    ...
    comandoE.N;
}
```
---

### Comando `if-else`
- Comando de seleção composto: dois blocos dependem de uma mesma condição
- Quando a condição é verdadeira: bloco correspondente ao `if` é executado
- Quando a condição é falsa: bloco correspondente ao `else` é executado
---

### Comando `if-else`
#### Exemplo
Programa que lê um número digitado pelo usuário
e imprime a frase `"Numero invalido"` caso o usuário digite zero
ou a frase `"Numero valido"` caso contrário

```C++
int main(){
    int x;
    cin >> x;
    if(x == 0){
        cout << "Numero invalido" << endl;
    }
    else{
        cout << "Numero valido" << endl;
    }
    return 0;
}
```
---

### Comando `if-else`

Exercício: faça um programa que lê uma letra digitada pelo usuário
e imprime a frase `"Vogal minuscula digitada"`  caso o usuário digite uma vogal
minúscula ou a frase `"Consoante minuscula digitada"` caso o usuário digite uma consoante minúscula
---

### Comando `if-else`
#### Exercício: Solução
```C++
int main(){
    char c;
    cin >> c;
    if(c == 'a' || c == 'e' || c == 'i' ||
       c == 'o' || c == 'u'){
        cout << "Vogal minuscula digitada" << endl;
    }
    else{
        cout << "Consoante minuscula digitada" << endl;
    }
    return 0;
}
```
---

### Encadeamento de `if-else`
Sintaxe:

```C++
if(condicao1){
    comando1.1;
    ...
    comando1.N;
}
else if(condicao2){
    comando2.1;
    ...
    comando2.N;
}
else{
    comando3.1;
    ...
    comando3.N;
}
```
---

### Encadeamento de `if-else`
- Comando de seleção aninhado: associação de vários `if-else`
- Cada `else` só é executado se o `if` anterior for falso
- Somente então a condição do próximo `if` é testada
- Assim, os blocos de comandos são mutuamente exclusivos (apenas um deles pode ser verdadeiro por execução)
---

### Encadeamento de `if-else`
Exercício: faça um programa que lê a nota de um aluno e imprime:
- `"Aprovado"`, caso a nota seja maior ou igual a `5.0`
- `"Em recuperacao"`, caso a nota seja maior ou igual a `3.0` e
menor do que `5.0`
- `"Reprovado"`, caso a nota seja menor do que `3.0`
---

### Encadeamento de `if-else`
#### Exercício: Solução
```C++
int main(){
    float nota;
    cin >> nota;
    if(nota >= 5.0){
        cout << "Aprovado" << endl;
    }
    else if(nota >= 3.0){
        cout << "Em recuperacao" << endl;
    }
    else{
        cout << "Reprovado" << endl;
    }
    return 0;
}
```
---

### Comando `switch-case`
Sintaxe:

```C++
switch(expressao){
    case constante1:
        comando 1.1;
        ...
        comando 1.N;
        break;
    ...
    case constanteN:
        comando N.1;
        ...
        comando N.N;
        break;
    default:
        comando d.1;
        ...
        comando d.N;    
}
```
---

### Comando `switch-case`
- Comando de seleção de múltipla escolha: alternativa ao uso de vários `if-else`
- Possui sintaxe específica que compara o valor de uma variável ao de várias
  constantes
- Funcionamento:
    - O bloco `case` que possuir valor igual ao da constante será executado
    - Todos os blocos `case` abaixo do executado são também executados...
---

### Comando `switch-case`
- ... exceto no caso em que cada `case` termina com um `break`
- `default` (opcional): executado quando a expressão não é igual a nenhuma das constantes
---

### Comando `switch-case`
Exemplo: programa que escreve por extenso na tela o nome de cada dígito (de 0 a 2; complete o código para nrs. até 9):

```C++
int main(){
    int d;
    cin >> d;
    switch(d){
        case 0:
            cout << "zero" << endl;
            break;
        case 1:
            cout << "um" << endl;
            break;
        case 2:
            cout << "dois" << endl;
            break;
    }
    return 0;
}
```
---

### Comando `switch-case`
Exercício: utilizando o `switch-case`, faça um programa que lê uma letra
digitada pelo usuário e imprime a frase `"Vogal digitada"`  caso o usuário
digite uma vogal ou a `"Consoante digitada"` caso o usuário digite uma
consoante
---

### Comando `switch-case`
#### Exercício: Solução

```C++
int main(){
    char c;
    cin >> c;
    switch(c){
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case u':
            cout << "Vogal digitada" << endl;
            break;
        default:
            cout << "Consoante digitada" << endl;
    }
    return 0;
}
```
---

### Operador Ternário `? :`
Sintaxe:
```C++
expr1 ? expr2 : expr3;  
```

- Como o nome sugere, necessita de três operandos `expr1`, `expr2` e `expr3`
    - `expr1` é avaliada
    - se `expr1` for verdadeira, `expr2` é calculada 
    - se `expr1` for falsa, `expr3` é calculada
- O resultado calculado é o resultado do operador ternário
---

### Operador Ternário `? :`
Exemplo: programa que atribui à `y`:
- O valor 1  se `x` for maior ou igual a zero
- O valor -1  se `x` for menor que zero

```C++
int main(){
    int x, y;
    cin >> x;
    y = x >= 0 ? 1 : -1;
    cout << "y: " << y << endl;
    return 0;
}
```
---

### Operador Ternário `? :`
Exercício: utilizando o `? :`, faça um programa que lê dois números
e imprime qual é o maior dos dois
---

### Operador Ternário: `? :`
#### Exercício: Solução
```C++
int main(){
    int x, y, maior;
    cin >> x >> y;
    x > y ? maior = x : maior = y;
    cout << maior << " e o maior" << endl;
    return 0;
}
```
---

### Comandos de Seleção
#### Dicas Gerais
- Todo `switch-case` pode ser feito com `if-else`, mas não o contrário
- Operador ternário: utilizado em casos simples de  `if-else`
- No final das contas:  `if-else` é mais genérico e portanto, mais indicado
para uso
---

### Sumário
Checklist da aula de hoje:
- Seleção simples `if`
- Seleção composta `if-else`
- Seleção aninhada (encadeamento de `if-else`)
- Comando `switch`
- Operador ternário `? :`
---