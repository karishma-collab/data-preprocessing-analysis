#Drop Duplicate Values
import pandas as pd
data = {"name":["a","b","c","d","a","c","e"],
        "maths":[80,90,95,87,80,96,67],
        "english":[90,67,78,88,90,84,79]}
df=pd.DataFrame(data)
print(df.shape)
# print(df)
# df["duplicate"]=df.duplicated()
df.drop_duplicates(inplace=True)
print(df.shape)