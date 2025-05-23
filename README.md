# Projeto-Analise-e-Previsao-de-Vendas-em-E-commerce
Este projeto tem como objetivo realizar uma análise completa dos dados de vendas de um e-commerce, utilizando técnicas de estatística, análise exploratória de dados e machine learning para prever resultados futuros. 
Abrange desde a limpeza e transformação dos dados até a criação de modelos preditivos, além da documentação completa em GitHub.
Ferramentas, e sites usados para auxiliar na analise:
Kaggle, Notion, Anaconda Navigator, Jupyter Notebook, Chat GPT, Medium

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
