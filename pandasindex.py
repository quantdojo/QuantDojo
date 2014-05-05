#http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/

#Setup

import pandas as pd
import numpy as np
from pandas import DataFrame, Series

df = DataFrame({'int_col' : [1,2,6,8,-1], 'float_col' : [0.1, 0.2, 0.2, 10.1, None], 'str_col' : ['a','b',None,'c','a']})

print(df)

#Indexing
print(---)
###

df[['float_col','int_col']]

print(df)

###

input()

