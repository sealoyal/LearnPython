import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Lets make  Series
ser1 = Series([1,2,3,4,1,2,3,4])
#Show
ser1

# Using replace we can select --> .replace(value to be replaced, new_value)
ser1.replace(1,np.nan)

#Can also input lists
ser1.replace([1,4],[100,400])

#Can also input dictionary
ser1.replace({4:np.nan})

#That's it for replace, next up Renaming an axis index