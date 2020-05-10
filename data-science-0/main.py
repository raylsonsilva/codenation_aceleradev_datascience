#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[145]:


black_friday.head(5)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[76]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[215]:


def q2():
    # Retorne aqui o resultado da questão 2.
    women = black_friday[black_friday['Gender']=='F']
    return women[women['Age']=='26-35'].shape[0]


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[112]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday['User_ID'].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[119]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return black_friday.dtypes.nunique()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[233]:


def q5():
    # Retorne aqui o resultado da questão 5.
    non_null_values = len(black_friday.dropna(axis=0, how='any'))
    null_values = len(black_friday) - non_null_values
    answer5 = null_values/len(black_friday)
    return answer5


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[240]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return black_friday['Product_Category_3'].isna().sum()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[275]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday['Product_Category_3'].dropna().mode().loc[0]


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[284]:


def q8():
    # Retorne aqui o resultado da questão 8.
    min=black_friday['Purchase'].min()
    max=black_friday['Purchase'].max()
    normalized_black_friday=(black_friday['Purchase']-min)/(max-min)
    return normalized_black_friday.mean().item()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[286]:


def q9():
    # Retorne aqui o resultado da questão 9.
    mean = black_friday['Purchase'].mean()
    std  = black_friday['Purchase'].std()
    normalized_black_friday = (black_friday['Purchase'] - mean)/(std)
    return normalized_black_friday.between(-1,1).sum().item() 


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[288]:


def q10():
    # Retorne aqui o resultado da questão 10.
    aux1 = black_friday[black_friday['Product_Category_2'].isna() == True]
    aux2 = black_friday.iloc[aux1.index,:].Product_Category_3.isna()
    return aux2.all().item()

