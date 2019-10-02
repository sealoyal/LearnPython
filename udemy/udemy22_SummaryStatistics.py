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

#Correlation
YouTubeVideo('4EXNedimDMs')

#Now lets check correlation and covariance on some stock prices!
#Pandas can get info off the web
#Install pandas_datareader first through pip
from pandas_datareader import data as pdweb

#Set datetime for date input
import datetime

#Get the closing prices
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 1)

prices = pdweb.get_data_yahoo(['CVX','XOM','BP'],
                               start,
                               end)['Adj Close']
#Show preview
prices.head()

#Now lets get the volume trades

volume = pdweb.get_data_yahoo(['CVX','XOM','BP'],
                               start,
                               end)['Volume']

#Show preview
volume.head()

#Lets get the return
returns = prices.pct_change()

#Show returns
returns.head()

#Get the correlation of the stocks
corr = returns.corr

#Show returns
corr.head()

#Lets see the prices over time to get a very rough idea of the correlation between the stock prices
prices.plot()


import seaborn as sns
import matplotlib.pyplot as plt

#As expected pretty strong correlations with each other
sns.heatmap(returns.corr())

#We'll learn much more about seaborn later!

# We can also check for unique values and their counts

#For example
ser1 = Series(['w','w','x','y','z','w','w','x','x','y','a','z'])

#Show
ser1

#Grab the unique values
ser1.unique()

#Now get the count of the unique values
ser1.value_counts()

#Next we'll learn how to best deal with missing data!