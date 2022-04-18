### Linguagem de Programação
#### Comando de Repetição `while`
---

### Linguagem de Programação
- Aula anterior:
    - Comando de repetição `for`
- Aula de hoje:
    - Comando de repetição `while`
    - Comando de repetição `do-while`
    - Comandos `break` e `continue`
---

### Comandos de Repetição
- Essenciais para a automatização de tarefas repetitivas
- Repetem todos os comandos que estejam no seu corpo
- Também chamados de laços ou *loops*
---

### Comandos de Repetição
Dois tipos:
- Comando de repetição contado: o `for` repete instruções
  por um determinado número de vezes (aula anterior)
- Comando de repetição condicional: o `while` repete instruções
  enquanto uma condição é verdadeira
---

### Comandos de Repetição
#### Exemplo de Motivação

Implemente um programa que escreva na tela
`"vou estudar lip"`
enquanto um número lido não for 0
---

### Comando `while`
Sintaxe:

```C++
while(condicao){
    comando1;
    ...
    comandoN;
}
```
---

### Comando `while`
- Executa enquanto a condição é verdadeira
- Condição é qualquer expressão e é obrigatória
  (é convertida implicitamente em expressão lógica)
- A condição é testada antes de cada iteração
---

### Comando `while`
Devemos nos certificar de dois itens para garantir o seu funcionamento de forma correta:
1. Que a condição tem a possibilidade de ser verdadeira ao ser testada pela primeira vez
2. Que a condição vai se tornar falsa, em algum momento
---

### Comando `while`
#### Exemplo
```C++
int main(){
    int i = 0, n;
    cin >> n;
    while(i < n){
        cout << "i: " << i << endl;
        i++;
    }
    return 0;
}
```
- Qual a saída deste programa?
- Como foram garantidos os dois itens necessários?
---

### Comandos de Repetição
#### Exemplo de Motivação
Voltando ao exemplo inicial: agora sim, vimos o que é necessário

```C++
int main(){
    int n;
    cout << "Digite um numero\n";
    cin >> n;
    while(n != 0){
        cout << "vou estudar lip\n";
        cout << "Digite um numero\n";
        cin >> n;
    }
    return 0;
}
```
---

### Comandos de Repetição
#### Diferenças entre `while` e `for`
- O comando `while` é apropriado para repetição condicional
    - É possível utilizá-lo para repetição contada, embora
      isto seja mais propenso a erros
    - Diversas expressões lógicas podem ser usadas para o mesmo efeito
- O comando `for` é apropriado para repetição contada
    - É possível utilizá-lo para repetição condicional, embora
      o código resultante fique menos intuitivo
---

### Comando `while`
- Exercício 1: faça um programa que lê **vários** números e
informa se cada um deles é par ou ímpar. O programa deve se encerrar
quando for digitado um número negativo.
---

### Comando `while`
Precisamos identificar:
1. Variáveis do programa
2. Entrada e saída do programa
3. O que deve ser repetido
4. Expressão lógica para repetição
---

### Comando `while`
#### Exercício 1: Solução
```C++
int main(){
    int x;
    cout << "Informe um numero\n";
    cin >> x;
    while(x >= 0){
        if(x % 2 == 0){
            cout << x << " e um numero par\n";
        }
        else{
            cout << x << " e um numero impar\n";
        }
        cout << "Informe um numero\n";
        cin >> x;
    }
    return 0;
}
```
---

### Lista de Presença

<img src="https://chart.apis.google.com/chart?cht=qr&chs=300x300&chld=L%7C0&chl=https%3A%2F%2Fbit.ly%2F3JNbrFe" alt="QR Code" border="0" />

<a href="https://bit.ly/3JNbrFe"><p style="text-align:center;">https://bit.ly/3JNbrFe</p></a>

---

### Comando `do-while`
- A linguagem C++ oferece também o comando
  `do-while` (faça-enquanto)
- Sintaxe:

```C++
do{
    comando1;
    ...
    comandoN;
} while(condicao);
```
---

### Comando `do-while`
**Diferença para o `while`**: a condição é testada após a execução do corpo

- No comando `while`, o corpo pode não ser executado nenhuma vez
- No comando `do-while`, o corpo é executado pelo menos uma vez
---

### Comando `while` e `do-while`
#### Erros Comuns
- Não garantir que a condição pode ser verdadeira ao ser testada pela primeira vez (`while`)
- Não garantir que a condição vai se tornar falsa na lógica do algoritmo
- Inverter condição: a expressão lógica deve ter valor verdadeiro para que o laço execute
---

