### Linguagem de Programação
#### Comando de Repetição `for`
---

### Linguagem de Programação
- Aula anterior:
    - Comandos de seleção
- Aula de hoje:
    - Comando de repetição `for`
---

### Comandos de Repetição
- Essenciais para a automatização de tarefas repetitivas
- Repetem todos os comandos que estejam no seu corpo
- Também chamados de laços ou *loops*
- Dois tipos:
    - Comando de repetição contado: o `for` repete instruções
      por um determinado número de vezes
    - Comando de repetição condicional: o `while` repete instruções
      enquanto uma condição é verdadeira (próxima aula)
---

### Comandos de Repetição
#### Exemplo de Motivação

Implemente um programa que escreva `n` vezes na tela
`"eu vou praticar programacao"`
---

### Comando `for`
Sintaxe:

```
for(inicializacao; condicao; incremento){
    comando1;
    ...
    comandoN;
}
```
---

### Comando `for`
- Itera sobre uma variável, chamada de contador, variável de iteração ou variável de controle
- Dividido em três expressões
    - Inicialização: executada somente na primeira vez (iteração)
      em que o `for` é executado
    - Condição: avaliada no início de cada iteração
    - Incremento: executado no final de cada iteração
- Todas as expressões são opcionais
---

### Comando `for`
```
for(inicializacao; condicao; incremento){
    comando1;
    ...
    comandoN;
}
```
Ordem de execução:
1. A expressão de inicialização é executada
2. A expressão de condição é avaliada:
    - Caso seja verdadeira: o bloco de comandos é executado
    - Caso seja falsa: o laço é encerrado
3. A expressão de incremento é executada
4. O passo 2 é executado
---

### Comando  `for`
#### Exemplo
```C++
int main(){
    int i, n;
    cin >> n;
    for(i = 0; i < n; i++){
        cout << "i: " << i << endl;
    }
    return 0;
}
```
Qual a saída do programa?
---

### Comandos de Repetição
#### Exemplo de Motivação
Voltando ao exemplo inicial: agora sim, vimos o que é necessário

```C++
int main(){
    int i, n;
    cin >> n;
    for(i = 0; i < n; i++){
        cout << "eu vou praticar programacao\n";
    }
    return 0;
}
```
---

### Programação e Automatização de Tarefas

<img src="quadrinho_nerd.png" width=600/>

Aprender programação é aprender a automatizar tarefas
---

### Comando `for`
#### Exemplo de Motivação
No mesmo exemplo, o que aconteceria se fosse usado:
- `for(i = 0; i < 10*n; i += 10)...`
- `for(i = n; i > 0; i--)...`
- `for(i = 10*n; i > 0; i -= 10)...`
---

### Comando `for`
#### Usos Equivalentes do `for`
- Diferentes combinações para a inicialização, condição e incremento
  fazem o  `for` repetir pela mesma quantidade de vezes
- Ou seja, diferentes `for` podem ser usados se estivermos preocupados
  com a quantidade de execuções de um bloco de comandos
  - O que não é o caso se desejarmos que a variável de iteração
    assuma uma sequência de valores específicos
---

### Comando `for`
- Exercício 1: faça um programa que lê um número `n` e em seguida,
lê as notas de  `n` alunos. O programa deve exibir a média das notas
na tela.
- Antes de programar: o que deve ser repetido?
---

### Comando `for`
#### Exercício 1: Solução
```C++
int main(){
    int i, n;
    float nota, media = 0;
    cout << "Insira a quantidade de notas\n";
    cin >> n;
    for(i = 0; i < n; i++){
        cout << "Insira a nota do "
             << i+1 << "o. aluno" << endl;
        cin >> nota;
        media += nota;
    }
    media /= n;
    cout << "media da turma: " << media << endl;
    return 0;
}
```
---

### Comando `for`
#### Exemplos Atípicos
- Quantas vezes é executado o laço a seguir? `n` vezes?
```C++
for(i = 0; i <= n; i++){
    ...
}
```

- Quantas vezes é executado o laço a seguir? Ele irá parar?
```C++
for(i = n; i > 0; i++){
    ...
}
```
---

### Comando `for`
- Exercício 2: implemente um programa que lê um número `n` e em seguida,
imprime os `n` primeiros números pares na tela. Considere o número 0 como
o primeiro par.
---

### Comando `for`
#### Exercício 2: Solução
```C++
int main(){
    int i, n;
    cout << "Digite n\n";
    cin >> n;
    for(i = 0; i < 2*n; i += 2){
        cout << i << endl;
    }
    return 0;
}
```
Obviamente, há outras formas de se implementar este programa
---

### Comando `for`
- Exercício 3: implemente um programa que imprime na tela em forma de tabela
as seguintes contagens
    - De 1 a 100
    - De 10 a 1000 (incrementando o contador de 10 em 10)
    - De 100 a 1 (em ordem decrescente)

| 1   | 10   | 100 |
|:----|------|----:|
| 2   | 20   | 99  |
| 3   | 30   | 98  |
| ... | ...  | ... |
| 100 | 1000 | 1   |
---

### Comando  `for`
#### Exercício 3: Solução
```C++
int main(){
    int i;
    for(i = 1; i <= 100; i++){
        cout << i << " "
             << 10*i << " "
             << 101-i << endl;
    }
    return 0;
}
```
É possível implementar o programa com o uso de
variáveis adicionais
---

### Comando `for`
- Exercício 4: faça um programa que lê um número `n` e em seguida,
lê `n` caracteres.
O programa deve exibir a quantidade de caracteres digitados
que são letras minúsculas.
---

### Comando `for`
#### Exercício 4: Solução
```C++
int main(){
    char car;
    int n, cont = 0;
    cout << "Informe a quantidade de caracteres:\n";
    cin >> n;
    for(int i = 0; i < n; i++){
        cout << "Informe um caractere\n";
        cin >> car;
        if(car >= 'a' && car <= 'z'){
            cont++;
        }
    }
    cout << cont << " letras minusculas digitadas\n";
    return 0;
}
```
---

### Comando `for`
- Exercício 5: faça um programa que lê um número `n` e um número `m`.
Em seguida, o seu programa deve exibir na tela as `m` primeiras potências
positivas dos `n` primeiros números positivos. As potências devem estar separadas por linha. Exemplo de execução:
```
Informe a quantidade de numeros
5
Informe a quantidade de potencias
4
Potencias:
1 1 1 1 
2 4 8 16 
3 9 27 81 
4 16 64 256 
5 25 125 625
```
---

### Comando `for`
#### Exercício 5: Solução
```C++
int main(){
    int i, j, n, m;
    cout << "Informe a quantidade de numeros\n";
    cin >> n;
    cout << "Informe a quantidade de potencias\n";
    cin >> m;
    for(i = 1; i <= n; i++){
        for(j = 1; j <= m; j++){
            cout << pow(i,j) << " "; 
        }
        cout << endl;
    }
    return 0;
}
```
---

### Sumário
Na aula de hoje:
- Comando de repetição `for`
- Exercícios
---