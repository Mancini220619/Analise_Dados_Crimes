#!/usr/bin/env python
# coding: utf-8

# # Etapa de analise de dados
# 
# 1. Indice de crimes por ano e total de crimes individuais
# 2. Indice de crimes de todos os anos por municipio
# 3. Filtro por ano, mes , cidade e crime
# 
# 
# # Dicionário de Dados
# 
# 
# <!DOCTYPE html>
# <html>
# <head>
# <style>
# table {
#   font-family: arial, sans-serif;
#   border-collapse: collapse;
#   width: 50%;
# }
# 
# td, th {
#   border: 1px solid #dddddd;
#   text-align: left;
#   padding: 8px;
# }
# 
# tr:nth-child(even) {
#   background-color: #dddddd;
# }
# </style>
# </head>
# <body>
# 
# <h2>Colunas</h2>
# 
# <table>
#   <tr>
#     <th>Nome</th>
#     <th>Descrição</th>
#     </tr>
#   <tr>
#     <td>ano</td>
#     <td>Ano</td>
#   </tr>
#   <tr>
#     <td>mes</td>
#     <td>Mes</td>
#   </tr>
#   <tr>
#     <td>id_municipio</td>
#     <td>ID Município - IBGE 7 Dígitos</td>
#   </tr>
#   <tr>
#     <td>regiao_ssp</td>
#     <td>Região definida pela SSP</td>
#   </tr>
#   <tr>
#     <td>homicidio_doloso</td>
#     <td>Homicídio doloso inclui homicídio doloso por acidente de trânsito</td>
#   </tr>
#   <tr>
#     <td>numero_de_vitimas_em_homicidio_doloso</td>
#     <td>Número de vítimas em homicídio doloso inclui número de vítimas de homicídio doloso por acidente de trânsito	</td>
#   </tr>
#   <tr>
#     <td>homicidio_doloso_por_acidente_de_transito</td>
#     <td>Homicídio doloso por acidente de trânsito</td>
#   </tr>
#   <tr>
#     <td>numero_de_vitimas_em_homicidio_doloso_por_acidente_de_transito</td>
#     <td>Número de vítimas de homicídio doloso por acidente de trânsito</td>
#   </tr>
#   <tr>
#     <td>homicidio_culposo_por_acidente_de_transito</td>
#     <td>Homicídio culposo por acidente de trânsito</td>
#   </tr>
#   <tr>
#     <td>homicidio_culposo_outros</td>
#     <td>Outros tipos de Homicídio Culposo</td>
#   </tr>
#   <tr>
#     <td>tentativa_de_homicidio</td>
#     <td>Tentativa de homicídio</td>
#   </tr>
#   <tr>
#     <td>lesao_corporal_seguida_de_morte</td>
#     <td>Lesão corporal seguida de morte</td>
#   </tr>
#   <tr>
#     <td>lesao_corporal_dolosa</td>
#     <td>Lesão corporal dolosa</td>
#   </tr>
#   <tr>
#     <td>lesao_corporal_culposa_por_acidente_de_transito</td>
#     <td>Lesão corporal culposa por acidente de trânsito</td>
#   </tr>
#   <tr>
#     <td>lesao_corporal_culposa_outras</td>
#     <td>Outros tipos de lesão corporal culposa</td>
#   </tr>
#   <tr>
#     <td>latrocinio</td>
#     <td>Latrocínio</td>
#   </tr>
#   <tr>
#     <td>numero_de_vitimas_em_latrocinio</td>
#     <td>Número de vítimas em latrocínio</td>
#   </tr>
#   <tr>
#     <td>total_de_estupro</td>
#     <td>Soma de estupro e estupro de vulnerável</td>
#   </tr>
#   <tr>
#     <td>estupro</td>
#     <td>Estupro</td>
#   </tr>
#   <tr>
#     <td>estupro_de_vulneravel</td>
#     <td>Estupro de vulnerável</td>
#   </tr>
#   <tr>
#     <td>total_de_roubo_outros</td>
#     <td>Soma de roubo - outros, roubo de carga e roubo a banco</td>
#   </tr>
#   <tr>
#     <td>roubo_outros</td>
#     <td>Outros tipos de roubos</td>
#   </tr>
#   <tr>
#     <td>roubo_de_veiculo</td>
#     <td>Roubo de veículo</td>
#   </tr>
#   <tr>
#     <td>roubo_a_banco</td>
#     <td>Roubo a banco</td>
#   </tr>
#   <tr>
#     <td>roubo_de_carga</td>
#     <td>Roubo de carga</td>
#   </tr>
#   <tr>
#     <td>furto_outros</td>
#     <td>Outros tipos de furto</td>
#   </tr>
#   <tr>
#     <td>furto_de_veiculo</td>
#     <td>Furto de veiculo</td>
#   </tr>
# 
# </table>
# 
# </body>
# </html>
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('SSP 2017 a 2021.csv')
df.head(10)


