import numpy as np

from pandas import Series,DataFrame
import pandas as pd

#Lets create a Series (array of data and data labels, its index)

obj = Series([3,6,9,12])

#Show
obj

#Lets show the values
obj.values

#Lets show the index
obj.index

#Now lets create a Series with an index
#WW2 casualties 
ww2_cas = Series([8700000,4300000,3000000,2100000,400000],index=['USSR','Germany','China','Japan','USA'])

#Show
ww2_cas

#Now we can use index values to select Series values
ww2_cas['USA']

#Can also check with array operations
#Check who had casualties greater than 4 million
ww2_cas[ww2_cas > 4000000]

#Can treat Series as ordered dictionary
#Check if USSR is in Series
'USSR' in ww2_cas

#Can convert Series into Python dictionary
ww2_dict = ww2_cas.to_dict()

#Show
ww2_dict

#Can convert back into a Series
WW2_Series = Series(ww2_dict)

#Show
WW2_Series

#Passing a dictionary the index will have the dict keys in order
countries = ['China','Germany','Japan','USA','USSR','Argentina']

#Lets redefine a Series
obj2 = Series(ww2_dict,index=countries)

#Show
obj2

#We can use isnull and notnull to find missing data
pd.isnull(obj2)

#obj2.isnull()

#Same for the opposite
pd.notnull(obj2)

#obj2.notnull()

#Lets see the ww2 Series again
WW2_Series

#Lets check our Series with Argentine again
obj2

#Now we can add and pandas automatically aligns data by index
WW2_Series + obj2

#We can give Series names
obj2.name = "World War 2 Casualties"

#Show
obj2

#We can also name index
obj2.index.name = 'Countries'

#Show
obj2

#Next we'll learn DataFrames!
