#Now we'll learn about Selecting Entries
import numpy as np
from pandas import Series,DataFrame
import pandas as pd

#Lets try some Series indexing
ser1 = Series(np.arange(3),index=['A','B','C'])

#multiply all values by 2, to avoid confusion in future
ser1 = 2*ser1

#Show
ser1

#Can grab entry by index name
ser1['B']

#Or grab by index 
ser1[1]

#Can also grab by index range
ser1[0:3]

#Or grab range by range of index values
ser1[['A','B','C']]

#Or grab by logic
ser1[ser1>3]

#Can also ser using these methods
ser1[ser1>3] = 10

#Show
ser1

#Now let's see selection in a DataFrame
dframe = DataFrame(np.arange(25).reshape((5,5)),index=['NYC','LA','SF','DC','Chi'],columns=['A','B','C','D','E'])

#Show
dframe

#Select by column name
dframe['B']

#Select by multiple columns
dframe[['B','E']]

#Can also use boolean
dframe['C']>8
dframe[dframe['C']>8]

#Can also just show a boolean DataFrame
dframe > 10

#Can also use ix as previously discussed to label-index
dframe.loc['LA']

#Another example
dframe.iloc[1]

#Next we'll learn about data alignment!