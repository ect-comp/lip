# Aula

## Nas Aulas Anteriores

- Tudo :)
	- Funções
	- Vetores e matrizes
	- Strings
	- Tipos estruturados
	- Arquivos

## Objetivo da Aula
- Demonstrar aplicações do conteúdo da disciplina
  na solução de problemas práticos

## Problema Proposto
Considere o seguinte problema:

- Dadas uma lista de cidades e a distância que
  ligam umas às outras diretamente
- Implemente um programa que leia do usuário o nome de uma cidade origem
  e o nome de uma cidade destino e em seguida, exiba na tela a distância entre as cidades
- Uma cidade deve ter como dados o seu nome, o nome do seu país e a sua população

## Problema Proposto
\framesubtitle{Dados das Cidades}
	\centering
	\includegraphics[width=0.40\textwidth]{img/cidades.png}

## Problema Proposto
\framesubtitle{Leitura de Dados}

- Será que é prático o usuário digitar todos estes dados
  a cada vez que for utilizar o programa?
  	- Usar arquivos
  	- Definir estrutura do arquivo: que dados devem estar nele e em que ordem

## Problema Proposto
\framesubtitle{Leitura de Dados}

- E quanto às distâncias entre as cidades? Como estes dados poderiam ser dados?
	- Usar matriz
	- Posição \texttt{M[i][j]} da matriz \texttt{M} informa a distância entre
	  a cidade \texttt{i} e a cidade \texttt{j} 
	- Note que \texttt{i} e \texttt{j} são números
	- Uma cidade \texttt{i} pode não ter conexão direta com \texttt{j}: distância é dada por -1
	- Neste problema, as distâncias de \texttt{i} para \texttt{j}
	  e de \texttt{j} para \texttt{i} são as mesmas
		- Só é necessário armazenar parte triangular superior (ou inferior) da matriz

## Problema Proposto
\framesubtitle{Distâncias entre as Cidades}
	\centering
	\includegraphics[width=0.60\textwidth]{img/cidades_distancias.png}

## Problema Proposto
\framesubtitle{Estrutura do Arquivo}
- A estrutura completa do arquivo deve ter portanto os seguintes dados (em ordem):
	1. total de cidades do problema
	2. para cada cidade:
		- nome da cidade, seguido por quebra de linha
		- nome do país, seguido por quebra de linha
		- população da cidade, seguida por quebra de linha
	3. matriz triangular superior contendo as distâncias:
		- linha 0: distância entre 0 e 1, 0 e 2, 0 e 3...
		- linha 1: distância entre 1 e 2, 1 e 3, 1 e 4...
		- linha n-2, distância entre n-2 e n-1 

## Problema Proposto
\framesubtitle{Estrutura do Arquivo}
Exemplo de arquivo de entrada:

```
9
cidade a
pais a
100000
cidade b
pais a
50000
cidade c
pais a
30000
cidade d
pais b
200000
cidade e
pais b
50000
... (continua)
```

## Problema Proposto
\framesubtitle{Estrutura do Arquivo}

```
...
cidade f
pais b
30000
cidade g
pais c
40000
cidade h
pais c
100000
cidade i
pais c
75000
...(continua)
```

## Problema Proposto
\framesubtitle{Estrutura do Arquivo}

```
...
4 -1 -1 -1 -1 -1  8 -1
   8 -1 -1 -1 -1 11 -1
      7 -1  4 -1 -1  2
         9 14 -1 -1 -1
           10 -1 -1 -1
               2 -1 -1
                  1  6
                     7
```

## Implementação
\framesubtitle{Funções a Serem Implementadas}
As funcionalidades devem ser implementadas cada uma em uma função.\newline\newline Entrada e verificação de dados:

0. Tipo estruturado cidade
1. Leitura de dados: função para inserir em um vetor de cidades e em uma matriz de inteiros
   todas as informações do arquivo
2. Função para impressão da matriz

## Implementação
\framesubtitle{Funções a Serem Implementadas}
Formulação da solução:

4. Função que retorna o índice da cidade no vetor dado o seu nome
5. Função \texttt{main}

## Observações Sobre a Solução
- A solução implementada retorna a distância entre cidades \textbf{diretamente} conectadas
- Entretanto, é possível ir da \texttt{cidade a} até a \texttt{cidade c}, passando por \texttt{cidade b}
	- Ou seja, existe um caminho que leva da \texttt{cidade a} até a \texttt{cidade c}, por exemplo

## Diagrama de Cidades
A conexão entre as cidades é dada pelo seguinte diagrama:
	\centering
	\includegraphics[width=0.60\textwidth]{img/cidades_diagrama.png}

## Novo Problema Proposto
- Exibir na tela \textbf{a menor} distância entre duas cidades informadas pelo usuário,
  assumindo que há um caminho entre as duas
- Problema consideravelmente mais complexo
- Possui algoritmo conhecido na literatura:
	- Algoritmo do caminho mais curto ou algoritmo de Dijkstra \cite{clrs}
	- Apenas a ideia do algoritmo será passada
	- Implementação poderá ser aceita como pontuação extra

