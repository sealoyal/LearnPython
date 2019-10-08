import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#Now we'll learn about binning

years = [1990,1991,1992,2008,2012,2015,1987,1969,2013,2008,1999]

# We can seperate these years by decade
decade_bins = [1960,1970,1980,1990,2000,2010,2020]

#Now we'll use cut to get something called a Category object
decade_cat = pd.cut(years,decade_bins)

#Show
decade_cat

# We can check the categories using .categories
decade_cat.categories

# Then we can check the value counts in each category
pd.value_counts(decade_cat)

# We can also pass data values to the cut.

#For instance, if we just wanted to make two bins, evenly spaced based on max and min year, with a 1 year precision
pd.cut(years,2,precision=1)

# Thats about it for binning basics
# One last thing to note, just like in standard math notation, when setting up bins:
# () means open, while [] means closed/inclusive

# Next up: Finding Outliers and Describing Data!