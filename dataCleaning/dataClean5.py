import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
dataset = pd.read_csv("titanic.csv")
# print(dataset.head())
# print(dataset.shape)
# print(dataset.isnull().sum())
# print(dataset.describe())
Q1 = dataset["Fare"].quantile(.25)
Q3 = dataset["Fare"].quantile(.75)
IQR = Q3 - Q1
lower_bound1 = Q1 - 1.5*IQR
upper_bound1 = Q3 + 1.5*IQR
print(lower_bound1,upper_bound1)
new_dataset = dataset[(dataset["Fare"]>= lower_bound1) & (dataset["Fare"] <= upper_bound1)]
print(dataset.shape)#891
print(new_dataset.shape)#775
f_mean = new_dataset["Fare"].mean()
f_mode = new_dataset["Fare"].mode()[0]
f_mid = new_dataset["Fare"].median()
# print(f_mean,f_mode,f_mid)
sns.histplot(x="Fare", data=new_dataset)
plt.plot([f_mean for i in range (0,275)],[i for i in range (0,275)],color="red",label="mean")
plt.plot([f_mode for i in range (0,275)],[i for i in range (0,275)],color="blue",label="mode")
plt.plot([f_mid for i in range (0,275)],[i for i in range (0,275)],color="green",label="median")
plt.legend(loc="upper right")
plt.show()
