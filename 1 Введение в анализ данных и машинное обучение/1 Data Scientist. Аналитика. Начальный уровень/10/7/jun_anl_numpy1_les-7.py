#!/usr/bin/env python
# coding: utf-8

# ### Урок 3.7 – Условия и булевы массивы

# Прежде, чем обсуждать формулировку условий для массивов, давайте немного поговорим об условиях вообще, а именно, про проверку условий на переменных в Python. Создадим две переменные `a` и `b` и присвоим им какие-нибудь значения:

# In[2]:


a = 6
b = 9


# Проверим, правда ли, что `b` больше `a`:

# In[3]:


b > a  # правда


# Теперь проверим более сложное условие – правда ли, что `b` не менее `a` (больше или равно):

# In[4]:


b >= a  # правда


# Простое условие, условие равенства, проверяется в Python с помощью двойного знака `=` (одинарное «равно» используется для присваивания значений). Правда ли, что `a` равно `b`?

# In[5]:


a == b  # конечно, нет


# Теперь перейдём к массивам. Для начала создадим массив, содержащий значения возрастов людей в трёх группах:

# In[6]:


import numpy as np


# In[7]:


ages = np.array([[15, 23, 32, 45, 52], 
               [68, 34, 55, 78, 20], 
               [25, 67, 33, 45, 14]])


# Давайте попробуем узнать, какие значения массива соответствуют людям трудоспособного возраста: от 16 лет и старше:

# In[8]:


M = ages >= 16  # больше или равно
M


# Все элементы, кроме первого в первом списке и кроме последнего в последнем списке: на всех позициях, кроме указанных, стоят значения `True`, что означает, что условие выполняется. То, что мы получили сейчас – это булев массив, массив, состоящий из булевых (логических) значений, значений `True` и `False`. 
# 
# Теперь попробуем сформулировать более сложное условие: проверим, какие элементы соответствуют людям старше 18, но младше 60 лет:

# In[9]:


work = (ages > 18) & (ages < 60) # & - одновременное условие
work


# Как посчитать, сколько элементов массива удовлетворяют некоторым условиям?

# Суммируем значения по всему массиву: Python понимает, что значение `True` – это 1, а `False` – это 0, поэтому нет необходимости превращать все значения в числовые, мы можем просто сложить все «единички»:

# In[10]:


work.sum()


# А теперь проверим, какие значения соответствуют людям либо младше 18, либо старше 60:

# In[11]:


(ages < 18) | (ages > 60)  # | - или - хотя бы одно условие верно


# А как увидеть сами значения, которые удовлетворяют определенным условиям? Заключить условие в квадратные скобочки:

# In[12]:


ages[ages >= 16]


# Итак, мы уже познакомились с тремя способами выбирать элементы из массива: 
# 
# * в квадратных скобках можно указать номер или индекс интересующего нас элемента;
# * последовательность индексов через `:` (получаем срез);
# * условие.
# 
# Логика выбора элементов по условиям такая: Python выбирает только те элементы, где условие возвращает значение `True` (вспомните, как выглядят булевы массивы и попытайтесь сопоставить). 
# 
# Сформулируем более сложное условие:

# In[13]:


ages[(ages >= 16) & (ages < 60)]


# Внимание: не забудьте круглые скобки для каждого условия, иначе Python поймёт всё неправильно и вернёт ошибку:

# In[14]:


ages[ages >= 16 & ages < 60]


# На этом мы завершим модуль, посвященный введению в `NumPy`, а в следующем модуле поговорим про изменение массивов и более продвинутые действия с массивами.