# In[2]:


df.describe() # estatistica dos dados


# In[3]:


df.info() #resumo, tipo do dado


# In[4]:


df.head() #verifica as 5 primeiras linhas


# In[5]:


df.tail() #verifica as ultimas 5 linhas


# In[6]:


df.shape #saber o tamamho da base Linhas|Colunas


# In[7]:


display(df) #visualiza base e tamanho


# In[8]:


df.isnull().sum() #verifica nulos, somatório de colunas com nulos e seus totais


# In[9]:


df.fillna(0, inplace=True) #preenche com zero todos os campos em branco


# In[10]:


df.isnull().sum() #somatório de colunas com nulos e seus totais


# In[11]:


df.dtypes


# In[12]:


#df2 = df.copy() #cópia do data frame


# In[13]:


df.columns #nome das colunas
df


# # Indice de crimes por anos e total de crimes individuais

# In[15]:


df2 = df.groupby('ano')[['homicidio_doloso','numero_de_vitimas_em_homicidio_doloso','homicidio_doloso_por_acidente_de_transito','numero_de_vitimas_em_homicidio_doloso_por_acidente_de_transito','homicidio_culposo_por_acidente_de_transito','homicidio_culposo_outros', 'tentativa_de_homicidio','lesao_corporal_seguida_de_morte', 'lesao_corporal_dolosa','lesao_corporal_culposa_por_acidente_de_transito','lesao_corporal_culposa_outras', 'latrocinio','numero_de_vitimas_em_latrocinio','total_de_estupro', 'estupro','estupro_de_vulneravel', 'total_de_roubo_outros', 'roubo_outros','roubo_de_veiculo', 'roubo_a_banco', 'roubo_de_carga', 'furto_outros','furto_de_veiculo']].sum()
df2 = df2.reset_index()
df2


# In[16]:


df2.plot.barh(x='ano', figsize=(20, 12))

plt.xlabel('Quantidade de Crimes')
plt.ylabel('Ano')
plt.title('Crimes por Ano')
plt.show()


# #### Ao visualizar o grafico notamos que em comparação com o anos de 2018  e 2021 notamos uma diminuição no numero de crimes cometidos

# # Indice de crimes de todos os anos por municipio

# In[17]:


todos_municipios = df.groupby('regiao_ssp')[['homicidio_doloso','numero_de_vitimas_em_homicidio_doloso','homicidio_doloso_por_acidente_de_transito','numero_de_vitimas_em_homicidio_doloso_por_acidente_de_transito','homicidio_culposo_por_acidente_de_transito','homicidio_culposo_outros', 'tentativa_de_homicidio','lesao_corporal_seguida_de_morte', 'lesao_corporal_dolosa','lesao_corporal_culposa_por_acidente_de_transito','lesao_corporal_culposa_outras', 'latrocinio','numero_de_vitimas_em_latrocinio','total_de_estupro', 'estupro','estupro_de_vulneravel', 'total_de_roubo_outros', 'roubo_outros','roubo_de_veiculo', 'roubo_a_banco', 'roubo_de_carga', 'furto_outros','furto_de_veiculo']].sum().reset_index()
todos_municipios


# In[18]:


todos_municipios.set_index('regiao_ssp').plot(kind='bar', figsize=(15, 6))
plt.xlabel('Região SSP')
plt.ylabel('Número de Crimes')
plt.title('Crimes por Região SSP')
plt.legend(loc='upper right', fontsize='x-small')
#plt.legend(loc='upper left')

# Mostrar o gráfico
plt.show()


# #### Ao analisar o gráfico notamos que a capital comparada as outras cidades é a mais violenta em numero de crimes

# # Filtro por ano, mes , cidade e crime

# In[19]:


exibicao = df[['ano', 'mes', 'regiao_ssp', 'roubo_a_banco']]
exibicao.query('ano == 2018 and regiao_ssp == "Capital" and roubo_a_banco != 0').reset_index(drop=True) #query 


# #### filtragem por ano, mes, cidade e crime especifico
