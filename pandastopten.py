###From: http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/ ###

import pandas as pd
import numpy as np
from pandas import DataFrame, Series

df = DataFrame({'int_col' : [1,2,6,8,-1], 'float_col' : [0.1, 0.2, 0.2, 10.1, None], 'str_col' : ['a','b',None,'c','a']})

print(df)

### 1. Indexing ###
print("---")
###

print(df[['float_col','int_col']])

### 2. Conditional Indexing ###
print("---")
###

print(df[df['float_col'] > 0.15])
print(df[df['float_col'] == 0.1])
print(df[(df['float_col'] > 0.1) & (df['int_col']>2)])
print(df[(df['float_col'] > 0.1) | (df['int_col']>2)])
print(df[~(df['float_col'] > 0.1)])

### 3. Conditional Indexing ###
print("---")
###
df2 = df.rename(columns={'int_col' : 'some_other_name'})
print(df2)
df2.rename(columns={'some_other_name' : 'int_col'}, inplace = True)
print(df2)

### 3. Handling Missing Values ###
print("---")
###

print(df2)
print(df2.dropna())
df3 = df.copy()
mean = df3['float_col'].mean()
print(df3)
print(df3['float_col'].fillna(mean))

input()

