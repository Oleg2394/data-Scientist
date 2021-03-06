#!/usr/bin/env python
# coding: utf-8

# ### Урок 6.2. Применение функций: группировка и агрегирование

# In[2]:


import pandas as pd
import numpy as np 
df = pd.read_csv("WeightLoss.csv")
df['total'] = df['w1'] + df['w2'] + df['w3']
df['total_gr'] = df['total'] * 1000


# Иногда нас интересуют сводные характеристики не по всей таблице, а по группам: например, хочется посмотреть, сколько килограммов в сумме потеряли люди, которые сидели на диете и те, кто помимо диеты выполнял комплекс упражнений. Для группировки в `pandas`| используется метод `groupby()`:

# In[3]:


df.groupby('group')


# Результат как таковой от нас скрыт, это особый объект в `pandas`, результат представляет собой список пар «название группы и сам датафрейм». Чтобы увидеть пример результата явно, сконвертируем в список и посмотрим на первый элемент: 

# In[4]:


list(df.groupby('group'))[0]


# Теперь попробуем к каждой группе применить функцию, которая будет суммировать значения по каждому показателю в каждой группе. Тут не понадобится `.apply()`, есть специальный метод для агрегирования –  `agg()`.

# In[5]:


df.groupby('group').agg('sum')  # название функции - в кавычках


# А теперь посчитаем средние показателей по каждой группе:

# In[6]:


df.groupby('group').agg('mean')


# Если нужно применить сразу несколько функций, их можно оформить в виде списка. Найдем минимальное, максимальное и среднее значение показателей по каждой группе:

# In[7]:


df.groupby('group').agg(['min', 'max', 'mean'])


# Как и в случае с `.apply()`, внутри `.agg()` можно прописывать свои функции, но тогда уже их название должно идти без кавычек.