### Comandos `while` e `do-while`
- Exercício 2: implemente um programa que lê um número inteiro positivo `n` e em seguida, imprime o quociente e o resto da divisão de `n` por 10. O seu programa deve checar se
o usuário digitou um número inteiro positivo, solicitando ao mesmo para redigitá-lo se não
for o caso.
---

### Comandos `while` e `do-while`
#### Exercício 2: Solução
```C++
int main(){
    int x;
    do{
        cout << "Insira um numero inteiro
                 e positivo\n";
        cin >> x;
    } while(x < 0);

    cout << "q: " << x/10
         << ", r:" << x%10 << endl;

    return 0;
}
```
---

### Comandos `break` e `continue`
- Existem dois comandos que podem ser utilizados
  no corpo de laços `for`, `while` e `do-while`:
    - Comando `break`: utilizado para encerrar o laço em que o comando `break` se encontra
    - Comando `continue`: utilizado para ignorar a iteração atual do laço e forçar a próxima iteração
- No geral, há alternativas que tornam ambos os comandos opcionais
---

### Comando `break`
#### Menu com `break` (I)
O comando `break` pode ser usado
em menus:

```C++
int main(){
    char c1;
    do{
        cout << "Insira uma opcao:\n";
        cout << "\t (1) opcao1\n";
        cout << "\t (2) opcao2\n";
        cout << "\t (3) opcao3\n";
        cout << "\t (s) air\n";
        cin >> c1;
        if(c1 == '1'){
            cout << "opcao1 escolhida\n";
        }
        else if(c1 == '2'){
            cout << "opcao2 escolhida\n";
        }
        else if(c1 == '3'){
            cout << "opcao3 escolhida\n";
        }
        else if(c1 == 's'){
            cout << "Vc escolheu sair\n";
            break;
        }
    }while(true);
    return 0;
}
```
---

### Comando `break`
#### Menu sem `break`
O mesmo menu pode ser implementado sem `break`:
```C++
int main(){
    char o;
    do{
        cout << "Insira uma opcao:\n";
        cout << "\t (1) opcao1\n";
        cout << "\t (2) opcao2\n";
        cout << "\t (3) opcao3\n";
        cout << "\t (s) air\n";
        cin >> o;
        if(o == '1'){
            cout << "opcao1 escolhida\n";
        }
        else if(o == '2'){
            cout << "opcao2 escolhida\n";
        }
        else if(o == '3'){
            cout << "opcao3 escolhida\n";
        }
        else if(o == 's'){
            cout << "Vc escolheu sair\n";
        }
    }while(o != 's');
    return 0;
```
---

### Comando `continue`
#### Exemplo de Uso
```C++
int main(){
    int n, i, s = 0;
    cout << "Informe um numero\n";
    cin >> n;
    for(i = 0; i < n; i++){
        if(i % 2 == 0){
            continue;
        }
        s += i;
    }
    cout << s << endl;
    return 0;
}
```
O que faz este programa?
---

### Comando `continue`
#### Programa equivalente sem `continue`
O mesmo programa pode ser implementado sem `continue`:

```C++
int main(){
    int n, i, s = 0;
    cout << "Informe um numero\n";
    cin >> n;
    for(i = 0; i < n; i++){
        if(i % 2 != 0){
            s += i;
        }
    }
    cout << s << endl;
    return 0;
}
```
---

### Comando `while` e `do-while`
- Exercício 3: implemente um programa que lê a população no ano corrente
de dois países, A e B. O país A tem taxa de crescimento de 2% ao ano, enquanto
o país B cresce 4% ao ano. Supondo que a população do país A é maior do que a do
país B, o seu programa deve informar em quantos anos a população do país B ultrapassará a população do país A.
---

### Comando `while` e `do-while`
`Exercício 3: Solução`
```C++
int main(){
    int anos = 0;
    int pop_a, pop_b;

    cout << "Insira as populacoes iniciais:\n";
    cin >> pop_a >> pop_b;

    while(pop_b <= pop_a){
        pop_a *= 1.02;
        pop_b *= 1.04;
        anos++;
    }
    cout << "A populacao do pais B ultrapassa
             a do pais A em "
         << anos << " anos.\n";
    
    return 0;
}
```
---

### Sumário
Na aula de hoje:
- Comando de repetição `while`
- Comando de repetição `do-while`
- Comandos `break` e `continue`
- Exercícios
---