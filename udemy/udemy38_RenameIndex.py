import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Making a DataFrame
dframe= DataFrame(np.arange(12).reshape((3, 4)), index=['NY', 'LA', 'SF'], columns=['A', 'B', 'C', 'D'])

#Show
dframe

# Just like a Series, axis indexes can also use map
#Let's use map to lowercase the city initials
dframe.index.map(str.lower)

# If you want to assign this to the actual index, you can use index
dframe.index = dframe.index.map(str.lower)

#Show
dframe

# Use rename if you want to create a transformed version without modifying the original!
# str.title will capitalize the first letter, lower-casing the columns
dframe.rename(index=str.title, columns=str.lower)

# We can also use rename to insert dictionaries providing new values for indexes or columns!
dframe.rename(index={'ny': 'NEW YORK'}, columns={'A': 'ALPHA'})

# If you would like to actually edit the data set in place, set inplace=True
dframe.rename(index={'ny': 'NEW YORK'}, inplace=True)
dframe

#Up next: Binning!

