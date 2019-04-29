# 多元线性回归
import pandas as pd
import  matplotlib as plt
colums = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceration', 'model-year', 'origin', 'car-name']
cars = pd.read_table('auto-mpg.data', delim_whitespace=True, names=colums)
print(cars.head(2))

feature_cols = ['cylinders', 'displacement', 'weight', 'acceration']
xdata=cars[feature_cols]
print(type(xdata.loc[0, 'cylinders']))

xdata['cylinders'] = xdata['cylinders'].astype('float64')
xdata['displacement'] = xdata['displacement'].astype('float64')
xdata['weight'] = xdata['weight'].astype('float64')
xdata['acceration'] = xdata['acceration'].astype('float64')

ydata = cars['mpg']


#构造训练集和测试集
from sklearn.model_selection import train_test_split