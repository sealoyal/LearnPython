import pandas as pd

# This will be a quick lesson on cross-tabulations, which are basically a special case of pivot-tables

# Let's create a quick data set
from io import StringIO

data ="""\
Sample   Animal   Intelligence
1        Dog     Smart
2 Dog Smart
3 Cat Dumb
4 Cat Dumb
5 Dog Dumb
6 Cat Smart"""

#Store as dframe
dframe = pd.read_csv(StringIO(data),sep='\s+')

# Show
dframe

# Now we can create a cross-tabulation table, which is basically just a frequency table
pd.crosstab(dframe.Animal,dframe.Intelligence,margins=True)

# And thats about it as far as it's general use.
# We'll use it in examples in the final projects!