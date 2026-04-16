# outliers remove in dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from dataCleaning.dataClean2 import new_dataset

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# age = [22,21,19,23,24,98]
# print(np.mean(age))
dataset = pd.read_csv('loan.csv')
# print(dataset.shape)
# print(dataset.isnull().sum())
# print(dataset.describe())
# sns.boxplot(x="ApplicantIncome",data=dataset)
# plt.show()
#####Interquartile(IQR) range to remove outliers ###
# print(dataset["ApplicantIncome"].isnull().sum())
# Q1 = dataset["ApplicantIncome"].quantile(.25)
# Q3 = dataset["ApplicantIncome"].quantile(.75)
# IQR = Q3 - Q1
# lower_bound1 = Q1 - 1.5*IQR # -1498.75
# upper_bound1 = Q3 + 1.5*IQR # 10171.25
# print(lower_bound,upper_bound)
# print(dataset.shape)
# dataset_new = dataset[(dataset["ApplicantIncome"]>= lower_bound1) & (dataset["ApplicantIncome"] <= upper_bound1)]
# print(dataset.shape) # 614
# print(dataset_new.shape) # 564
# print(((614-564)/614)*100)
# plt.subplot(1,2,1)
# plt.title("Applicant Income Before Outlier Removal")
# sns.boxplot(x="ApplicantIncome",data=dataset)
# plt.subplot(1,2,2)
# plt.title("Applicant Income after Outlier Removal")
# sns.boxplot(x="ApplicantIncome",data=dataset_new)
# plt.show()
# ################### normalization curve ########
# lower_bound2 = (dataset["ApplicantIncome"].mean()) - (3*dataset["ApplicantIncome"].std())
# upper_bound2 = (dataset["ApplicantIncome"].mean()) + (3*dataset["ApplicantIncome"].std())
# # print(lower_bound,upper_bound)
# new_dataset = dataset[(dataset["ApplicantIncome"] >= lower_bound2) & (dataset["ApplicantIncome"] <= upper_bound2)]
# # print(new_dataset.shape) # 606
# plt.subplot(2,2,1)
# plt.title("Applicant Income Before Outlier Removal using IQR method")
# sns.boxplot(x="ApplicantIncome",data=dataset)
# plt.subplot(2,2,2)
# plt.title("Applicant Income after Outlier Removal using IQR method")
# sns.boxplot(x="ApplicantIncome",data=dataset_new)
# plt.subplot(2,2,3)
# plt.title("Applicant Income after Outlier Removal using normalize curve method")
# sns.boxplot(x="ApplicantIncome",data=dataset)
# plt.subplot(2,2,4)
# plt.title("Applicant Income after Outlier Removal using normalize curve method")
# sns.boxplot(x="ApplicantIncome",data=new_dataset)
# plt.show()
#####Z-score#####
dataset["zscore"]=(dataset["ApplicantIncome"]-dataset["ApplicantIncome"].mean())/dataset["ApplicantIncome"].std()
# print(dataset["zscore"])
new_dataset = dataset[dataset["zscore"]<3]
print(new_dataset.shape)#606