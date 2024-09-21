# projeto_extensao_desenvolvimento_rapido_aplicacoes_python
Desenvolvimento Rápido de Aplicação para fins de Precificação de itens de vestuário infantil em uma loja utilizando informações de Notas fiscais

Desenvolver uma aplicação que colete das notas fiscais de compra, os dados dos itens e exporte para uma planilha, para que assim haja possibilidades diversas de trabalhar com esses dados. Além de exportar os dados, a aplicação deverá fazer a precificação dos itens, com base nas orientações recebidas.

Objetivo: Que a loja saia de uma situação de uma ausência total de dados manipuláveis, para uma onde todos os dados principais e importantes para o estabelecimento sejam coletados das notas fiscais e colocados em uma planilha, juntamente com a precificação de todos os produtos adquiridos. 

Espera-se que a aplicação possa de forma simples, com um volume relativamente grande de ítens adquiridos, facilitar e agilizar a precificação, eliminando a necessidade de fazer-se os cálculos manualmente.

A proposta deste projeto foi realmente desafiadora, pois desafia-nos a aplicar os conhecimentos para criar uma aplicação funcional e útil para nossa comunidade, mas conforme aprendemos no Tema 2, o desenvolvimento rápido de aplicações é ideal para projetos que exigem entrega rápida e adaptabilidade. 

Conforme orientações do Tema 2 Módulo 2, no levantamento de requisitos foi feita uma pesquisa, juntamente com a cliente, do ambiente, recursos e do tempo de implementação, chegando a conclusão que o projeto era viável.

Então deu-se início ao desenvolvimento da aplicação. Inicialmente o objetivo era que a aplicação percorresse nota por nota e extraísse as informações que fossem importantes para a cliente e as exportasse em forma de uma planilha, para que, assim, os dados pudessem ter utilidades não previstas. 

Conforme tema 3 módulo 1, utilizamos a estrutura “with open” que garante que o arquivo será fechado adequadamente após utilizarmos o arquivo.
Após a criação do protótipo, a aplicação já fazia o que se previa. Porém testes de possíveis situações que gerassem erro, conforme aprendido no Tema 3 Módulo 3, foram tratadas todas as exceções.

Após apresentação do protótipo, a cliente ficou extremamente satisfeita com o resultado. Mas após eu conversar sobre o que mais fazia falta dentro do cotidiano, esta me explicou como era feita a precificação, onde ítem por ítem, utilizando calculadora, se pegava o valor do custo do ítem e multiplicava por 2.2 e depois acrescia de 12%. Então vi a oportunidade de automatizar as precificação de todos os ítens que fossem adquiridos, acrescentando, com um cálculo simples, uma coluna na planilha com a precificação.

Após a geração da versão 2 do protótipo, foi apresentado a cliente, sendo que esta ficou super satisfeita. porém me mostrou a etiqueta que somente mostrava o valor em parcelas de 3x __, então foi feita nova modificação, acrescentando a coluna do valor da parcela. e foi novamente apresentado o protótipo, com grande satisfação desta.

Então eu, vendo que ainda haveria certo tempo, busquei usar os conhecimentos do Tema 5 (Interface Gráfica Com Python) para que a aplicação ficasse mais amigável. Então usando o TKinter elaborei uma interface que acrescentava a funcionalidade de escolher quais colunas gostaria de usar, melhorando ainda mais.

Então foi apresentado a cliente a versão final, mediante total aprovação, foi-se feito o processo de implantação e treinamento com sucesso.
