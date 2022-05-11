import numpy as np
import pandas as pd
from pandas import read_csv
import locale
from locale import atof
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import pydotplus
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

locale.setlocale(locale.LC_NUMERIC,'')

#Convert to Real float or Number
def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0
#
def percent_to_float(x):
    if type(x)==float or type(x)==int:
        return x
    if '%' in x:
        if len(x)>1:
            return float(x.replace('%',''))
    return 0.0
#
df = pd.read_csv('VNINDEX_2010-2022.csv',sep=',',thousands=',')
#print(df)
df['Vol.'] = df['Vol.'].apply(value_to_float)
df['Change %'] = df['Change %'].apply(percent_to_float)
# 

#print(df.dtypes)

# what is data and target

