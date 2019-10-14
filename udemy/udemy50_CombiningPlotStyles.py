# The normal imports
import numpy as np
from numpy.random import randn
import pandas as pd

# Import the stats library from numpy
from scipy import stats

# These are the plotting modules adn libraries we'll use:
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Command so that plots appear in the iPython Notebook
plt.tight_layout()

# Command so that plots appear in the iPython Notebook: Only for Jupter Notebook
# %matplotlib inline

# Now we'l learn how to combine plot styles

# Create datset
dataset = randn(100)

# Use distplot for combining plots, by default a kde over a histogram is shown
sns.distplot(dataset,bins=25)

# hist, rug, and kde are all input arguments to turn those plots on or off
sns.distplot(dataset,rug=True,hist=False)

# TO control specific plots in distplot, use [plot]_kws argument with dictionaries.

#Here's an example
sns.distplot(dataset,bins=25,
             kde_kws={'color':'indianred','label':'KDE PLOT'},
             hist_kws={'color':'blue','label':"HISTOGRAM"})

# We can also use pandas data objects for this
from pandas import Series

# Create Series form dataset
ser1 = Series(dataset,name='My_DATA')

# Plot Series
sns.distplot(ser1,bins=25)

# Next up: We'll learn about box and violin plots!