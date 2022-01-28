### Linguagem de Programação
#### Tipos Estruturados II
---

### Na Aula Anterior

- Tipos Estruturados
---

### Objetivo da Aula
Mais usos de tipos estruturados
---

### Exercício
Relembrando o problema apresentado na aula anterior:

- Ler do usuário o nome e a nota de 5 alunos
- Imprimir o nome dos alunos com nota inferior à média de todas as notas

Como ficaria o mesmo com o uso de tipos estruturados?
---

### Solução
#### Uso de Tipos Estruturados
```C++
const int STRMAX = 21;

struct Aluno{
  char nome[STRMAX];
  float nota;
};

int main(){
  int n = 5, i;
  Aluno alunos[n];
  float media = 0.0;

  for(i = 0; i < n; i++){
    cout << "Insira o nome do aluno: ";
    cin.getline(alunos[i].nome, STRMAX);
    cout << "Insira a nota do aluno: ";
    cin >> alunos[i].nota;
    cin.ignore();
    media += alunos[i].nota;
  }
  media /= n;

  for(i = 0; i < n; i++){
    if(alunos[i].nota < media){
      cout << alunos[i].nome
           << " esta abaixo da media\n";
    }
  }
  return 0;
}
```

### Motivação
E se desejássemos implementar o mesmo programa com uma função,
como poderíamos proceder?

- Função `imprime_alunos_abaixo_da_media`: imprime todos
  os alunos que estão abaixo da média
---

### Tipos Estruturados e Funções
#### Assinatura de Funções

Variáveis de tipos estruturados podem ser utilizadas
em funções com as mesmas regras de uma variável qualquer:

- Função que retorna o aluno com maior nota
em um vetor de alunos:

```
Aluno calcula_maior_nota(Aluno v[], int n);
```
---

### Tipos Estruturados e Funções
#### Assinatura de Funções

Variáveis de tipos estruturados podem ser utilizadas
em funções com as mesmas regras de uma variável qualquer:

- Função que armazena o aluno com a menor nota e
o aluno com a maior nota em parâmetros de saída:

```
void calcula_menor_maior_nota(Aluno v[], int n, 
                              Aluno& menor,
                              Aluno& maior);
```
---

### Tipos Estruturados e Funções
#### Chamadas de Funções

Assumindo variáveis declaradas como

```
Aluno a_menor, a_maior, alunos[MAX];
```

As funções mostradas anteriormente devem
ser chamadas da seguinte forma:

```
//var. recebe o retorno
a_maior = calcula_maior_nota(alunos, n);

//chamada armazena o resultado em parametros de saida
calcula_menor_maior_nota(alunos, n, a_menor, a_maior);

```
---

### Exercício 1

Reimplemente o exercício do início desta aula
implementando uma função **que imprime** todos
os alunos abaixo da média. Ou seja, a função
deve receber como parâmetro de entrada um vetor
do tipo `Aluno` (além do seu tamanho).

---

### Exercício 1
#### Solução

```C++
const int STRMAX = 21;

struct Aluno{
  char nome[STRMAX];
  float nota;
};

void imprime_alunos_abaixo_media(Aluno v[], int n){
  int i;
  float media = 0.0;

  //Calcula a média dos alunos
  for(i = 0; i < n; i++){
    media += v[i].nota;
  }
  media /= n;

  //Imprime os alunos abaixo da média
  for(i = 0; i < n; i++){
    if(v[i].nota < media){
      cout << v[i].nome
           << " esta abaixo da media\n";
    }
  }
}

int main(){
  int n = 5, i;
  Aluno alunos[n];

  //Lê do usuário os dados dos alunos
  for(i = 0; i < n; i++){
    cout << "Insira o nome do aluno: ";
    cin.getline(alunos[i].nome, STRMAX);
    cout << "Insira a nota do aluno: ";
    cin >> alunos[i].nota;
    cin.ignore();
  }

  imprime_alunos_abaixo_media(alunos, n);

  return 0;
}
```

### Tipo Estruturado para uma Matriz

- Uma grande vantagem do uso de tipos estruturados
  é que definir um tipo estruturado para representar
  uma matriz reduz a quantidade de parâmetros das
  funções
- Para isto, o tipo estruturado deve ter como campos:
  - O número de linhas da matriz
  - O número de colunas da matriz
  - Uma matriz de números inteiros, caracteres
    ou números reais, conforme pede o problema

---

### Tipo Estruturado para uma Matriz

Assim, uma função que lê uma matriz de números
inteiros, que tem como assinatura:

```C++
void le_mat(int mat[][MAX], int nl, int nc);
```

Passa a ter uma assinatura mais compacta dada por:

```C++
void le_mat(Matriz& mat);
```

(Note o parâmetro passado por referência).

---

### Exercício 2

Defina um tipo estruturado `Matriz`, que deve armazenar
uma matriz de números inteiros, o seu número de linhas e
o seu número de colunas.

Em seguida, implemente uma função que receba como parâmetro 
duas matrizes de tamanho qualquer e que calcule a soma matricial.
Faça a função retornar a matriz em uma primeira versão
e ela armazenar o resultado em um parâmetro de saída em uma segunda.

Implemente também a função `main`, de modo que o usuário
possa inserir os dados das matrizes e testar o programa.

---

### Exercício 2
#### Solução

```C++
const int MAX = 21;

struct Matriz{
  int nl;
  int nc;
  int numeros[MAX][MAX];
};

void le_mat(Matriz& m){
  int i, j;

  for(i = 0; i < m.nl; i++){
    for(j = 0; j < m.nc; j++){
      cin >> m.numeros[i][j];
    }
  }
}

void imprime_mat(Matriz m){
  int i, j;

  for(i = 0; i < m.nl; i++){
    for(j = 0; j < m.nc; j++){
      cout << m.numeros[i][j] << " ";
    }
    cout << endl;
  }
}

//Versão 1
Matriz soma_matrizes(Matriz m1, Matriz m2){
  int i, j;
  Matriz r;

  for(i = 0; i < m1.nl; i++){
    for(j = 0; j < m1.nc; j++){
      r.numeros[i][j] = m1.numeros[i][j] + m2.numeros[i][j];
    }
  }

  return r;
}

//Versão 2 a cargo do aluno :)

int main(){
  Matriz mat1, mat2, mat_soma;

  cout << "Insira a matriz 1:\n";
  le_mat(mat1);
  cout << "Insira a matriz 2:\n";
  le_mat(mat2);

  mat_soma = soma_matrizes(mat1, mat2);

  imprime_mat(mat_soma);

  return 0;
}
```

### Exercício 3

Implemente uma função que calcula
o produto matricial.
A função deve ter dois parâmetros
de entrada do tipo `Matriz`
e retornar uma `Matriz` como resultado.

---

### Sumário
Na aula de hoje:
- Uso de tipos estruturados em funções
- Exercícios
---
