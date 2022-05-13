Pontuação no Campeonato

Você deseja calcular a pontuação de um time em um campeonato de futebol
a partir das informações das partidas realizadas.

As informações de uma partida são representadas como um dicionário
com os seguintes campos:
- mandante: nome do time mandate
- visitante: nome do time visitante
- gols\_mandante: número de gols marcados pelo time mandante
- gols\_visitante: número de gols marcados pelo time visitante

O time que marca mais gols em uma partida é o vencedor e ganha três pontos,
enquanto o outro time não ganha nenhum ponto.
Caso os dois times marquem a mesma quantidade de gols, há um empate e os dois
times ganham um ponto.

O seu programa deve ler um valor inteiro **N** e em seguida ler as
informações de **N** partidas, onde os dados de cada partida serão fornecidos
em uma linha, separados por espaços, seguindo o formato:
Nome_Time_Mandante Gols_Time_Mandante Gols_Time_Visitante Nome_Time_Visitante

Em seguida, o seu programa deve ler o nome de um time e imprimir a pontuação
dele no campeonato.



- Exemplo de Entrada

4
ABC 2 1 Globo
Potiguar 3 1 America 1
ABC 0 1 America
Alecrim 3 3 Globo
Globo

- Exemplo de Saída
Globo tem 1 pontos