## Novo Problema Proposto
\framesubtitle{Intuição do Algoritmo}
- O algoritmo calcula a distância mínima entre a cidade origem e todas as outras,
  armazenando este resultado em um vetor
- Após isto, basta acessar a posição da cidade destino no vetor
- Funcionamento:
	- O algoritmo separa todas as cidades entre processadas e não processadas
	- Enquanto houverem cidades não processadas, a cidade mais próxima a qualquer
	  cidade processada deve ser adicionada ao conjunto das cidades processadas
	- As distâncias totais partindo desta nova cidade até as suas vizinhas devem
	  ser atualizadas

## Novo Problema Proposto
\framesubtitle{Pseudo-código do Algoritmo}

1. Inicialize cidades processadas como o vetor vazio
2. Inicialize as dist. totais com \texttt{INF} para todas as cidades
   exceto para a cidade de origem, que deve conter o valor 0
3. Enquanto houverem cidades não processadas:
	1. u = cidade não processada com menor dist. total
	2. para toda cidade vizinha não processada v de u:
		1. some a dist. total até u com a distância entre u e v
		2. compare esta soma com a dist. total até v e substitua esta dist.
		   pela soma se a soma for menor
4. Utilize o índice da cidade destino para obter a dist. total a partir da cidade origem

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo0.png}

- \texttt{processadas = \{\}}
- \texttt{dist. tot. = \{0, $\infty$, $\infty$, $\infty$, $\infty$, $\infty$, $\infty$, $\infty$, $\infty$\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo1.png}

- \texttt{processadas = \{0\}}
- \texttt{dist. tot. = \{0, $\infty$, $\infty$, $\infty$, $\infty$, $\infty$, $\infty$, $\infty$, $\infty$\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo2.png}

- \texttt{processadas = \{0\}}
- \texttt{dist. tot. = \{0, 4, $\infty$, $\infty$, $\infty$, $\infty$, $\infty$, 8, $\infty$\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo3.png}

- \texttt{processadas = \{0, 1\}}
- \texttt{dist. tot. = \{0, 4, $\infty$, $\infty$, $\infty$, $\infty$, $\infty$, 8, $\infty$\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo4.png}

- \texttt{processadas = \{0, 1\}}
- \texttt{dist. tot. = \{0, 4, 12, $\infty$, $\infty$, $\infty$, $\infty$, 8, $\infty$\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo5.png}

- \texttt{processadas = \{0, 1, 7\}}
- \texttt{dist. tot. = \{0, 4, 12, $\infty$, $\infty$, $\infty$, $\infty$, 8, $\infty$\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo6.png}

- \texttt{processadas = \{0, 1, 7\}}
- \texttt{dist. tot. = \{0, 4, 12, $\infty$, $\infty$, $\infty$, 9, 8, 15\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo7.png}

- \texttt{processadas = \{0, 1, 7, 6\}}
- \texttt{dist. tot. = \{0, 4, 12, $\infty$, $\infty$, $\infty$, 9, 8, 15\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo8.png}

- \texttt{processadas = \{0, 1, 7, 6\}}
- \texttt{dist. tot. = \{0, 4, 12, $\infty$, $\infty$, 11, 9, 8, 15\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo9.png}

- \texttt{processadas = \{0, 1, 7, 6, 5\}}
- \texttt{dist. tot. = \{0, 4, 12, $\infty$, $\infty$, 11, 9, 8, 15\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo10.png}

- \texttt{processadas = \{0, 1, 7, 6, 5\}}
- \texttt{dist. tot. = \{0, 4, 12, 25, 21, 11, 9, 8, 15\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo11.png}

- \texttt{processadas = \{0, 1, 7, 6, 5, 2\}}
- \texttt{dist. tot. = \{0, 4, 12, 25, 21, 11, 9, 8, 15\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo12.png}

- \texttt{processadas = \{0, 1, 7, 6, 5, 2\}}
- \texttt{dist. tot. = \{0, 4, 12, 19, 21, 11, 9, 8, 14\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo13.png}

- \texttt{processadas = \{0, 1, 7, 6, 5, 2, 8\}}
- \texttt{dist. tot. = \{0, 4, 12, 19, 21, 11, 9, 8, 14\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo14.png}

- \texttt{processadas = \{0, 1, 7, 6, 5, 2, 8, 3\}}
- \texttt{dist. tot. = \{0, 4, 12, 19, 21, 11, 9, 8, 14\}}

## Novo Problema Proposto
\framesubtitle{Funcionamento do Algoritmo}
	\centering
	\includegraphics[width=0.60\textwidth]{img/grafo15.png}

- \texttt{processadas = \{0, 1, 7, 6, 5, 2, 8, 3, 4\}}
- \texttt{dist. tot. = \{0, 4, 12, 19, 21, 11, 9, 8, 14\}}

## Sumário
- Na aula de hoje:
	- Exemplo de aplicação prática que pode ser implementada com o que foi visto na disciplina
