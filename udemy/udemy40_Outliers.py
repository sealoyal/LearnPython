import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Let's see how we would find outliers in a dataset

# First we'll seed the numpy generator
np.random.seed(12345)

#Next we'll create the dataframe
dframe = DataFrame(np.random.randn(1000,4))

#Show preview
dframe.head()

# Lets describe the data
dframe.describe()

# Lets select the first column
col = dframe[0]

# NOw we can check which values in the column are greater than 3, for instance.
col[np.abs(col) > 3]

# So we now know in column[0], rows 523 and 900 have values with abs > 3

#How about all the columns?

# We can use the "any" method
dframe[(np.abs(dframe) > 3).any(1)]

# WE could also possibly cap the data at 3

dframe[np.abs(dframe) > 3] = np.sign(dframe) * 3

dframe.describe()

# Next we'll learn about Permutation!