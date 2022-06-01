Biblioteca

Você deve escrever uma classe para representar uma biblioteca.
Essa classe deve ter campos para representar o nome da biblioteca e o
catálogo de livros disponíveis para empréstimo.

O construtor da sua classe deve receber o nome da biblioteca e criar uma
biblioteca sem nenhum livro no catálogo.

Essa classe deve ter métodos para adicionar um livro ao catálogo e para pegar
um livro emprestado. Somente é possível pegar emprestado um livro que está
no catálogo e não está emprestado.

Por fim, sua classe também deve ter um método para imprimir o catálogo atual
da biblioteca, conforme mostrado abaixo.

A entrada de dados começa com uma linha contendo o nome da biblioteca.
Em seguida, há uma linha com um número inteiro **N**, seguida de **N**
eventos, cada um em uma linha. Podemos ter os seguintes tipos de eventos:
- adicionar NomeLivro: adiciona NomeLivro ao catálogo de livros.
- emprestar NomeLivro: empresta o livro NomeLivro, desde que ele exista no
católogo e não tenha sido emprestado.
- imprimir: imprime o católogo atual da biblioteca

A cada evento, o seu programa deve imprimir uma mensagem informativa.
Veja o exemplo de entrada e saída abaixo.


- Exemplo de Entrada

Biblioteca Câmara Cascudo
6
adicionar Sertões
emprestimo Sertões
emprestimo Sertões
emprestimo A_Rosa_do_Povo
adicionar Pequeno_Príncipe
imprimir

- Exemplo de Saída

Sertões adicionado ao catálogo
Sertões emprestado
Sertões já foi emprestado
A_Rosa_do_Povo não está no catálogo
Pequeno_Príncipe adicionado ao catálogo
Biblioteca Câmara Cascudo:
Sertões (emprestado)
Pequeno_Príncipe (disponível)
