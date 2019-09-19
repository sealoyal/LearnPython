import pandas as pd
import numpy as np


# pass in column names for each CSV
#User files
userFile = 'ml-100k/u.user'
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv(userFile, sep='|', names=u_cols, encoding='latin-1')
users

file = open(userFile)
print(file.read()) 

#Ratings file
ratingsFile = 'ml-100k/u.data'
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv(ratingsFile, sep='\t', names=r_cols, encoding='latin-1')

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
#Movies file
moviesFile = 'ml-100k/u.item'
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv(moviesFile, sep='|', names=m_cols, usecols=range(5), encoding='latin-1')

# create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
lens = pd.merge(movie_ratings, users)

# What are the 25 most rated movies?
most_rated = lens.groupby('title').size().sort_values(ascending=False)[:25]
most_rated
"""
SELECT title, count(1)
FROM lens
GROUP BY title
ORDER BY 2 DESC
LIMIT 25;
"""

# Alternative method
lens.title.value_counts()[:25]

# Which movies are most highly rated?
# agg method aggregates
movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})
movie_stats.head()

# sort by rating average
movie_stats.sort_values([('rating', 'mean')], ascending=False).head()

# Movies that have been rated at least 100 times.
atleast_100 = movie_stats['rating']['size'] >= 100
movie_stats[atleast_100].sort_values([('rating', 'mean')], ascending=False)[:15]