#Now we'll learn about dropping entries
import numpy as np
from pandas import Series,DataFrame
import pandas as pd

#Create a new series to play with
ser1 = Series(np.arange(3),index=['a','b','c'])

#Show
ser1

#Now let's drop an index
ser1.drop('b')

#With a DataFrame we can drop values from either axis
dframe1 = DataFrame(np.arange(9).reshape((3,3)),index=['SF','LA','NY'],columns=['pop','size','year'])

#Show (remember just random values)
dframe1

#Now dropping a row
dframe1.drop('LA')

#Or we could drop a column
#Need to specify that axis is 1, not 0
dframe1.drop('year',axis=1)

#Next we'll learn about selecting entires in a DataFrame!
