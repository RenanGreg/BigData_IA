import pandas as pd 

data = {'Nome' : ['Ana', 'Bruno', None, 'Carlos'],
       'Idade':[23, None, 35,29],
       'Cidade':['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', None]} 

df = pd.DataFrame(data) 
print(df.isnull()) 
print(df.isnull().sum()) 

df_sem_na = df.dropna() 
print(df_sem_na) 

df_sem_na_col = df.dropna(axis=1)
print(df_sem_na_col) 

df['Idade'] = df['Idade'].fillna(df['Idade'].mean()) 
print(df)

# Correção aqui
df_sem_dup = df.drop_duplicates() 
print(df_sem_dup) 

df_sem_dup_nome = df.drop_duplicates(subset=['Nome'])
print(df_sem_dup_nome) 

data_tipos = {'Produto' : ['A', 'B', 'C'],
              'Preco' : ['10.5', '20.3', '30.2'],
             'Quantidade' : ['1', '2', '3']} 

df_tipos = pd.DataFrame(data_tipos) 

df_tipos['Preco'] = df_tipos['Preco'].astype(float) 
df_tipos['Quantidade'] = df_tipos['Quantidade'].astype(int)
print(df_tipos.dtypes) 

data_espacos = {'Nome' : ['Ana', 'Bruno', 'Carlos'],
               'Cidade' : ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte']}  

df_espacos = pd.DataFrame(data_espacos) 

df_espacos['Nome'] = df_espacos['Nome'].str.strip()
df_espacos['Cidade'] = df_espacos['Cidade'].str.strip()
print(df_espacos) 

data_outliers = {'Idade' : [23, 29, 35, 120, 28, 22, 25]} 

df_outliers = pd.DataFrame(data_outliers) 

media = df_outliers['Idade'].mean() 
desvio_padrao = df_outliers['Idade'].std() 

outliers = df_outliers[(df_outliers['Idade'] > media + 3*desvio_padrao)] 


df_sem_outliers = df_outliers[(df_outliers['Idade'] <= media + 2*desvio_padrao) &
                                (df_outliers['Idade'] >= media - 2*desvio_padrao)] 
print(df_sem_outliers)
