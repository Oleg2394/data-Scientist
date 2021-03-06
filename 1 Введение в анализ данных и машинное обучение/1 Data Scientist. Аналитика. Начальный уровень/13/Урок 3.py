#!/usr/bin/env python
# coding: utf-8

# ### Урок 6.3. Сортировка и упорядочение

# In[3]:


import pandas as pd
import numpy as np 
df = pd.read_csv("WeightLoss.csv")
df['total'] = df['w1'] + df['w2'] + df['w3']
df['total_gr'] = df['total'] * 1000


# Попробуем отсортировать строки в таблице по значениям в каком-нибудь столбце. Для этого нам пригодится метод `.sort_values()`. Отсортируем строки по показателю `total`:

# In[4]:


df.sort_values('total')


# Сортировка может происходить по нескольким столбцам сразу. Например, давайте сделаем так, чтобы вначале шли люди, которые меньше всего сбросили килограммов за три месяца и чья самооценка в последний месяц была небольшой:

# In[5]:


df.sort_values(['total', 'se3'])


# По умолчанию сортировка происходит по возрастанию, но это можно поправить:

# In[6]:


df.sort_values(['total', 'se3'], ascending = False)


# По умолчаю изменения исходного датафрейма не происходит, но это можно исправить, добавив опцию `inplace=True`. Тогда строки в исходном датасете поменяют своё расположение в соответствии с выбранной сортировкой.
