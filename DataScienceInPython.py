import pandas as pd
import statsmodels.api as sm
import numpy as np

df = pd.read_csv("binary.csv")

# create a dataframe
df_mydata = pd.DataFrame(df)

print(df_mydata.shape)
df_mydata = df_mydata.rename(columns={'rank': 'position'})

print(df_mydata.describe())
print(df_mydata.head())
for i in list(df_mydata.columns) :
    k = sum(pd.isnull(df_mydata[i]))
    print(i, k)

#Display name of month
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

# create a date object
x = datetime.datetime(2020, 5, 17)
print(x)

# reading files where r is for read and t is for text
f = open("demofile.txt", "rt")
print(f.read())

#loop through the lines of the file
f = open("demofile.txt", "r")
for x in f:
  print(x)

#append a line of text to the existig file
f = open("demofile.txt", "a")
f.write("Now the file has one more line!")

# delete the content
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")

# create a new file called myfile
#f1 = open("myfile3.txt", "x")
# create a new file if it does not exist
#f2 = open("myfile2.txt", "w")

# delete a file
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exists")