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

# Now we'll learn how ot visualize multiple regression with lmplot()

# Luckily, Seaborn comes with an example dataset to use as a pandas DataFrame
tips = sns.load_dataset("tips")

# Preview
tips.head()

# Let's use lmplot() to plot the total bill versus tips
sns.lmplot("total_bill","tip",tips)

# First we can see a scatter plot of all the points, tip vs total_bill
# Then we see a linear regression line, which is an estimateed linear fit model to the data

# We can also specify the confidence interval to use for the linear fit
sns.lmplot("total_bill","tip",tips,ci=75) # 68% ci

# Just like before, we can use dictionaries to edit individual parts of the plot
sns.lmplot("total_bill", "tip", tips,
           scatter_kws={"marker": "o", "color": "indianred"},
           line_kws={"linewidth": 1, "color": "blue"});
           
# We can also check out higher-order trends
sns.lmplot("total_bill", "tip", tips,order=4,
           scatter_kws={"marker": "o", "color": "indianred"},
           line_kws={"linewidth": 1, "color": "blue"})

# We can also not fit a regression if desired
sns.lmplot("total_bill", "tip", tips,fit_reg=False)

# lmplot() also works on discrete variables, such as the percentage of the tip
# Create a new column for tip percentage
tips["tip_pect"]=100*(tips['tip']/tips['total_bill'])

#plot
sns.lmplot("size", "tip_pect", tips);

# We can also add jitter to this
#Info link
url = "http://en.wikipedia.org/wiki/Jitter"

#plot
sns.lmplot("size", "tip_pect", tips,x_jitter=.1);

# We can also estimate the tendency of each bin (size of party in this case)
sns.lmplot("size", "tip_pect", tips, x_estimator=np.mean);

# Interesting, looks like there is more variance for party sizes of 1 then 2-4
# We can use the hue facet to automatically define subsets along a column

# Plot, note the markers argument
sns.lmplot("total_bill", "tip_pect", tips, hue="sex",markers=["x","o"])

# Does day make a difference?
sns.lmplot("total_bill", "tip_pect", tips, hue="day")

# Finally it should be noted that Seabron supports LOESS model fitting
url = 'http://en.wikipedia.org/wiki/Local_regression'

sns.lmplot("total_bill", "tip_pect", tips, lowess=True, line_kws={"color": 'black'});

# The lmplot() we've been using is actually using a lower-level function, regplot()
sns.regplot("total_bill","tip_pect",tips)

# reg_plot can be added to existing axes without modifying anything in the figure
# Create figure with 2 subplots
fig, (axis1,axis2) = plt.subplots(1,2,sharey =True)

sns.regplot("total_bill","tip_pect",tips,ax=axis1)
sns.violinplot(tips['tip_pect'],tips['size'],color='blue',ax=axis2)