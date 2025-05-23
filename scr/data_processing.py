import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import pearsonr

-----------------------------------------------------------------------------------------
clientes = pd.read_csv("data/raw/olist_customers_dataset.csv")
geolocal = pd.read_csv("data/raw/olist_geolocation_dataset.csv")
itens = pd.read_csv("data/raw/olist_order_items_dataset.csv")
pagamentos = pd.read_csv("data/raw/olist_order_payments_dataset.csv")
reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
produtos = pd.read_csv ("data/raw/olist_products_dataset.csv")
vendedores = pd.read_csv("data/raw/olist_sellers_dataset.csv")
traducao = pd.read_csv("data/raw/product_category_name_translation.csv")

-----------------------------------------------------------------------------------------------
clientes.isnull().sum()

-------------------------------------------------------------------------------------
geolocal.isnull().sum()

--------------------------------------------------------------------------------
pagamentos.isnull().sum()

-------------------------------------------------------------------------
traducao.isnull().sum()

--------------------------------------------------------------------------
reviews.isnull().sum()

-----------------------------------------------------------------------------
orders.isnull().sum()

----------------------------------------------------------------------------
produtos.isnull().sum()

------------------------------------------------------------------------------
vendedores.isnull().sum()

---------------------------------------------------------------------------------
traducao.isnull().sum()

--------------------------------------------------------------------------
clientes.info()

-------------------------------------------------------------------------
geolocal.info()

-----------------------------------------------------------------------------
traducao.info()

----------------------------------------------------------------------
pagamentos.info()

-------------------------------------------------------------------------------
reviews.info()

----------------------------------------------------------------------
orders.info()

-----------------------------------------------------------------
produtos.info()

-----------------------------------------------------------------------
vendedores.info()

------------------------------------------------------------------------
traducao.info()

---------------------------------------------------------------------
reviews[pd.isnull(reviews['review_comment_title'])]

-------------------------------------------------------------------------
orders[pd.isnull(orders['order_approved_at'])]

----------------------------------------------------------------
produtos[pd.isnull(produtos['product_category_name'])]

--------------------------------------------------------------------------------------
produtos

----------------------------------------------------------------------
produtos.dropna(inplace=True)

---------------------------------------------------------------------
produtos

------------------------------------------------------------------------
pagamentos

---------------------------------------------------------------------
data = {'valor': pagamentos['payment_value'] }
df = pd.DataFrame(data)

