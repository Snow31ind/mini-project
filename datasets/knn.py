import numpy as np
import pandas as pd
import locale
from locale import atof
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

locale.setlocale(locale.LC_NUMERIC,'')

#Convert to Real float or Number
def value_to_float(x): # 10k -> 10,000
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
def percent_to_float(x): # 0.1% -> 0.001
    if type(x)==float or type(x)==int:
        return x
    if '%' in x:
        if len(x)>1:
            return float(x.replace('%',''))
    return 0.0
#

# Arrange the main 
df = pd.read_csv('VNINDEX_2010-2022.csv',sep=',',thousands=',') # 1,000 -> 1000
df['Vol.'] = df['Vol.'].apply(value_to_float)                   
df['Change %'] = df['Change %'].apply(percent_to_float)
# 

# KNN
#'''
features=['Price','Open','High','Low']
X = df[features] # features
y = df['Change %'] # target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1) # 70% training and 30% test

kclf=KNeighborsClassifier()     # Creating
kclf=kclf.fit(X_train,y_train)  # Training
y_pred=kclf.predict(X_test)     # Predict
#'''


#print(df.dtypes)
#print(df)
print("Accuracy : ",metrics.accuracy_score(y_test,y_pred))
