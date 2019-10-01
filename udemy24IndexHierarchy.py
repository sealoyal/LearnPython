import numpy as np
from pandas import Series,DataFrame
import pandas as pd
from numpy.random import randn

#Now we'll learn about Index Hierarchy
#pandas allows you to have multiple index levels, which is very clear with this example:
ser = Series(np.random.randn(6),index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])

#Show Series with multiple index levels
ser

# We can check the multiple levels
ser.index

#Now we can select specific subsets
ser[1]

# We can also select from an internal index level
ser[:,'a']

# We can also create Data Frames from Series with multiple levels
dframe = ser.unstack()

#Show
dframe

#Can also reverse
dframe.unstack()

# We can also apply multiple level indexing to DataFrames
dframe2 = DataFrame(np.arange(16).reshape(4, 4),
                    index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                    columns=[['NY', 'NY', 'LA', 'SF'], ['cold', 'hot', 'hot', 'cold']])

dframe2

# We can also give these index levels names
#Name the index levels
dframe2.index.names = ['INDEX_1','INDEX_2']

#Name the column levels
dframe2.columns.names = ['Cities','Temp']

dframe2

# We can also interchange level orders (note the axis=1 for columns)
dframe2.swaplevel('Cities','Temp',axis=1)

#We can also sort levels
dframe2.sort_index(level='INDEX_2')

#Note the change in sorting, now the Dframe index is sorted by the INDEX_2

#We can also perform operations on particular levels
dframe2.sum(level='Temp',axis=1)

#Thats the end of this section! Next up, Section 5: Working with Data Part 1 !!!