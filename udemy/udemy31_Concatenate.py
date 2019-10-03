# Now we'll learn about concatenating along an axis
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# First in just Numpy
# Create a matrix
arr1 = np.arange(9).reshape((3,3))

# Show
arr1

# Concatenate along axis 1
np.concatenate([arr1,arr1],axis=1)

# Let's see other axis options
np.concatenate([arr1,arr1],axis=0)

# Now let's see how this works in pandas
# Lets create two Series with no overlap
ser1 = Series([0,1,2],index=['T','U','V'])
ser2 = Series([3,4],index=['X','Y'])

#Now let use concat (default is axis=0)
pd.concat([ser1,ser2])

# Now passing along another axis will produce a DataFrame
pd.concat([ser1,ser2],axis=1,sort=False)

# We can specify which specific axes to be used
pd.concat([ser1,ser2],axis=1,join_axes=[['U','V','Y']]) #Deprecated
pd.concat([ser1,ser2],axis=1,sort=False).reindex(['U','V','Y'])

# Lets say we wanted to add markers.keys to the concatenation result
# We can do this with a hierarchical index
pd.concat([ser1,ser2],keys=['cat1','cat2'])

# Along the axis=1 then these Keys become column headers
pd.concat([ser1,ser2],axis=1,keys=['cat1','cat2'],sort=False)

#Lastly, everything works similarly in DataFrames
dframe1 = DataFrame(np.random.randn(4,3), columns=['X', 'Y', 'Z'])
dframe2 = DataFrame(np.random.randn(3, 3), columns=['Y', 'Q', 'X'])

#Concat on DataFrame
pd.concat([dframe1,dframe2],sort=False)

#If we dont care about the index info and just want to make a complete DataFrame, just use ignore_index
pd.concat([dframe1,dframe2],ignore_index=True,sort=False)

#For more info in documentation:
url = 'http://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html'

#Next up: More on Combining DataFrames with Overlapping Indexes!
