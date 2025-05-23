from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df00 = df.merge(orders, on='customer_id')
df00 = df00.merge(itens, on='order_id')
df00 = df00.merge(produtos, on='product_id', how='left')

df00.dropna(subset=[
    'product_name_lenght',
    'product_description_lenght',
    'product_photos_qty',
    'order_approved_at',
    'freight_value'
], inplace=True)

df00 = pd.get_dummies(df00, columns=['product_category_name'], drop_first=True)


-----------------------------------------------------------------------------------------


Q1 = df00['price'].quantile(0.25)
Q3 = df00['price'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

df00 = df00[(df00['price'] >= limite_inferior) & (df00['price'] <= limite_superior)]


----------------------------------------------------------------------------------------------


from sklearn.ensemble import RandomForestRegressor

modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)


------------------------------------------------------------------------------------------------


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

df00 = df.merge(orders, on='customer_id')
df00 = df00.merge(itens, on='order_id')
df00 = df00.merge(produtos, on='product_id', how='left')

df00.dropna(subset=[
    'product_name_lenght',
    'product_description_lenght',
    'product_photos_qty',
    'order_approved_at',
    'order_purchase_timestamp',
    'freight_value',
    'product_category_name'
], inplace=True)

df00['order_purchase_timestamp'] = pd.to_datetime(df00['order_purchase_timestamp'])
df00['order_approved_at'] = pd.to_datetime(df00['order_approved_at'])

df00['tempo_aprovacao_segundos'] = (df00['order_approved_at'] - df00['order_purchase_timestamp']).dt.total_seconds()

Q1 = df00['price'].quantile(0.25)
Q3 = df00['price'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
df00 = df00[(df00['price'] >= limite_inferior) & (df00['price'] <= limite_superior)]

df00 = pd.get_dummies(df00, columns=['product_category_name'], drop_first=True)

X = df00[[
    'product_name_lenght',
    'product_description_lenght',
    'product_photos_qty',
    'freight_value',
    'tempo_aprovacao_segundos'
] + [col for col in df00.columns if col.startswith('product_category_name_')]]

y = df00['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Amostras no teste: {len(X_test)}")

modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("R²:", r2)
