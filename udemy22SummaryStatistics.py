#Now we'll learn about pandas built-in methods of summarizing data founr in DataFrames
import numpy as np
from pandas import Series,DataFrame
import pandas as pd

#Let's create a dataframe to work with
arr = np.array([[1,2,np.nan],[np.nan,3,4]])
dframe1 = DataFrame(arr,index=['A','B'],columns = ['One','Two','Three'])

#Show
dframe1

#Let's see the sum() method in action
dframe1.sum()

#Notice how it ignores NaN values
#We can also over rows instead of columns
dframe1.sum(axis=1)

#Can also grab min and max values of dataframe
dframe1.min()
dframe1.max()

#As well as there index
dframe1.idxmin()
dframe1.idxmax()

#Show
dframe1

#Can also do an accumulation sum
dframe1.cumsum()

#A very useful feature is describe, which provides summary statistics
dframe1.describe()

# We can also get information on correlation and covariance

#For more info on correlation and covariance, check out the videos below!

from IPython.display import YouTubeVideo
# For more information about Covariaance and Correlation
# Check out these great videos!
# Video credit: Brandon Foltz.

#CoVariance
YouTubeVideo('xGbpuFNR1ME')