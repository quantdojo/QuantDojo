###From: http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/ ###

import pandas as pd
import numpy as np
from pandas import DataFrame, Series

###functions###

def some_fn(x):
    if type(x) is str:
        return 'applymap_' + x
    elif x:
        return 100 * x
    else:
        return


###

df = DataFrame({'int_col' : [1,2,6,8,-1], 'float_col' : [0.1, 0.2, 0.2, 10.1, None], 'str_col' : ['a','b',None,'c','a']})

print(df)

### 1. Indexing ###
print("---")
###

print(df[['float_col','int_col']])

### Conditional Indexing ###
print("---")
###

print(df[df['float_col'] > 0.15])
print(df[df['float_col'] == 0.1])
print(df[(df['float_col'] > 0.1) & (df['int_col']>2)])
print(df[(df['float_col'] > 0.1) | (df['int_col']>2)])
print(df[~(df['float_col'] > 0.1)])

### 2. Conditional Indexing ###
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

### 4. Map, Apply ###
print("---")
###

print(df['str_col'].dropna().map(lambda x : 'map_' + x))

print(df.ix[:,['int_col','float_col']].apply(np.sqrt))

print(df.ix[:,['int_col','float_col']].apply(np.sum))

print(df.applymap(some_fn))

### Vectorized mathematical and string operations ###

df = pd.DataFrame(data={"A":[1,2], "B":[1.2,1.3]})

df["C"] = df["A"]+df["B"]

print(df)

df["D"] = df["A"]*3

print(df)

df["E"] = np.sqrt(df["A"])

print(df)

df = pd.DataFrame(data={"A":[1,2], "B":[1.2,1.3], "Z":["a","b"]})

print(df)

df["F"] = df.Z.str.upper()

print(df)

### 5. Groupby ###

### tutorial didnt mention reseting df so reseting here ###
df = DataFrame({'int_col' : [1,2,6,8,-1], 'float_col' : [0.1, 0.2, 0.2, 10.1, None], 'str_col' : ['a','b',None,'c','a']})

grouped = df['float_col'].groupby(df['str_col'])

print(grouped.mean())

### 6. New Columns ###

df4 = df.copy()

def two_three_strings(x):
    return x*2, x*3

df4['twice'],df4['thrice'] = zip(*df4['int_col'].map(two_three_strings))

print(df4)

df5 = df.copy()

def sum_two_cols(series):
    return series['int_col'] + series['float_col']

df5['sum_col'] = df5.apply(sum_two_cols,axis=1)

print(df5)

import math

def int_float_squares(series):
 return pd.Series({'int_sq' : series['int_col']**2, 'flt_sq' : series['float_col']**2})

print(df.apply(int_float_squares, axis = 1))

### 7. Basic Stats ###

print(df.describe())
print(df.cov())
print(df.corr())

### 8. Merge and Join ###

print(df)
other = DataFrame({'str_col' : ['a','b'], 'some_val' : [1,2]})
print(other)
print(pd.merge(df,other,on='str_col',how='inner'))
print(pd.merge(df,other,on='str_col',how='outer'))
print(pd.merge(df,other,on='str_col',how='left'))
print(pd.merge(df,other,on='str_col',how='right'))

### 9. Plot ###

plot_df = DataFrame(np.random.randn(1000,2),columns=['x','y'])
plot_df['y'] = plot_df['y'].map(lambda x : x + 1)

plot_df.plot() ### plot not working???? ###

plot_df.hist() ### plot not working???? ###

### 10. Scikit-learn conversion ###

print(df)

print(df.values[:,:-1])

#print(df.values[:,:-1].astype(float32)) not working?

input()
