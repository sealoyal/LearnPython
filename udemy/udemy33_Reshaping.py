import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#Let's see how stack and unstack work

# Create DataFrame
dframe1 = DataFrame(np.arange(8).reshape((2, 4)),index=pd.Index(['LA', 'SF'], name='city'),columns=pd.Index(['A', 'B', 'C','D'],name='letter'))
#Show
dframe1

# Use stack to pivot the columns into the rows
dframe_st = dframe1.stack()

#Show
dframe_st

#We can always rearrange back into a DataFrame
dframe_st.unstack()

#We can choose which level to unstack by
dframe_st.unstack(0)

# Also by which name to unstack by
dframe_st.unstack('letter')

# Also by which name to unstack by
dframe_st.unstack('city')

# Let's see how stack and unstack handle NAN
#Make two series
ser1 = Series([0, 1, 2], index=['Q', 'X', 'Y'])
ser2 = Series([4, 5, 6], index=['X', 'Y', 'Z'])

#Concat to make a dframe
dframe = pd.concat([ser1, ser2], keys=['Alpha', 'Beta'])

# Unstack resulting DataFrame
dframe.unstack()

# Now stack will filter out NAN by default
dframe.unstack().stack()

# If we dont want this we can set it to False
dframe.unstack().stack(dropna=False)

# Next we'll learn more abot Pivoting DataFrames!