Q1 = df['valor'].quantile(0.25)
Q3 = df['valor'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[(df['valor'] < limite_inferior) | (df['valor'] > limite_superior)]

print("Outliers encontrados:")
print(outliers)

plt.figure(figsize=(8, 4))
sns.boxplot(x=df['valor'], color="blue")
plt.axvline(limite_inferior, color='red', linestyle='--', label='Limite Inferior')
plt.axvline(limite_superior, color='green', linestyle='--', label='Limite Superior')
plt.title('Boxplot com Outliers')
plt.legend()
plt.show()

----------------------------------------------------------------------------------------
mascara_outliers = (df['valor'] < limite_inferior) | (df['valor'] > limite_superior)

outliers = df[mascara_outliers]

--------------------------------------------------------------------------
duplicadas1 = clientes.duplicated().sum()
duplicadas1

---------------------------------------------------------------------------
duplicadas2 = geolocal.duplicated().sum()
duplicadas2

------------------------------------------------------------------------------
duplicadas3 = pagamentos.duplicated().sum()
duplicadas3

----------------------------------------------------------------------------
duplicadas4 = traducao.duplicated().sum()
duplicadas4

--------------------------------------------------------------------------
duplicadas5 = reviews.duplicated().sum()
duplicadas5

----------------------------------------------------------------------
duplicadas6 = orders.duplicated().sum()
duplicadas6

------------------------------------------------------------------------
duplicadas7 = produtos.duplicated().sum()
duplicadas7

---------------------------------------------------------------------
duplicadas8 = vendedores.duplicated().sum()
duplicadas8

----------------------------------------------------------------------
geolocal

---------------------------------------------------------------------
geolocalnew = geolocal.drop_duplicates()
geolocalnew

--------------------------------------------------------------------------
df = clientes
df1 = geolocalnew
df2 = itens
df3 = pagamentos
df4 = reviews
df5 = orders
df6 = produtos
df7 = vendedores
df8 = traducao

-------------------------------------------------------------------------------------------------------
order_customers = pd.merge(df5, df, on='customer_id', how='left')
full_data = pd.merge(order_customers, df3, on="order_id", how='left')
full_data = pd.merge(full_data, df2, on="order_id", how='left')
full_data = pd.merge(full_data, df6, on="product_id", how='left')
full_data = pd.merge(full_data, df4, on='order_id', how='left')
full_data = pd.merge(full_data, df7, on='seller_id', how='left')
full_data = pd.merge(full_data, df8, on="product_category_name", how='left')
full_data["product_category_name"] = full_data["product_category_name_english"]
full_data.pop("product_category_name_english")

------------------------------------------------------------------------------------------------------------------
top_10_produtos = full_data.groupby('product_category_name')['order_id'].nunique().sort_values(ascending=False)
top_10_produtos.head(10).plot(kind='bar', title='Top-10 de cada categoria')
plt.xlabel('categoria')
plt.ylabel('produto')
plt.show()

-----------------------------------------------------------------------------------------------------------------------------
full_data['order_delivered_customer_date'] = pd.to_datetime(full_data['order_delivered_customer_date'])
full_data['order_purchase_timestamp'] = pd.to_datetime(full_data['order_purchase_timestamp'])
full_data['delivery_time'] = (full_data['order_delivered_customer_date'] - full_data['order_purchase_timestamp']).dt.days
full_data['delivery_time'] = list(full_data['delivery_time'])
rewiews_by_delivery = full_data.groupby('review_score')['delivery_time'].mean()


sns.set_theme(style="ticks", font_scale=1.25)
sns.catplot(data=full_data, kind='bar', x='review_score', y='delivery_time')
plt.show()

--------------------------------------------------------------------------------------------------------------------------------------------
price_by_state = full_data.groupby('customer_state')['payment_value'].mean().sort_values(ascending=True).head(10).reset_index()

sns.set_theme(style="whitegrid", font_scale=1.1)
plt.figure(figsize=(6, 8))
sns.barplot(data=price_by_state, x='payment_value', y='customer_state')

plt.title('Top 10 Estados com Menor Valor Médio de Pedido')
plt.ylabel('Estado')
plt.xlabel('Valor Médio do Pedido')
plt.show()

-----------------------------------------------------------------------------------------------------------
full_data['order_purchase_timestamp'] = pd.to_datetime(full_data['order_purchase_timestamp'])

full_data['year_month'] = full_data['order_purchase_timestamp'].dt.to_period('M').astype(str)

monthly_sales = full_data.groupby('year_month')['payment_value'].sum().reset_index()

sns.set_theme(style="whitegrid", font_scale=1.2)
plt.figure(figsize=(14, 6))
sns.lineplot(data=monthly_sales, x='year_month', y='payment_value', marker='o', linewidth=2)

plt.title('Vendas Totais por Mês')
plt.xlabel('Ano-Mês')
plt.ylabel('Total de Vendas (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

--------------------------------------------------------------------------------------------------------------------------
mask = (full_data['order_purchase_timestamp'] >= '2018-08-01') & (full_data['order_purchase_timestamp'] <= '2018-10-31')
missing_period = full_data.loc[mask]

print(f"Registros entre 08/2018 e 10/2018: {len(missing_period)}")


---------------------------------------------------------------------------------------------------------
correlacao0 = pd.merge(pagamentos, reviews, on='order_id')
correlacao0_num = correlacao0[['payment_value', 'review_score']].dropna()
correlacao0_num.select_dtypes(include='number').corr()

--------------------------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.regplot(data=correlacao0_num, x='payment_value', y='review_score')
plt.title('Correlação entre Valor do Pagamento e Nota de Avaliação')
plt.xlabel('Valor do Pagamento ')
plt.ylabel('Nota da Avaliação ')
plt.grid(True)
plt.tight_layout()
plt.show()

----------------------------------------------------------------------------------------------
correlacao1 = pd.merge(pagamentos, itens, on='order_id')
correlacao1 = correlacao1[['payment_value', 'price']].corr()
correlacao1

----------------------------------------------------------------------------------------
corr, p_valor = pearsonr(correlacao0['payment_value'], correlacao0['review_score'])

print(f"Coeficiente de correlação: {corr:.2f}")
print(f"Valor-p: {p_valor:.4f}")