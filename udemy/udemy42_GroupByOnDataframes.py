import numpy as np
import pandas as pd
from pandas import DataFrame, Series

#Let's make a dframe
dframe = DataFrame({'k1':['X','X','Y','Y','Z'],
                    'k2':['alpha','beta','alpha','beta','alpha'],
                    'dataset1':np.random.randn(5),
                    'dataset2':np.random.randn(5)})

#Show
dframe

#Now let's see how to use groupby

#Lets grab the dataset1 column and group it by the k1 key
group1 = dframe['dataset1'].groupby(dframe['k1'])

#Show the groupby object
group1

#Now we can perform operations on this particular group
group1.mean()

# We can use group keys that are series as well

#For example:

#We'll make some arrays for use as keys
cities = np.array(['NY','LA','LA','NY','NY'])
month = np.array(['JAN','FEB','JAN','FEB','JAN'])

#Now using the data from dataset1, group the means by city and month
dframe['dataset1'].groupby([cities,month]).mean()

# let's see the original dframe again.
dframe

# WE can also pass column names as group keys
dframe.groupby('k1').mean()

# Or multiple column names
dframe.groupby(['k1','k2']).mean()

# Another useful groupby method is getting the group sizes
dframe.groupby(['k1']).size()

# We can also iterate over groups

#For example:
for name,group in dframe.groupby('k1'):
    print "This is the %s group" %name
    print group
    print '\n'
    
# We can also iterate with multiple keys
for (k1,k2) , group in dframe.groupby(['k1','k2']):
    print "Key1 = %s Key2 = %s" %(k1,k2)
    print group
    print '\n'
    
# A possibly useful tactic is creating a dictionary of the data pieces 
group_dict = dict(list(dframe.groupby('k1')))

#Show the group with X
group_dict['X']

# We could have also chosen to do this with axis = 1

# Let's creat a dictionary for dtypes of objects!
group_dict_axis1 = dict(list(dframe.groupby(dframe.dtypes,axis=1)))

#show
group_dict_axis1

# Next we'll learn how to use groupby with columns

# For example if we only wanted to group the dataset2 column with both sets of keys
dataset2_group = dframe.groupby(['k1','k2'])[['dataset2']]

dataset2_group.mean()

#Next we'll have a quick lesson on grouping with dictionaries and series!






