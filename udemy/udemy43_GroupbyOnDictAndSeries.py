import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#let's learn how to use dict or series with groupby

# Let's make a Dframe

animals = DataFrame(np.arange(16).reshape(4, 4),
                   columns=['W', 'X', 'Y', 'Z'],
                   index=['Dog', 'Cat', 'Bird', 'Mouse'])

#Now lets add some NAN values
animals.loc[1:2, ['W', 'Y']] = np.nan 

#Show
animals

# Now let's say I had a dictionary with ebhavior values in it
behavior_map = {'W': 'good', 'X': 'bad', 'Y': 'good','Z': 'bad'}

# Now we can groupby using that mapping
animal_col = animals.groupby(behavior_map, axis=1)

# Show the sum accroding to the groupby with the mapping
animal_col.sum()

# For example [dog][good] = [dog][Y]+[dog][W]

# Now let's try it with a Series
behav_series = Series(behavior_map)

#Show
behav_series

# Now let's groupby the Series

animals.groupby(behav_series, axis=1).count()

# We can also groupby with functions!

#Show our dframe again
animals

# Lets assume we wanted to group by the length of the animal names, we can pass the len function into groupby!

# Show
animals.groupby(len).sum()

#Note the index is now number of letters in the animal name++# We can also mix functions with arrays,dicts, and Series for groupby methods

# Set a list for keys
keys = ['A', 'B', 'A', 'B']

# Now groupby length of name and the keys to show max values
animals.groupby([len, keys]).max()

# We can also use groupby with hierarchaly index levels

#Create a hierarchal column index
hier_col = pd.MultiIndex.from_arrays([['NY','NY','NY','SF','SF'],[1,2,3,1,2]],names=['City','sub_value'])

# Create a dframe with hierarchal index
dframe_hr = DataFrame(np.arange(25).reshape(5,5),columns=hier_col)

#Multiply values by 100 for clarity
dframe_hr = dframe_hr * 100

#Show
dframe_hr

#Up next: Data Aggregation!!