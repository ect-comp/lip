### Linguagem de Programação
#### Comandos de Seleção - Exercícios
---

### Linguagem de Programação
#### Exercício 0 (Desafio de 06/04)

Implemente um programa que leia do usuário um número inteiro.
O seu programa deve imprimir na tela o sucessor do número,
exceto se ele for o número 11. Neste caso, o próprio número
deve ser impresso.
**Você não deve utilizar nenhum comando condicional.**

---

### Linguagem de Programação
#### Exercício 0 (Desafio de 06/04) - Solução

```C++
#include <iostream>

using namespace std;

int main(){

    int num;

    cout << "Insira um num. inteiro:\n";
    cin >> num;

    //Duas soluções:
    
    //cout << ( (num == 11)*num + (num != 11)*(num+1) ) << endl;
    cout << ( (num != 11) + num ) << endl;

    return 0;
}
```

---

### Linguagem de Programação
#### Exercício 1

O mês de Abril de 2022 começou em uma sexta-feira.
Implemente um programa que dado o número de um dia
do mês de abril de 2022 (um valor entre 1 e 30),
imprime o dia da semana correspondente. Você
pode utilizar **if-else** ou **switch** na solução.

Exemplo:
```
Entrada: 17
Saída: Dia 17 - Domingo.
```

---

### Linguagem de Programação
#### Exercício 1 - Solução

```C++
#include <iostream>

using namespace std;

int main(){

    int dia;

    cout << "Insira um dia (1-30) de Abril/2022:\n";
    cin >> dia;

    switch((dia-1) % 7){
        case 0:
            cout << "Dia " << dia << " - sexta\n";
            break;
        case 1:
            cout << "Dia " << dia << " - sabado\n";
            break;
        case 2:
            cout << "Dia " << dia << " - domingo\n";
            break;
        case 3:
            cout << "Dia " << dia << " - segunda\n";
            break;
        case 4:
            cout << "Dia " << dia << " - terca\n";
            break;
        case 5:
            cout << "Dia " << dia << " - quarta\n";
            break;
        case 6:
            cout << "Dia " << dia << " - quinta\n";
            break;
    }

    return 0;
}
```

---

### Linguagem de Programação
#### Exercício 2

Implemente um programa que lê três notas
de um aluno em uma disciplina e imprime
a situação do aluno conforme as regras da UFRN:

- **Aprovado**: média das notas é maior ou igual a 5 e
  o aluno não tem nenhuma nota abaixo de 3
- **Reposicao**: o aluno não foi aprovado e tem média
  maior ou igual a 3
- **Reprovado**: o aluno tem média menor do que 3

Exemplo:
```
Entrada: 5 2 10          Saída: Reposicao
Entrada: 5 4  6          Saída: Aprovado
Entrada: 4 4  0          Saída: Reprovado
```

---

### Linguagem de Programação
#### Exercício 2 - Solução

```C++
#include <iostream>

using namespace std;

int main(){

    float n1, n2, n3, media;

    cout << "Insira as 3 notas:\n";
    cin >> n1 >> n2 >> n3;

    media = (n1 + n2 + n3)/3;

    if(n1 >= 3 && n2 >= 3 && n3 >= 3 && media >= 5){
        cout << "Aprovado\n";
    }
    else if(media >= 3){
        cout << "Reposicao\n";
    }
    else{
        cout << "Reprovado\n";
    }

    return 0;
}
```

---

### Lista de Presença

<img src="https://chart.apis.google.com/chart?cht=qr&chs=300x300&chld=L%7C1&chl=https%3A%2F%2Fbit.ly%2F361rEZw" alt="QR Code" border="0" />

<a href="https://bit.ly/361rEZw"><p style="text-align:center;">https://bit.ly/361rEZw</p></a>

---

### Linguagem de Programação
#### Exercício 3

Implemente um programa que leia
do usuário uma letra. O programa
deve imprimir uma mensagem informando
se a letra é vogal/consoante e
minúscula/maiúscula.

Exemplo:
```
Entrada: a          Saída: Vogal minuscula
Entrada: C          Saída: Consoante maiuscula
```

---

### Linguagem de Programação
#### Exercício 3 - Solução

```C++
#include <iostream>

using namespace std;

int main(){

    char letra;

    cout << "Insira uma letra:\n";
    cin >> letra;

    if(letra >= 'a' && letra <= 'z'){
        if(letra == 'a' || letra == 'e' || letra == 'i' ||
           letra == 'o' || letra == 'u'){
            cout << "Vogal minuscula\n";
        }
        else{
            cout << "Consoante minuscula\n";   
        }
    }
    else{
        if(letra == 'A' || letra == 'E' || letra == 'I' ||
           letra == 'O' || letra == 'U'){
            cout << "Vogal maiuscula\n";
        }
        else{
            cout << "Consoante maiuscula\n";
        }
    }

    return 0;
}
```

---

### Linguagem de Programação
#### Exercício 4

Implemente um programa que, dada a hora de saída,
tempo de viagem e a diferença de fuso horário
entre a cidade de saída e o destino, informe
a hora de chegada no destino.

A entrada é dada por 3 números inteiros $$s (0 \le s \le 23)$$,
$$t (1 \le t \le 12)$$ e $$f (-5 \le f \le 5)$$ (estes intervalos
são assumidos verdadeiros, o seu programa não precisa checá-los.)

(Exercício retirado do
[Beecrowd](https://www.beecrowd.com.br/judge/pt/problems/view/2057))

Exemplos:
```
Entrada: 10 7  3         Saída: 20
Entrada: 22 6 -2         Saída:  2
Entrada:  0 3 -4         Saída: 23
```

---

### Linguagem de Programação
#### Exercício 4 - Desafio

- Entre no site da questão e faça o seu cadastro
- Prints de soluções submetidas até as 12:29 do dia 14/04
  serão aceitas como 0,3 extra na 1a. unidade

---