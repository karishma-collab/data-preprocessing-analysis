#Feature Scaling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import boxplot
from sklearn.preprocessing import StandardScaler, minmax_scale, MinMaxScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
dataset = pd.read_csv('loan.csv')
# print(dataset.head())
# print(dataset.isnull().sum())
# print(dataset.describe())
Q1 = dataset["ApplicantIncome"].quantile(.25)
Q3 = dataset["ApplicantIncome"].quantile(.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR
# print(lower_bound,upper_bound)
new_dataset = dataset[(dataset["ApplicantIncome"]>= lower_bound) & (dataset["ApplicantIncome"] <= upper_bound)]
# print(dataset.shape)
# print(new_dataset.shape)

new_dataset = new_dataset.reset_index(drop=True)
# print(new_dataset)
# sns.boxplot(x="ApplicantIncome",data=new_dataset)
# plt.show()
# print(new_dataset["ApplicantIncome"])
# applicant_income_before = sns.boxplot(x="ApplicantIncome",data=dataset)
# plt.show()
# print(new_dataset["ApplicantIncome"])
ss=StandardScaler()
app_income_scaling=ss.fit_transform(new_dataset[["ApplicantIncome"]])
# print(app_income_scaling)
new_dataset["ApplicantIncome_scale"]=pd.DataFrame(app_income_scaling,columns=["ApplicantIncome_scale"])
# # print(new_dataset["ApplicantIncome_scale"])
# plt.subplot(1,2,1)
# plt.title("Before Scaling")
# sns.boxplot(x="ApplicantIncome", data=new_dataset)
# plt.subplot(1,2,2)
# plt.title("After Scaling")
# sns.boxplot(x="ApplicantIncome_scale", data=new_dataset)
# plt.show()
plt.subplot(1,2,1)
plt.title("Before MinMax scaling")
sns.boxplot(x="ApplicantIncome_scale", data=new_dataset)

mm = MinMaxScaler()
app_min_max = mm.fit_transform(new_dataset[["ApplicantIncome"]])
new_dataset["ApplicantIncome_MinMax"]=pd.DataFrame(app_min_max,columns=["ApplicantIncome_MinMax"])
plt.subplot(1,2,2)
plt.title("After minmax Scaling")
sns.boxplot(x="ApplicantIncome_MinMax", data=new_dataset)
plt.show()
