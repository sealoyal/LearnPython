import pandas as pd
from pandas import Series, DataFrame
import numpy as np
#Now we'll learn how to merge on an index

# Lets get two dframes
df_left = DataFrame({'key': ['X','Y','Z','X','Y'],'data': range(5)})
df_right = DataFrame({'group_data': [10, 20]}, index=['X', 'Y'])

#Show
df_left

#Show
df_right

#Now merge, we'll use the key for the left Dframe, and the index for the right
pd.merge(df_left,df_right,left_on='key',right_index=True)

# We can also get a union by using outer
pd.merge(df_left,df_right,left_on='key',right_index=True,how='outer')

#Now let's try something a little more complicated, remember hierarchal index?
df_left_hr = DataFrame({'key1': ['SF','SF','SF','LA','LA'],'key2': [10, 20, 30, 20, 30],'data_set': np.arange(5.)})
df_right_hr = DataFrame(np.arange(10).reshape((5, 2)),index=[['LA','LA','SF','SF','SF'],[20, 10, 10, 10, 20]],columns=['col_1', 'col_2'])

#SHOW
df_left_hr

#Show, this has a index hierarchy
df_right_hr

# Now we can merge the left by using keys and the right by its index
pd.merge(df_left_hr,df_right_hr,left_on=['key1','key2'],right_index=True)

# We can alo keep a union by choosing 'outer' method
pd.merge(df_left_hr,df_right_hr,left_on=['key1','key2'],right_index=True,how='outer')

# WE can also you .join()

# Shown on our first two DataFrames
df_left.join(df_right)

# Next we'll learn about the concatenate function!