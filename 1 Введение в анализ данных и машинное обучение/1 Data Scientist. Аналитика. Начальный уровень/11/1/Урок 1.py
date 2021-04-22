#!/usr/bin/env python
# coding: utf-8

# ## Библиотека `NumPy` : часть 2

# ### Урок 4.1: Изменение размерности списков

# Импортируем библиотеку `NumPy`:

# In[1]:


import numpy as np


# Представим, что у нас есть массив оценок студентов `scores`:

# In[2]:


scores = np.array([3, 5, 7, 9, 8, 10])
scores


# И мы узнаём, что эти оценки должны быть записаны парами: студенты выполняли проект вдвоём, но оценки получили по отдельности по результатам защиты проекта. Как разбить шесть значений в массиве на маленькие списки по два значения? Воспользоваться методом `.reshape()`, который позволяет поменять форму массива.

# In[3]:


pairs = scores.reshape(3, 2)
pairs


# **Важно:** теперь изменилась не только форма массива, но и его размерность – запросим число измерений массива `pairs`:

# In[4]:


pairs.ndim


# In[5]:


scores.ndim  # сравним


# Теперь массив двумерный, и чтобы обратиться к элементу массива, нам нужно указывать две вещи: индекс списка и индекс элемента в этом списке. Метод `.reshape()` удобен, но при его использовании стоит помнить, что не любой массив можно превратить в массив другой формы – общее число элементов в массиве должно позволять получить новое число списков и элементов в них. Так, массив `pairs`, в котором всего 6 элементов, нельзя превратить в массив вида `(2, 4)` (таблица $2 \times 4$), потому что для такой формы понадобится 8 элементов! И Python явно об этом сообщит:

# In[16]:


pairs.reshape(2, 4)


# Если нам нужно просто поменять местами строки и столбцы в таблице, то есть списки в массиве, можно воспользоваться транспонированием, которое осуществляется в `NumPy` с помощью метода `.transpose()`:

# In[17]:


# было
pairs


# In[6]:


# стало
T = pairs.transpose() 
T


# Кроме того, в противоположность `.reshape()`, который часто используется для разбиения одномерного массива на многомерный из нескольких маленьких списков, в `NumPy` существует «обратный» метод `.ravel()`, который позволяет любой многомерный массив превратить в одномерный, состоящий из одного списка, другими словами, сделать массив «плоским»:

# In[49]:


pairs.ravel()


# *Примечание:* в `NumPy` есть ещё другой метод для создания «плоских» массивов – `flatten()`.

# На этом мы закончим обсуждать изменение размерности списков, а в следующем уроке поговорим об изменении элементов списков.
