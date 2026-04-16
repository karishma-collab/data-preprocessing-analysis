import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
dataset = pd.read_csv('loan.csv')
sm = SimpleImputer(strategy='mean')
data = sm.fit_transform(dataset.select_dtypes(include=['float64', 'int64']))
# print(data)
# print(dataset.select_dtypes(include=['float64', 'int64']).columns)
data2 = pd.DataFrame(data, columns=dataset.select_dtypes(include=['float64', 'int64']).columns)
sm2 = SimpleImputer(strategy='most_frequent')
data_mode = sm2.fit_transform(dataset.select_dtypes(include='str'))
data2 = pd.DataFrame(data_mode, columns=dataset.select_dtypes(include=['object', 'string']).columns)
# print(data2.head())
# print(data2.isnull().sum())
# #### Label encoding (nominal encoding)
# courses = {"name":["c","python","c++","ai/ml"]}
# # print(courses)
# df_new = pd.DataFrame(courses)
# print(df_new)
# le = LabelEncoder()
# le.fit(courses["name"])
# df_new["course_encoding"]=le.transform(df_new.name)
# df_new["name"]=df_new["course_encoding"]
# print(df_new)
dataset=pd.read_csv('loan.csv')
data=["Property_Area"]
dataset = pd.read_csv('loan.csv')

data = dataset["Property_Area"]   # ✅ get actual column
data2 = pd.DataFrame(data)

print(data2)

le = LabelEncoder()
le.fit(data2["Property_Area"])   # ✅ pass 1D

data2["course_encoding"] = le.transform(data2["Property_Area"])
data2["name"] = data2["course_encoding"]

print(data2)
# le = LabelEncoder()
# data2["Property_Area_Encoding"] = le.fit_transform(data2["Property_Area"])
# print(data2["Property_Area_Encoding"])