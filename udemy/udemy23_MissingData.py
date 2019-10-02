import numpy as np
from pandas import Series,DataFrame
import pandas as pd

#Now we'll learn how to deal with missing data, a very common task when analyzing datasets!
data = Series(['one','two', np.nan, 'four'])

#Show data
data

#Find the missing values
data.isnull()

#We can simply drop the NAN
data.dropna()

# In a DataFrame we need to be a little more careful!
dframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])

#Show
dframe

clean_dframe = dframe.dropna()

#Show
clean_dframe
#Note all rows where an NA occured was a drop of the entire row

#We can also specify to only drop rows that are complete missing all data
dframe.dropna(how='all')

#Or we can specify to drop columns with missing data
dframe.dropna(axis=1)
#This should drop all columns out since every column contains at least 1 NAN

#We can also threshold teh missing data as well
#For example if we only want rows with at least 3 data points
dframe2 = DataFrame([[1,2,3,np.nan],[2,np.nan,5,6],[np.nan,7,np.nan,9],[1,np.nan,np.nan,np.nan]])

#Show
dframe2

#Droping any rows that don't have at least 2 data points
dframe2.dropna(thresh=2)

#Droping rows without at least 3 data points
dframe2.dropna(thresh=3)

#We can also fill any NAN
dframe2.fillna(1)

#Can also fill in diff values for diff columns
dframe2.fillna({0:0,1:1,2:2,3:3})

#Note that we still have access to the original dframe
dframe2

#If we want to modify the exsisting object, use inplace
dframe2.fillna(0,inplace=True)

#Now let's see the dframe
dframe2

#Awesome! Next we'll learn about Index Hierarchy