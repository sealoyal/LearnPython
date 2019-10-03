import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#Lets make some Series to work with

#First Series
ser1 = Series([2,np.nan,4,np.nan,6,np.nan],index=['Q','R','S','T','U','V'])

#Second Series (based off length of ser1)
ser2 = Series(np.arange(len(ser1), dtype=np.float64),index=['Q','R','S','T','U','V'])
ser2[-1] = np.nan

ser1

# Now let's get a series where the value of ser1 is chosen if ser2 is NAN,otherwise let the value be ser1
Series(np.where(pd.isnull(ser1),ser2,ser1),index=ser1.index)
#Take a moment to really understand how the above worked

#Now we can do the same thing simply by using combine_first with pandas
ser1.combine_first(ser2)
#This combines the Series values, choosing the values of the calling Series first, unless its a NAN

#Now lets how this works on a DataFrame!
#Lets make some 
dframe_odds = DataFrame({'X': [1., np.nan, 3., np.nan],'Y': [np.nan, 5., np.nan, 7.],'Z': [np.nan, 9., np.nan, 11.]})
dframe_evens = DataFrame({'X': [2., 4., np.nan, 6., 8.],'Y': [np.nan, 10., 12., 14., 16.]})

#Show
dframe_odds
dframe_evens

#Now lets combine using odds values first, unless theres a NAN, then put the evens values
dframe_odds.combine_first(dframe_evens)

#Next up: Reshaping DataFrames!