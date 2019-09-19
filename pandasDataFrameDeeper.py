import pandas as pd
import numpy as np

# pass in column names for each CSV
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols, encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, encoding='latin-1')

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(5), encoding='latin-1')

#Inspection
movies.info()

##Show memory usage
movies.memory_usage

#Show data types
movies.dtypes

#Describe
users.describe()

#The head method displays the first five records
movies.head()

#The tail method shows the last 5 records. In this case displays 3 as specified
movies.tail(3)

#Slicing
movies[20:22]

#Selecting
users['occupation']
users['occupation'].head()

#Selecting multiple columns
print(users[['age', 'zip_code']].head())
print('\n')

# can also store in a variable to use later
columns_you_want = ['occupation', 'sex'] 
print(users[columns_you_want].head())

#Selecting using booleans
# users older than 25
print(users[users.age > 25].head(3))
print('\n')

# users aged 40 AND male
print(users[(users.age == 40) & (users.sex == 'M')].head(3))
print('\n')

# users younger than 30 OR female
print(users[(users.sex == 'F') | (users.age < 30)].head(3))
users
print(users)

#Setting an index with an existing column just for printing purposes, not changing Dataframe
print(users.set_index('user_id').head())
print('\n')

print(users.head())
print("\n^^^ I didn't actually change the DataFrame. ^^^\n")

#returning a new Dataframe
with_new_index = users.set_index('user_id')
print(with_new_index.head())
print("\n^^^ set_index actually returns a new DataFrame. ^^^\n")

#Modify existing Dataframe using inplace parameter (not very efficient)
users.set_index('user_id', inplace=True)
users.head()

#Select rows by POSITION using the iloc method
print(users.iloc[99])
print('\n')
print(users.iloc[[1, 50, 300]])

#select rows by LABEL
print(users.loc[100])
print('\n')
print(users.loc[[2, 51, 301]])

#Reset indexes with the old pandas things
users.reset_index(inplace=True)
users.head()

#Joining
left_frame = pd.DataFrame({'key': range(5), 'left_value': ['a', 'b', 'c', 'd', 'e']})
right_frame = pd.DataFrame({'key': range(2, 7), 'right_value': ['f', 'g', 'h', 'i', 'j']})
print(left_frame)
print('\n')
print(right_frame)

#Inner join (default)
pd.merge(left_frame, right_frame, on='key', how='inner')
"""
SELECT left_frame.key, left_frame.left_value, right_frame.right_value
FROM left_frame
INNER JOIN right_frame ON left_frame.key = right_frame.key;
"""

pd.merge(left_frame, right_frame, left_on='left_key', right_on='right_key')

#If keys were indexes
pd.merge(left_frame, right_frame, left_on='key', right_index=True)

#Left outer join
pd.merge(left_frame, right_frame, on='key', how='left')
"""
SELECT left_frame.key, left_frame.left_value, right_frame.right_value
FROM left_frame
LEFT JOIN right_frame ON left_frame.key = right_frame.key;
"""

#Right outer join
pd.merge(left_frame, right_frame, on='key', how='right')
"""
SELECT right_frame.key, left_frame.left_value, right_frame.right_value
FROM left_frame
RIGHT JOIN right_frame ON left_frame.key = right_frame.key;
"""

#Full outer join
pd.merge(left_frame, right_frame, on='key', how='outer')
"""
SELECT IFNULL(left_frame.key, right_frame.key) key, left_frame.left_value, right_frame.right_value
FROM left_frame FULL OUTER JOIN right_frame ON left_frame.key = right_frame.key;
"""

#Combining
pd.concat([left_frame, right_frame])

#Concatenating side-by-side using axis parameter
pd.concat([left_frame, right_frame], axis=1)

#Grouping
salariesFile = 'data/city-of-chicago-salaries.csv'
headers = ['name', 'title', 'department', 'salary']

chicago = pd.read_csv(salariesFile, 
                      header=0,
                      names=headers,
                      converters={'salary': lambda x: float(x.replace('$', ''))})
chicago.head()

by_dept = chicago.groupby('department')
by_dept

#Total number of records in each group
print(by_dept.count().head()) # NOT NULL records within each column
print('\n')
print(by_dept.size().tail()) # total records for each department

#Summation
print(by_dept.sum()[20:25]) # total salaries of each department
print('\n')
print(by_dept.mean()[20:25]) # average salary of each department
print('\n')
print(by_dept.median()[20:25]) # take that, RDBMS!

#Get the five departments with the most distinct titles
by_dept.title.nunique().sort_values(ascending=False)[:5]
"""
SELECT department, COUNT(DISTINCT title)
FROM chicago
GROUP BY department
ORDER BY 2 DESC
LIMIT 5;
"""

#split-apply-combine
#Get highest paid employee within each department.
"""
SELECT *
FROM chicago c
INNER JOIN (
    SELECT department, max(salary) max_salary
    FROM chicago
    GROUP BY department
) m
ON c.department = m.department
AND c.salary = m.max_salary;
"""

#Assigns a rank to each employee based on salary, with 1 being the highest paid
#Assumes the data is DESC sorted
def ranker(df):
    df['dept_rank'] = np.arange(len(df)) + 1
    return df

chicago.sort_values('salary', ascending=False, inplace=True)
chicago = chicago.groupby('department').apply(ranker)
print(chicago[chicago.dept_rank == 1].head(7))

#See where each employee ranks within their department based on salary.
chicago[chicago.department == "LAW"][:6]

