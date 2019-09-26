import numpy as np
from pandas import Series, DataFrame
import pandas as pd

#Now we'll learn DataFrames

#Let's get some data to play with. How about the NFL?
import webbrowser as wb
url = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
wb.open(url)

#Copy and read to get data
nfl_frame = pd.read_clipboard()

url='https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

df=pd.read_html(url, header=0)[0]

df.head()


#Show
nfl_frame

# We can grab the oclumn names with .columns
nfl_frame.columns

#Lets see some specific data columns
DataFrame(nfl_frame,columns=['Team','First Season','Total Games'])

#What happens if we ask for a column that doesn't exist?
DataFrame(nfl_frame,columns=['Team','First Season','Total Games','Stadium'])

# Call columns
nfl_frame.columns

#We can retrieve individual columns
nfl_frame.Team

# Or try this method for multiple word columns
nfl_frame['Total Games']

#We can retrieve rows through indexing
nfl_frame.ix[3]

#We can also assign value sto entire columns
nfl_frame['Stadium']="Levi's Stadium" #Careful with the ' here

#Show
nfl_frame

#Putting numbers for stadiums
nfl_frame["Stadium"] = np.arange(5)

#Show
nfl_frame

# Call columns
nfl_frame.columns

#Adding a Series to a DataFrame
stadiums = Series(["Levi's Stadium","AT&T Stadium"],index=[4,0])

#Now input into the nfl DataFrame
nfl_frame['Stadium']=stadiums

#Show
nfl_frame

#We can also delete columns
del nfl_frame['Stadium']

nfl_frame

#DataFrames can be constructed many ways. Another way is from a dictionary of equal length lists
data = {'City':['SF','LA','NYC'],
        'Population':[837000,3880000,8400000]}

city_frame = DataFrame(data)

#Show
city_frame

#For full list of ways to create DataFrames from various sources go to teh documentation for pandas:
url = 'http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html'
webbrowser.open(url)