# 1. Análise exporatória e governança de dados

Este documento tem o intuito de explorar os dados entregues pelo parceiro, a fim de receber omsoghts, além de explicar como os dados devem ser lidados para garantir conformidade com a governança de dados.

## 1.1 Variáveis e pontos estratégicos

Para realizar análises mais precisas durante a primeira sprint do projeto, foi decido por escolher 3 variáveis que mais se encaixavam nas user stories e requisitos definidos. 

Todas as variáveis se referem a um desses 3 temas macro: vendedores e gerentes, produtos ou lojas, e por isso, uma das decisões foi que teríamos pelo menos uma variáveis de cada um dos temas. 

No início, foi realizado um brainstorming por parte do grupo para coletar algumas variáveis possiíveis, e porteriormente, essas foram filtradas por relevância para o parceiro. No fim, esse foi o resultado:
- lucro entre lojas de uma região;
- lucro entre regiões;
- produtos com maior taxa de lucro;
- categoria de produto mais vendida por região;
- lojas com maior targetsale por região por mês;
- melhores vendedores por loja de cada região;
- categoria mais vendida por loja, região e diretoria;
- cruzamento de dados entre vendedores e categoria dos produtos vendidos, para perceber se algum se destaca na venda de algum tipo de produto;
- quantidade de vendas de um vendedor por mês;
- quais produtos costumam ser vendidos juntos;

Todas essas análises foram consideradas importântes de serem realizadas até o final do porjeto, porém, levando em conta o tempo de desenvolvimento que o grupo possuía, profundidade de análise, e relação com os requisitos e user stories do projeto, as escolhidas foram:
- lucro entre regiões;
- produtos com maior taxa de lucro;
- quantidade de vendas de um vendedor por mês;

## 1.2 Análise gráfica das variáveis

Para facilitar a compreensão, cada análise foi feita em um documento R markdown diferente, e suas versões em html podem ser acessadas abaixo:
- [lucro entre regiões](/docs/R%20notebooks/lucro.html)
- [produtos com maior taxa de lucro](/docs/R%20notebooks/produto.html)
- [quantidade de vendas de um vendedor por mês](/docs/R%20notebooks/vendedor.html)

## 1.3 Novas análises gráficas das variáveis

Após a apresentação da sprint 1, o parceiro percebeu que faltaram alguns dados, e ao enviá-los, as análises tiveram de ser refeitas para analisar a possibilidade de novos insights. Suas versões em html podem ser acessadas abaixo:
-[lucro entre regiões](/docs/R%20notebooks/lucro_novas_analises.html)