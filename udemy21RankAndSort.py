import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#Sorting by index
ser1 = Series(range(3),index=['C','A','B'])

#show
ser1

#Now sort_index
ser1.sort_index()

#Can sort a Series by its values
ser1.sort_values()

#Lets see how ranking works
from numpy.random import randn
ser2 = Series(randn(10))

#Show
ser2

#This will show you the rank used if you sort the series
ser2.rank()

#Lets sort it now
ser2.sort_values()

#Show
ser2

#After sorting let's check the rank and see iof it makes sense
ser2.rank()

#On the left column we see th original index value and on the right we see it's rank!

#Next we'll learn about using descriptive statistics on dataframes!