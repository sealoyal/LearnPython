# Let's begin by importing what we'll need (You'll probably be copying and pasting this a lot)

# The normal imports
import numpy as np
from numpy.random import randn
import pandas as pd

# Import the stats librayr from numpy
from scipy import stats

# These are the plotting modules adn libraries we'll use:
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Command so that plots appear in the iPython Notebook
plt.tight_layout()

# Command so that plots appear in the iPython Notebook: Only for Jupter Notebook
# %matplotlib inline

# First of all, source of information for what a histogram actually is: http://en.wikipedia.org/wiki/Histogram

#Create a random normal-dist dataset
dataset1 = randn(100)

#Plot a histogram of the dataset, note bins=10 by default
plt.hist(dataset1)

# Lets make another dataset
dataset2 = randn(80)

#Plot
plt.hist(dataset2,color='indianred')

# We can use normed to plot on same plot

# Set normed=True for the plots to be normalized in order to comapre data sets with different number of observations
# Set alpha=0.5 for transparency
plt.hist(dataset1,density=True,color='indianred',alpha=0.5,bins=20)
plt.hist(dataset2,density=True,alpha=0.5,bins=20)

# Make two more random normal dist data sets
data1 = randn(1000)
data2 = randn(1000)

#Can represent joint distributions using joint plots
sns.jointplot(data1,data2)

# Can also use hex bins for a more concise picture
sns.jointplot(data1,data2,kind='hex')

# Next we'll learn how to use Kernel Estimation Plots