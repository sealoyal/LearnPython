import pandas as pd
import numpy as np
pd.set_option('max_columns', 50)

# create a Series with an arbitrary list
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
s

#Specifying using indexes
t = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
              index=['A', 'Z', 'C', 'Y', 'E'])
t

#Dictionaries
d = {'Chicago': 1000,
     'New York': 1300,
     'Portland': 900,
     'San Francisco': 1100,
     'Austin': 450,
     'Boston': None}

cities = pd.Series(d)
cities
cities['Chicago']
cities[['Chicago', 'Portland', 'San Francisco']]
cities[cities < 1000]
cities[cities > 1000]

lessThanThousand = cities < 1000
print(lessThanThousand)
print('\n')
print(cities[lessThanThousand])

# changing based on the index
print('Old value:', cities['Chicago'])
cities['Chicago'] = 1400
print('New value:', cities['Chicago'])

# changing values using boolean logic
print(cities[cities < 1000])
print('\n')
cities[cities < 1000] = 750
print(cities[cities < 1000])

#Using idiomatic Python
print('Seattle' in cities)
print('San Francisco' in cities)

# divide city values by 3
cities / 3

# square city values
np.square(cities)

#Adding 2 series, returning an unionof the two series with addition on shared index values
print(cities[['Chicago', 'New York', 'Portland']])
print('\n')
print(cities[['Austin', 'New York']])
print('\n')
print(cities[['Chicago', 'New York', 'Portland']] + cities[['Austin', 'New York']])

# returns a boolean series indicating which values aren't NULL
cities.notnull()

#use boolean logic to grab the NULL cities
print(cities.isnull())
print('\n')
print(cities[cities.isnull()])