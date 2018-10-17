import pandas as pd 
#read data from a csv file
data=pd.read_csv("data/titanic.csv")
#print some of the top values
print(data.head())
#Description about the data
print(data.describe())
#get the values of a column
survived=data["Survived"]
print(survived)
#if you want to know the column names
col_names=data.columns
#Which returns a list of column names
print(col_names)