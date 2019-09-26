import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}

football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
football

#Processing CSV files
csv1 = "data/mariano-rivera.csv"
fromCSV = pd.read_csv(csv1)
fromCSV.head()


##CSV
#Processing another CSV file with defined headers
csv2 = "data/peyton-passing-TDs-2012.csv"

cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
        'result', 'quarter', 'distance', 'receiver', 'score_before',
        'score_after']

no_headers = pd.read_csv(csv2, sep=',', header=None, names=cols)
no_headers.head()

no_headers.to_csv('path_to_file.csv')

##EXCEL
##Convert files to Excel. Check values first
football.head()

#Convert football variable to Excel file
football.to_excel('football.xlsx', index=False)

# delete the DataFrame
del football

# read from Excel
football = pd.read_excel('football.xlsx', 'Sheet1')
football

##SQL
from pandas.io import sql
import sqlite3
databaseFile = 'towed.db'
conn = sqlite3.connect(databaseFile)
query = "SELECT * FROM towed WHERE make = 'FORD';"
results = sql.read_sql(query, con=conn)
results.head()

#Clipboard
clip = pd.read_clipboard()
clip.head()

#URL
url = 'https://raw.github.com/gjreda/best-sandwiches/master/data/best-sandwiches-geocode.tsv'

# fetch the text from the URL and read it into a DataFrame
from_url = pd.read_table(url, sep='\t')
from_url.head(3)