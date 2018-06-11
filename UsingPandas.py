import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import datetime


# load the data from file
mydata=pd.read_csv("/Users/alket/PycharmProjects/MyProject1/sales.txt")
print(mydata)

# create a dataframe
df_mydata = pd.DataFrame(mydata)

# print dimensions and the first three rows
print(df_mydata.shape)
print(df_mydata.head(3))

# to summarize data
print(df_mydata.describe())

# to summarize all the character variables
print(df_mydata.describe(include=['O']))

# print some stats singularly
print("mean "+str(df_mydata.sales.mean()))
print("median "+str(df_mydata.sales.median()))
print("count "+str(df_mydata.sales.count()))
print("min "+str(df_mydata.sales.min()))
print("max "+str(df_mydata.sales.max()))

# access only one field of the data
print(df_mydata['sales'])

# filter rows from dataframe where data satisfies certain conditions
df1 = df_mydata[(df_mydata.Productcode == "Aa") & (df_mydata.sales >= 950)]
print(df1)

# in the same way we can use the method query
df2 = df_mydata.query('(Productcode == "Aa") & (sales >= 50)')
print(df2)

# sort the data against a certain field - sales
print(df_mydata.sort_values(['sales']))

#sort the data against certain filed - cost
print(df_mydata.sort_values(['cost']))

# you can use groupby the rows like in SQL
# to group the records in categories after applying a function such as mean
print(df_mydata.groupby(df_mydata.Productcode).mean())

# you can groupby also by single variable
print(df_mydata['sales'].groupby(df_mydata.Productcode).mean())

# plot an histagram of the data
plt.hist(df_mydata['sales'])
plt.show()

# plot a boxplot
plt.boxplot(df_mydata['sales'])
plt.show()


#dictionaries
words = {'apple': 'red','lemon': 'yellow'}
print(words)
print("the value associated to apple is "+str(words['apple']))

# print keys and values of a dictionary
print(words.keys())
print(words.values())



# datetime in Python
x = datetime.datetime.now()
print(x)