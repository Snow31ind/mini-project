import numpy as np
import pandas as pd
import locale
from locale import atof
from datetime import datetime
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split


locale.setlocale(locale.LC_NUMERIC,'')

# Definition for Convert to Real float or Number
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

#
def time_convert(x):
    if type(x)==float or type(x)==int:
        return x
    if 'Dec' in x:
        return str(x.replace('Dec','12'))
    if 'Nov' in x:
        return str(x.replace('Nov','11'))
    if 'Oct' in x:
        return str(x.replace('Oct','10'))
    if 'Sep' in x:
        return str(x.replace('Sep','09'))
    if 'Aug' in x:
        return str(x.replace('Aug','08'))
    if 'Jul' in x:
        return str(x.replace('Jul','07'))
    if 'Jun' in x:
        return str(x.replace('Jun','06'))
    if 'May' in x:
        return str(x.replace('May','05'))
    if 'Apr' in x:
        return str(x.replace('Apr','04'))
    if 'Mar' in x:
        return str(x.replace('Mar','03'))
    if 'Feb' in x:
        return str(x.replace('Feb','02'))
    if 'Jan' in x:
        return str(x.replace('Jan','01'))
#
def time_convert2(x):
    x = str(x.replace(' ','/'))
    x = str(x.replace(',',''))
    dateobj=pd.to_datetime(x,format='%m/%d/%Y')
    return dateobj
#
# Arrange the main 
df = pd.read_csv('VNINDEX_2010-2022.csv',sep=',',thousands=',')
df['Vol.'] = df['Vol.'].apply(value_to_float)
df['Change %'] = df['Change %'].apply(percent_to_float)
df['Date'] = df['Date'].apply(time_convert)
df['Date'] = df['Date'].apply(time_convert2)
# 

#print(df.dtypes)
#print(df)
# Main part
#'''
features=['Price','Open','High','Low']
X = df[features] # features
y = df['Change %'] # target

# Splitting Data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1) # 70% training and 30% test

# Decision Tree classifer
clf = DecisionTreeClassifier()  # Creating
clf = clf.fit(X_train,y_train)  # Training
y_pred = clf.predict(X_test)    # Predict

#Print Evaluating
print("Classify Accuracy : ",metrics.accuracy_score(y_test,y_pred))
'''
X_reg = df['Date']  # features
y_reg = df['Vol.']  # traget
reg1 = DecisionTreeRegressor(max_depth=2)
reg2 = DecisionTreeRegressor(max_depth=5)

'''
