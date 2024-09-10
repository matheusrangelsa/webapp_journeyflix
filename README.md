# Projeto Journeyflix | Sistema de Recomendação de Conteúdos de Streaming
Projeto desenvolvido para implementar as **funcionalidades básicas** do sistema de recomendação de um streaming de vídeos, baseado na **filtragem por conteúdo** usando **python**.

### **O que é o Journeyflix?**
A proposta da Journeyflix é oferecer um sistema de recomendação de vídeos, tais como os principais players de streaming Video On Demand (Netflix, Max, Globoplay, Amazon Prime, entre outros), mas focado em quem gosta de aproveitar o tempo de deslocamento diário em transportes públicos para assistir algo

Imagine que sua faculdade fica a duas horas de distância da sua casa, e todos os dias você passa quatro horas no trem, entre ida e volta. Muitas vezes, você quer assistir a algo, mas acaba gastando boa parte desse tempo apenas escolhendo o que ver, e no fim, não assiste nada (isso é o conhecido como paradoxo da escolha).

A Journeyflix vem para facilitar sua vida: você informa ao sistema quanto tempo tem disponível e quais são seus gêneros favoritos. Com base nesses dados, a Journeyflix cria uma lista personalizada e entrega recomendações de títulos que você poderá assistir do início ao fim, encaixando-se perfeitamente no tempo do seu trajeto.

O código está sendo melhorado ainda, mas por enquanto se seguir as instruções corretamente, conseguirá receber filmes recomendados ao executar o código.

### **Como usar:**
---
   1.  **Informe o tempo do trajeto:** Insira o tempo que você leva para ir e voltar do trabalho, faculdade, ou curso utilizando transporte público (em minutos);
   2.  **Escolha seus temas favoritos:** Selecione um ou mais temas de sua preferência para que o algoritmo possa entender melhor seus gostos;
   3.  **Receba suas recomendações:** O sistema de recomendação analisará o catálogo de conteúdos e sugerirá aqueles que se encaixam perfeitamente no seu tempo disponível para assistir;
   4.  **Atualize as sugestões:** Se quiser ver novas recomendações, basta apertar F5 para atualizar a página. O sistema irá sugerir outras opções disponíveis, caso existam.

---
---

### **Etapas do algoritmo:**
---
   1.  Ler um arquivo CSV com informações sobre filmes;
   2.  Solicitar ao usuário o tempo disponível para assistir filmes;
   3.  Perguntar ao usuário qual dos gêneros de filmes disponíveis é o seu favorito;
   4.  Aplicar o primeiro filtro e gera uma pré-lista com os filmes que atendam às condições escolhidas de tempo x gêneros;
   5.  Aplicar o segundo filtro que seleciona os filmes cuja soma das durações é menor ou igual ao tempo disponível informado pelo usuário;
   6.  Formatar a saída da lista de recomendações de filmes, exibindo o resultado das recomendações.
<br><br>

Todos os direitos reservados. Este projeto é protegido por direitos autorais e não pode ser copiado, distribuído, ou modificado.