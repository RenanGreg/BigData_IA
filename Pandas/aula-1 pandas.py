import pandas as pd

data = {
    'nome': ['Alice', 'Bob', 'Carlos'],
    'Idade': [25, 30, 22],
    'Cidade': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(data)
print(df)

nomes = df['nome']
print(nomes)

primeira_linha = df.iloc[0]
print(primeira_linha)

subset = df.loc[:1, ['nome', 'Idade']]
print(subset)

filtro = df[df['Idade'] > 23]
print(filtro)

df['Idade em 5 anos'] = df['Idade'] + 5
print(df)

df = df.drop(columns=['Cidade'])
print(df)

df_ordenado = df.sort_values(by='Idade', ascending=False)
print(df_ordenado)

data = {
    'Cidade': ['Sao Paulo', 'Rio de Janeiro', 'Alagoas', 'Sergipe'],
    'Vendas': [200, 150, 300, 400]
}

df_vendas = pd.DataFrame(data)

agrupado = df_vendas.groupby('Cidade').sum()
print(agrupado)

df1 = pd.DataFrame({'Id': [1, 2, 3], 'Nome': ['Alice', 'Bob', 'Carlos']})
df2 = pd.DataFrame({'Id': [1, 2, 4], 'Salario': [5000, 6000, 7000]})

df_combined = pd.merge(df1, df2, on='Id', how='inner')
print(df_combined)

