import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#Lets get a dataframe with duplicates
dframe = DataFrame({'key1': ['A'] * 2 + ['B'] * 3,'key2': [2, 2, 2, 3, 3]})

#Show
dframe

#We can use duplicated to find duplicates
dframe.duplicated()

# We can also drop duplicates like this:
dframe.drop_duplicates()

#You can filter which duplicates to drop by a single column
dframe.drop_duplicates(['key1'])

#Show original
dframe

#By default the first value was taken for the duplicates, we can also take the last value instead
dframe.drop_duplicates(['key1'],keep='last')

# That's about it for finding duplicates, pretty easy huh?
#Up next: Mapping