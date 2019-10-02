# Now we'll learn how to merge data sets by linking rows by keys.

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Let's make a dframe

dframe1 = DataFrame({'key':['X','Z','Y','Z','X','X'],'data_set_1': np.arange(6)})

#Show
dframe1

#Now lets make another dframe

dframe2 = DataFrame({'key':['Q','Y','Z'],'data_set_2':[1,2,3]})

#Show
dframe2

# Now we can use merge the dataframes, this is a "many-to-one" situation
# Merge will automatically choose overlapping columns to merge on
pd.merge(dframe1,dframe2)
#Note no overlapping 'X's

# We could have also specified which column to merge on
pd.merge(dframe1,dframe2,on='key')

# We can choose which DataFrame's keys to use, this will choose left (dframe1)
pd.merge(dframe1,dframe2,on='key',how='left')

# Choosing the one on the right (dframe2)
pd.merge(dframe1,dframe2,on='key',how='right')

#Choosing the "outer" method selects the union of both keys
pd.merge(dframe1,dframe2,on='key',how='outer')

#Now we'll learn about a many to many merge

# Nnote that these DataFrames contain more than one instance of the key in BOTH datasets

dframe3 = DataFrame({'key': ['X', 'X', 'X', 'Y', 'Z', 'Z'],'data_set_3': range(6)})
dframe4 = DataFrame({'key': ['Y', 'Y', 'X', 'X', 'Z'], 'data_set_4': range(5)})

#Show the merge
pd.merge(dframe3, dframe4)

"""
So what happened? A many to many merge results in the product of the rows.
Because there were 3 'X's in dframe3 and 2 'X's in dframe4 there ended up being a total of 6 'X' rows in the result (2*3=6)!
Note how dframe3 repeats its 0,1,2 values for 'X' and dframe4 repeats its '2,3' pairs throughout the key set. 
"""

# We can also merge with multiple keys!
# Dframe on left
df_left = DataFrame({'key1': ['SF', 'SF', 'LA'],
                     'key2': ['one', 'two', 'one'],
                     'left_data': [10,20,30]})

#Dframe on right
df_right = DataFrame({'key1': ['SF', 'SF', 'LA', 'LA'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'right_data': [40,50,60,70]})

#Merge
pd.merge(df_left, df_right, on=['key1', 'key2'], how='outer')

# Now using the above you can check mulitple data sets for multiple key combos, for instance what did the left data set have for LA,one?
# Answer =  60

#Note that the left and right DataFrames have overlapping key names (key1 and key2).
# pandas automatically adds suffixes to them
pd.merge(df_left,df_right,on='key1')

# We can also specify what the suffix becomes
pd.merge(df_left,df_right, on='key1',suffixes=('_lefty','_righty'))

# For more info on merge parameters check out:
url = 'http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.merge.html'

# Next we'll learn how to merge on Index!
