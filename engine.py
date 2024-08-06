# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 21:18:25 2022

@author: doguilmak

dataset: https://www.kaggle.com/datasets/edoardoba/fitness-exercises-with-animations

"""

#%%
# 1. Libraries

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#%%
# 2. Data Preprocessing

# 2.1. Uploading data
df = pd.read_csv('fitness_exercises.csv')
print(df.isnull().sum())
print(list(df.columns))
print("\n", df.head(10))
print(df.info())

#  2.2. Dropping unnecessary column (id)
print("{} duplicated data.".format(df.duplicated().sum()))

#%%
# 3. Seperate columns

bodyPart = df['bodyPart']
print(bodyPart.unique())

target = df['target']
print(target.unique())

equipment = df['equipment']
print(equipment.unique())

exercise_id = df['id']

#%%
# 4. Filtering exercises

len(df[(df.bodyPart == 'waist') & (df.target == 'abs')])
print(df[(df.bodyPart == 'waist') & (df.target == 'abs')])

len(df[(df.bodyPart == 'upper legs') & (df.target == 'quads')])
print(df[(df.bodyPart == 'upper legs') & (df.target == 'quads')])

recommend = pd.DataFrame()
recommend = df.loc[df['bodyPart'].isin(['upper legs']) & df['target'].isin(['quads'])]
length=len(recommend.index)

for i in range(0, length):
    print('\n\n', i)
    print(recommend.bodyPart.iloc[i])
    print(recommend.equipment.iloc[i])
    print(recommend.name.iloc[i])
    print(recommend.target.iloc[i])

