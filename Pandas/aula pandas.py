import pandas as pd 


data = {'Idade': [23, 29, 34, 22, 55]}
df = pd.DataFrame(data) 

media_idade = df['Idade'].mean() 
print(f'Média de Idade: {media_idade}') 

mediana_idade = df['Idade'].median()
print(f'Mediana de Idade: {mediana_idade}')


data = {'Idade': [23, 29, 34, 22, 25, 29]} 
df = pd.DataFrame(data) 

moda_idade = df['Idade'].mode()
print(f'Moda de Idade: {moda_idade}') 

soma_idade = df['Idade'].sum()
print(f'Soma de Idade: {soma_idade}') 

contagem_idade = df['Idade'].count()
print(f'Contagem de Idade: {contagem_idade}') 

desvio_padrao_idade = df['Idade'].std()
print(f'Desvio Padrão de Idade: {desvio_padrao_idade}') 

min_idade = df['Idade'].min()
max_idade = df['Idade'].max()
print(f'Idade mínima: {min_idade}, Idade máxima: {max_idade}')

variancia_idade = df['Idade'].var()
print(f'Variância de Idade: {variancia_idade}')


df_sem_duplicatas = df.drop_duplicates()
print(df_sem_duplicatas) 


data_vendas = {
    'Vendas': [100, 200, 300, 400, 500],
    'Custos': [80, 150, 200, 300, 400]
}
df_vendas = pd.DataFrame(data_vendas)


resumo_estatistico = df_vendas.describe()
print(resumo_estatistico) 


df_vendas['Lucro'] = df_vendas['Vendas'] - df_vendas['Custos'] 
print(df_vendas) 

correlacao = df_vendas[['Vendas', 'Lucro']].corr()
print(f'Correlação:\n{correlacao}') 

covariancia = df_vendas[['Vendas', 'Lucro']].cov() 
print(f'Covariância:\n{covariancia}') 

df_vendas['Rank'] = df_vendas['Vendas'].rank()
print(df_vendas)
