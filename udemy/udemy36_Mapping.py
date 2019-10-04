import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Let's create a dframe to work with (Highest elevation cities in USA)
dframe = DataFrame({'city':['Alma','Brian Head','Fox Park'],
                    'altitude':[3158,3000,2762]})

#Show
dframe

#Now let's say we wanted to add a column for the States, we can do that with a mapping.
state_map = {'Alma':'Colorado','Brian Head':'Utah','Fox Park':'Wyoming'}

# Now we can map that data to our current dframe
dframe['state'] = dframe['city'].map(state_map)

#Show result
dframe

# Mapping is a great way to do element-wise transformations and other data cleaning operations!
# Next up : Replacing Values!
