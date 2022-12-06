### Linguagem de Programação
#### Tipos Estruturados e Ordenação - Exercícios
---

## Contexto: Treinos de Corrida

Imagine um aplicativo que registra __treinos de corrida__,
ou seja, o dia, distância, tempo e ritmo que uma pessoa
correu.

---

## Contexto: Treinos de Corrida
<video data-autoplay src="./videos/ordenacao_corridas.mp4"></video>
---

### Exercício 1
#### Treinos de Corrida

Considere um treino de corrida. Ele contém:

- Uma data
- Uma duração (horas, minutos e segundos)
- Uma distância dada em quilômetros
- Um *pace* (ritmo por quilômetro), dado em minutos e segundos

Tendo em mente que você vai precisar ordenar por
data, duração e pace...

---

### Exercício 1
#### Treinos de Corrida

Implemente os tipos estruturados:
- `Data`, com os campos `dia`, `mes` e `ano`
- `Duracao`, com os campos `hor`, `min` e `seg`
- `Pace`, com os campos `min` e `seg`
- `Corrida`, com os campos `data`, `duracao`, `pace` e `distancia`

---

### Exercício 2
#### Ordenando Datas

Agora, divida o seu programa, se concentrando em implementar
uma função para ordenar um vetor de `Data`, da mais antiga
para a mais recente.

Como você pode implementar esta função?

**Observe que é para ordenar um vetor de `Data` e não
de `Corrida`**

---

### Lista de Presença

<img src="https://chart.apis.google.com/chart?cht=qr&chs=300x300&chld=L%7C1&chl=https%3A%2F%2Fbit.ly%2F3VCvEUR" alt="QR Code" border="0" />

<a href="https://bit.ly/3VCvEUR"><p style="text-align:center;">https://bit.ly/3VCvEUR</p></a>

---

### Exercício 3
#### Ordenando Datas - Função Main

Implemente a função `main` para testar a função
do exercício anterior:
- Deve ler uma quantidade `n` de datas
- Deve ler o dia, mês e ano de `n` datas
- Chamar a função de ordenar por datas
- Exibir o resultado na tela

---

### Exercício 4
#### Lendo Dados de Corrida

Implemente um função que receba uma `Corrida`
como parâmetro de entrada e saída.

A função deve ler, na ordem:
- A data da corrida (dia, mês e ano)
- A duração da corrida (hora, min. e seg.)
- A distância da corrida (em Km)

Faça a função `main` exibir os dados
lidos em um formato adequado.

---

### Exercício 5
#### Calculando o Pace

> O pace é dado na quantidade de minutos e segundos
> que uma pessoa leva para percorrer 1 Km

Ex:
Se uma pessoa corre 10Km em 1h 03 min e 35 seg,
o seu pace foi de 6:25/Km.

---

### Exercício 5
#### Calculando o Pace

Implemente um programa que calcule
o pace dada uma duração.

O pace é calculado por:
- Transformando a duração em segundos/Km
- O quociente da divisão da transformação por 60 é
  a quantidade de minutos do pace
- O resto da divisão da transformação por 60 é
  a quantidade de segundos do pace

---

### Exercício Completo

**Pontuação extra:** funções para
- Ordenar um vetor de `Corrida` por duração
- Ordenar um vetor de `Corrida` por pace

Na função main, implemente um menu, a partir do qual
o usuário pode escolher como quer visualizar
suas corridas (opção 0 ordena por data,
1 por duração e 2 por pace).

---