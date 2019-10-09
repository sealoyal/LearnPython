import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# Data Agrregation consists of operations that result in a scalar (e.g. mean(),sum(),count(), etc)

#Let's get a csv data set to play with
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'


# Save thewinquality.csv file in the same folder as your ipython notebooks, note the delimiter used ;
dframe_wine = pd.read_csv('data/winequality-red.csv',sep=';')

# Let's get a preview
dframe_wine.head()

# How about we find out the average alcohol content for the wine
dframe_wine['alcohol'].mean()

# That was an example of an aggregate, how about we make our own?
def max_to_min(arr):
    return arr.max() - arr.min()

# Let's group the wines by "quality"
wino = dframe_wine.groupby('quality')

# Show
wino.describe()

# We can now apply our own aggregate function, this function takes the max value of the col and subtracts the min value of the col
wino.agg(max_to_min)

# We can also pass string methods through aggregate
wino.agg('mean')

# Let's go back to the original dframe
dframe_wine.head()

# Let's adda  quality to alcohol content ratio
dframe_wine['qual/alc ratio'] = dframe_wine['quality']/dframe_wine['alcohol']

# Show
dframe_wine.head()

# We can also use pivot tables instead of groupby
# Pivot table of quality
dframe_wine.pivot_table(index=['quality'])

%matplotlib inline
dframe_wine.plot(kind='scatter',x='quality',y='alcohol')

#We can see that the data is probably better fit for a box plot for a more concise view of the data See if you can figure how to get a boxplot using the pandas documentation and what you have learned so far
#Don't worry if you can't quite figure it out just yet, the next section will cover all sorts of data visualizations!