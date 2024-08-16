import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Importando o dataset
df = pd.read_csv('MKT.csv')

# Exibindo o dataframe
print(df)

# Exibindo as informações do dataframe
df.info()
print(f'{df.describe()}\n')

# Sepando as variaveis 
X = df.drop('sales', axis=1)
y = df['sales']

# Seperando os conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# Criando um modelo de regressão linear
model = LinearRegression()

# Treinando o modelo com os dados de treinamento
model.fit(X_train, y_train)

# Fazendo previsões
predictions = model.predict(X_test)

# Criando um dataframe com os valores de test e sua previsão
df_test = X_test
df_test['sales'] = y_test
df_test['predictions'] = predictions

# Exibindo dadaframe de test
print(f'{df_test}\n')

# Calcular o coeficiente de determinação (R²)
r2 = r2_score(y_test, predictions)

# Exibir o resultado do coeficiente de determinação (R²)
print(f'Coeficiente de Determinação (R²) tem: {r2*100:.2f}% de precisão\n')

# Criando dicionario para receber as entradas do usuario
user_input = {}

# Recebendo entradas do usuário
for i in X.columns:
    user_input[i] = float(input(f'Digite o valor que você deseja investir em {i}: '))

# Convertendo as entradas do usuário em um DataFrame
user_input_df = pd.DataFrame([user_input])

# Fazendo previsões para as entradas do usuário
user_predictions = model.predict(user_input_df)

# Exibindo as previsões para as entradas do usuário
print(f'\nPrevisão do valor de retorno: {user_predictions[0]:.2f}\n')
