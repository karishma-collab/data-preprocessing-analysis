import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
dataset = pd.read_csv('loan.csv')
# print(dataset.shape)
# print(dataset.head())
# dataset = dataset.fillna(0)
# print(dataset.isnull().sum())
# print(dataset.head(20))
# dataset = dataset.ffill()
# dataset = dataset.bfill(axis=1)
# print(dataset.head(20))
# loan_avg = dataset["LoanAmount"].mean()
# print(loan_avg) #146.41216216216216
# dataset["LoanAmount"]= dataset["LoanAmount"].fillna(loan_avg)
# print(dataset["LoanAmount"].isnull().sum())
# print(dataset.head())
# print(dataset["LoanAmount"].mean()) # 146.41216216216216
# print(dataset.info())
# print(dataset.select_dtypes(include=["int64","float64"]).columns)
for i in dataset.select_dtypes(include=["int64", "float64"]).columns:
    dataset[i] = dataset[i].fillna(dataset[i].mean())
for i in dataset.select_dtypes(include="str").columns:
    dataset[i] = dataset[i].fillna(dataset[i].mode()[0])
# print(dataset.isnull().sum())
# print(dataset["Gender"].mode()[0])
# print(dataset["Gender"].unique())
# print(dataset["Gender"].value_counts())
# print(dataset.isnull().sum())
# print(dataset.head())
new_dataset = dataset[["Gender","Married"]]
# print(new_dataset.shape)
# g_dummy = pd.get_dummies(new_dataset)
# print(g_dummy.info()) # Gender_Female  Gender_Male  Married_No  Married_Yes
ohe = OneHotEncoder(drop="first")
# ohe.fit(new_dataset)
encoding = ohe.fit_transform(new_dataset).toarray()
# print(encoding)
new_dataset2 = pd.DataFrame(encoding,columns=["Gender","Married"])
# print(new_dataset2)
dataset["Gender"]=new_dataset2["Gender"]
dataset["Married"]=new_dataset2["Married"]
print(dataset.head(10))
# data_preprocessing.py file name