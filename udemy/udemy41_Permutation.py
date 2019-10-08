import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#We can randomly reorder (permutate) a Series, or the rows in a DataFrame

#Let's take a look
dframe = DataFrame(np.arange(4 * 4).reshape((4, 4)))

#Create an array with a random perumation of 0,1,2,3
blender = np.random.permutation(4)

# Show
blender
dframe

# Now permutate the dframe based on the blender
dframe.take(blender)

# Now what if we want permuations WITH replacement

# Let imagine a box with 3 marbles in it: labeled 1, 2, and 3
box = np.array([1,2,3])

# Now lets create a random permuation WITH replacement using randint
shaker = np.random.randint(0, len(box), size=10)

# Let's check teh box "shaker"
shaker

#Now lets grab form the box
hand_grabs = box.take(shaker)

#show
hand_grabs
