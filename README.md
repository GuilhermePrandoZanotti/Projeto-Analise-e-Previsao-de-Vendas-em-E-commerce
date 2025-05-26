---PROJETO DE ANALISE DE DADOS DE UM E-COMMERCE---

Este projeto tem como objetivo realizar uma análise exploratória dos dados de um e-commerce, com foco na identificação de padrões de compra, comportamento dos clientes e desempenho de vendas.

Durante o desenvolvimento do projeto, foi utilizada a metodologia Kanban em conjunto com a ferramenta Notion. Essa abordagem permitiu um trabalho mais organizado e eficiente, evitando perdas de foco e facilitando o acompanhamento das tarefas.

Na fase inicial do projeto, observou-se a presença de valores nulos nas bibliotecas Reviews, Orders e Produtos, os valores nulos de Reviews e Orders não foram descartados, pois representam avaliações ou pedidos incompletos, já os valores nulos em produtos foram considerados descartáveis, pois comprometem a integridade da base de dados.

Também foi notada uma grande quantidade de variáveis do tipo float64 e object, o que exigiu atenção especial durante o tratamento dos dados.

Durante a análise estatística, notou-se a presença significativa de outliers. No entanto, esses dados não foram removidos, pois compõem uma parcela importante da base. 
Muitos valores duplicados foram identificados na tabela geolocation e tratados adequadamente.

Foram criados diversos gráficos, incluindo:

Produtos mais vendidos por categoria;

Relação entre tempo de entrega e avaliação — demonstrando que quanto maior o tempo de entrega, menor a nota atribuída pelo cliente;

Ticket médio por estado — possibilitando identificar regiões com menor valor médio de compra e, com isso, sugerir promoções ou eventos específicos para aumentar as vendas;

Volume de vendas por mês (09/2016 a 10/2018);

Correlação entre forma de pagamento e avaliação — mostrou uma correlação baixa, sugerindo que o valor pago pelo cliente não afeta significativamente sua avaliação;

Correlação entre o preço de compra do produto e o valor final de venda — revelou uma correlação forte, indicando que o preço de aquisição impacta diretamente o valor repassado ao consumidor.

Na etapa de modelagem, foi utilizada a biblioteca Scikit-learn. Duas tentativas foram realizadas:

Primeiro modelo: apresentou desempenho insatisfatório.

Segundo modelo: teve resultado mais satisfatório, com um R2 de 0,69, indicando que o modelo explica 69% da variabilidade dos dados e gera previsões próximas aos valores reais.

As decisões tomadas foram guiadas tanto pela documentação técnica quanto por um planejamento de fluxo bem estruturado. As etapas seguiram uma ordem lógica e progressiva:

Criação do repositório;

Importação e verificação dos dados;

Limpeza e tratamento;

Análises exploratórias;

Análises estatísticas;

Modelagem preditiva.

Este projeto demonstrou como a análise de dados pode oferecer insights valiosos para a tomada de decisões estratégicas em um e-commerce. Através de uma abordagem estruturada e ferramentas adequadas, foi possível identificar padrões, corrigir inconsistências, prever comportamentos e propor melhorias baseadas em evidências concretas.

--- DIAS DE TRABALHO ---

06/05/2025 - Dia 1 -Inicio do projeto
- Planejamento do projeto
- Análise de requisitos
- Criação do repositório GitHub
- Criação do projeto e interligação com GitHub
- Importação dos dados do projeto
- Definição de variaveis
  
 07/05/2025 - Dia 2
 - Verificação de valores faltantes
 - Verificação de tipos
 - Foi verificado que mesmo as tabelas Reviews e Orders tendo valores nulos, não havia necessidade de retiralos e nem de renomealos
 - Tabela Produtos teve seus valores nulos retirados, pois não havia nenhuma informação em tais colunas
 - Criação da pasta Notebooks, e do arquivo "01-EDA"

12/05/2025 - Dia 3
 - Verificação de valores duplicados
 - Remoção de valores duplicados
 - Remoção de Outliers
   
13/05/2025 - Dia 4
 - Após analisar o grafico de Top 10 Produtos e Reviews relacionados a tempo de entrega, pode se concluir, que artigos de beleza, decoração e eletrônicos são os mais vendidos do e-commerce,
   também concluimos que, o tempo de entrega influencia diretamente nos reviews da loja
 - Criação de um grafico para ver o valor médio do pedido
 - Após analisar o grafico dee valor médio de pedido, indentifiquei que os estados listados no grafico, apresentam um valor de tiquet médio bom
 - Criação de um grafico para visulização de vendas por periodo
 - Foi notado uma grande queda de vendas em 09/2018 - 10/2018, podendo significar uma possivel falta de dados, ou interrupção nas operaçoes da empresa

14/05/2025 - Dia 5
 - Organização de pastas

20/05/2025 - Dia 6
 - Criação de gráficos e consulta de calculos de correlação de vendas e notas de avaliação, pagamentos e notas de avaliação
 - Após o teste de hipotese pode se observar que a correlação de pagamento e reviews é significativa, sendo que conforme o preço do produto sobe as notas vão diminuindo, diferente da relação de pagamentos e itens, que dizem que produtos mais caros tendem a receber pagamentos mais altos, tendo assim uma forte correlação entre os dois

23/05/2025 - Dia 7
 - Concluida a modelagem preditiva: Separação de treino/teste, Treinamento do modelo de regressão, Avaliação de performance.
 - Criação dos documentos e formatação do projeto

26/05/2025 - Dia 8
 - Conclusão da documentação
