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
#### Programando na linguagem C++
---

## C++: Primeiro Programa

```C++
int main(){
    return 0;
}
```
---

<section data-markdown><textarea data-template>
### C++: Primeiro Programa **Útil** 

```C++
#include <iostream>

using namespace std;

int main(){
    cout << "LiP: programando em C++\n";
    return 0;
}
```
---
</textarea></section>

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

### C++: Declaração de Variáveis
#### Sintaxe
```
tipo_da_variavel nome_da_variavel;
```
- `tipo\_da\_variavel` pode ser:
    - `bool`: declara um booleano (assume verdadeiro ou falso)
    - `int`: declara um número inteiro
    - `float`: declara um número real
    - `char`: declara **um único** caractere
- `nome\_da\_variavel` deve obedecer às regras:
    1. deve começar com uma letra ou `_` (underline ou underscore)
    2. deve ser composto por letras, dígitos ou `_`
    3. não pode ser uma palavra reservada (p. ex. `if`)
- Note que `x` e `X` são duas variáveis diferentes
- Boa prática: utilizar nomes significativos
---

### Linguagem de Programação
#### Relação da Disciplina com o Curso

- Para responder esta pergunta, é interessante enumerar as competências
  e habilidades previstas para os bachareis em CeT
- Mais informações [Projeto Pedagógico do Curso](https://sigaa.ufrn.br/sigaa/public/curso/ppp.jsf?lc=pt_BR&id=10320810)
---

### Linguagem de Programação
#### Competências e Habilidades

1. **capacidade de identificar, avaliar e resolver problemas, enfrentar desafios e responder
a novas demandas da sociedade contemporânea**
2. **capacidade de comunicação e argumentação em suas múltiplas formas**
3. **capacidade de atuar em áreas de fronteira e interfaces de diferentes disciplinas e campos de saber**
---

### Linguagem de Programação
#### Competências e Habilidades

4. **atitude investigativa, de prospecção, de permanente busca e produção do conhecimento**
5. capacidade de reconhecer especificidades regionais ou locais, contextualizando-as e relacionando-as com a situação global
6. **atitude ética nas esferas profissional, acadêmica e das relações interpessoais**
---

### Linguagem de Programação
#### Competências e Habilidades

7. comprometimento com a sustentabilidade nas relações entre ciência, tecnologia, economia, sociedade e ambiente
8. **capacidade de tomar decisões em cenários de imprecisões e incertezas**
---

### Linguagem de Programação
#### Competências e Habilidades

Como é possível ver, o curso de Linguagem de Programação (LiP)
é bem completo quanto ao seu envolvimento com as competências
e habilidades desejadas de um bacharel em CeT.

---

### Apresentação
- Prof. Dr. Bruno Silva
- Atendimento:
    - Via email: bruno.silva@ect.ufrn.br
    - Via Discord
    - Horário para a turma: terças e quintas, das 15h às 16h
- Áreas de interesse:
    - Processamento de imagens e visão computacional
    - Inteligência artificial e robótica
---

### Sobre a Disciplina
- Aulas teóricas: quartas e sextas, de 16:50 às 18:30,
  via Google Meet
- Carga horária total: 90 horas
    - Teoria: 60 horas
    - Laboratório: 30 horas
- Metodologia
    - Aulas expositivas com slides digitais
    - Apresentação de um tópico de aula seguido por exercícios relacionados
    - Atividades práticas em laboratório
---

### Laboratórios
- Professor responsável:
    - Prof. Dr. Francisco Vidal
- Horários:
    - Subturma 2A: Terça, 7:00 às 8:40 
    - Subturma 2B: Terça, 8:55 às 10:35
    - Subturma 2C: Quinta, 7:00 às 8:40
    - Subturma 2D: Quinta, 8:55 às 10:35
---

### Avaliações
- Avaliação semanal:
    - Avaliação continuada
    - Práticas de laboratório envolvendo o conteúdo
      dado na semana anterior
- Assiduidade
    - Presenças serão registradas por chamada oral
      em todas as aulas
---

### Sobre a Disciplina: Observação Importante
Regimento Interno/UFRN, Seção III:

- Prevê punições para casos de:
    - Fraudes (colas)
    - Perturbação ao andamento normal das atividades
    - Ofensas a servidores da universidade
---