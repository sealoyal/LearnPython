#Now we'll elarn about reindexing

import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn

#Lets create a new series
ser1 = Series([1,2,3,4],index=['A','B','C','D'])

#Show
ser1

#Call reindex to rearrange the data to a new index
ser2 = ser1.reindex(['A','B','C','D','E','F'])

#Show
ser2

# We can alos fill in values for new indexes
ser2.reindex(['A','B','C','D','E','F','G'],fill_value=0)

#Using a particular method for filling values
ser3 = Series(['USA','Mexico','Canada'],index=[0,5,10])

#Show
ser3

#Can use a forward fill for interploating values vetween indices 
ser3.reindex(range(15),method='ffill')

#Reindexing rows, columns or both
#Lets make a dataframe with some random values
dframe = DataFrame(randn(25).reshape((5,5)),index=['A','B','D','E','F'],columns=['col1','col2','col3','col4','col5'])

#Show
dframe

#Notice we forgot 'C' , lets reindex it into dframe
dframe2 = dframe.reindex(['A','B','C','D','E','F'])

#Can also explicitly reindex columns
new_columns = ['col1','col2','col3','col4','col5','col6']

dframe2.reindex(columns=new_columns)

#Reindex quickly using the label-indexing with ix (we'll see this more in the future)
#Show original
dframe

dframe.loc[['A','B','C','D','E','F'],new_columns]
