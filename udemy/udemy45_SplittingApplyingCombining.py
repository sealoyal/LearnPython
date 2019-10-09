import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Let's grab the wine data again
dframe_wine = pd.read_csv('data/winequality_red.csv',sep=';')

#Preview
dframe_wine.head()

# What if we wanted to know the highest alcohol content for each quality range?
# We can use groupby mechanics to split-apply-combine

# Create a function that assigns a rank to each wine based on alcohol content, with 1 being the highest alcohol content
def ranker(df):
    df['alc_content_rank'] = np.arange(len(df)) + 1
    return df

# Now sort the dframe by alcohol in ascending order
dframe_wine.sort('alcohol',ascending = False,inplace = True)

# Now we'll group by quality and apply our ranking function
dframe_wine = dframe_wine.groupby('quality').apply(ranker)

#Preview
dframe_wine.head()

# Now finally we can just call for the dframe where the alc_content_rank == 1

# Get the number of quality counts
num_of_qual = dframe_wine['quality'].value_counts()

#Show
num_of_qual

# Now we'll show the combined info for the wines that had the highest alcohol content for their respective rank!
dframe_wine[dframe_wine.alc_content_rank == 1].head(len(num_of_qual))

# Awesome! Ask yourself if there are any trends you would like to find in this data?
# Is there a relationship between wine ranking and alcohol content?