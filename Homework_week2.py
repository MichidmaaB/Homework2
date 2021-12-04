#Homework of week 2
#working directory 

import pandas as pd
import os
import numpy as np
os.getcwd() 

df = pd.read_excel("/Users/user/Documents/python/Introduction_Python_Nov21/week2/data/data.xlsx")

#Task 1
#pandas dr nuhtsul tavin ylgah
df[(df["age"]>25) & (df["gender"] == "F")][["firstName","age"]]
df.to_csv("women_over25.csv")

df[(df["age"]<23) & (df["gender"] == "M")][["firstName","age"]]
df.to_json("men_below23.json")

#loop ashiglan tuuh


#Task 2
df.iloc[27,1:6]

df.loc[25:28,("firstName","age")]

df.groupby('gender')['salary'].mean()
df.groupby("gender")['salary'].max()
df.groupby("gender")['salary'].min()

df_by_gender= df.groupby("gender")
df_by_gender.describe()
df_salary = df_by_gender['salary']
df_salary.describe()
df_age = df_by_gender['age']
df_age.describe()

table = pd.pivot_table(df, values='salary' , index='gender',
                       aggfunc={'salary' : [min, max, np.mean ]})
table

#Task 3
