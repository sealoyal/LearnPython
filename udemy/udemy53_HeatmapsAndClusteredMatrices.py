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

# Again seaborn comes with a great dataset to play and learn with
flight_dframe = sns.load_dataset('flights')

#Preview
flight_dframe.head()

# Let's pivot this dataframe do its easier to manage
flight_dframe = flight_dframe.pivot("month","year","passengers")

#Show
flight_dframe

# This dataset is now in a clear format to be dispalyed as a heatmap
sns.heatmap(flight_dframe)

# We also have the option to annotate each cell
sns.heatmap(flight_dframe,annot=True,fmt='d')

# seaborn will automatically try to pick the best color scheme for your dataset, whether is be diverging or converging colormap
# We can choose our own 'center' for our colormap
sns.heatmap(flight_dframe,center=flight_dframe.loc['January',1955])

# heatmap() can be used on an axes for a subplot to create more informative figures
f, (axis1,axis2) = plt.subplots(2,1)
yearly_flights = flight_dframe.sum()

# Since yearly_flights is a weird format, we'll have to grab the values we want with a Series, then put them in a dframe
years = pd.Series(yearly_flights.index.values)
years = pd.DataFrame(years)

flights = pd.Series(yearly_flights.values) 
flights = pd.DataFrame(flights)

# Make the dframe and name columns
year_dframe = pd.concat((years,flights),axis=1)
year_dframe.columns = ['Year','Flights']

# Create the bar plot on top
sns.barplot('Year',y='Flights',data=year_dframe, ax = axis1)

# Create the heatmap on bottom
sns.heatmap(flight_dframe,cmap='Blues',ax=axis2,cbar_kws={"orientation": "horizontal"})


# Finally we'll learn about using a clustermap
# Clustermap will reformat the heatmap so similar rows are next to each other
sns.clustermap(flight_dframe)

# Let's uncluster the columns
sns.clustermap(flight_dframe,col_cluster=False)

# Since the number of flights increase every year, we should set a standard scale
sns.clustermap(flight_dframe,standard_scale=1) # standardize by columns (year)

# Or scale the rows
sns.clustermap(flight_dframe,standard_scale=0)

# Finally we can also normalize the rows by their Z-score.
# This subtracts the mean and devides by the STD of each column, then the rows have a mean of 0 and a variance of 1
sns.clustermap(flight_dframe,z_score=1)

# Above we can see which values are greater than the mean and which are below very clearly
# CONGRATULATIONS!! We've developed quite a toolbox to hammer out some great data anaysis projects!

# Up next: Projects to apply what we've learned to real datasets!