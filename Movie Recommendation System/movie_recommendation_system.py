# -*- coding: utf-8 -*-
"""Movie Recommendation system

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12LaZKv20SgDu6zLmYwI6bQpaZNhp6IsP

**Importing The Dependencies**
"""

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""**Data Collection and Pre-Processing**"""

# loading the data from the csv file to pandas dataframe

movies_data = pd.read_csv('/content/movies.csv')

"""Printing The first 5 rows"""

movies_data.head()

"""Selecting the relevant features for recommendations"""

selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
print(selected_features)

# replace na values with empty string

for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')

# combining all the 5 selected features

combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
print(combined_features)

# converting the text data to feature vectors

vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(combined_features)
print(feature_vectors)

"""Cosine **Similarity**"""

# getting the cosine score using cos similarity

similarity = cosine_similarity(feature_vectors)
print(similarity)

# getting the movie from the user

movie_name = input('Enter your fav movie name : ')

# creating a list with all the movie names given in dataset

list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)

# finding the closest match

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles, n = 10, cutoff =  0.0002)
print(find_close_match)

from os import supports_effective_ids
# getting a list of several movies 
close_match = find_close_match[0]
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]


#calculating similarity with all other movies
similarity_score = list(enumerate(similarity[index_of_the_movie]))

# sorting based on similarity
sorted_similarity_score = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print(sorted_similarity_score)

#Print Movie names based on index

print('Some Movie Suggestions are : \n')

i = 1
for movie in sorted_similarity_score:
  index = movie[0]
  title_from_index = movies_data[movies_data.index == index]['title'].values[0]
  if i < 30:
    print(i, '.', title_from_index)
    i+=1

#MOVIE RECOMMENDATION SYSTEM

movie_name = input('Enter your fav movie name : ')

list_of_all_titles = movies_data['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

close_match = find_close_match[0]

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similarity_score = sorted(similarity_score, key = lambda x:x[1], reverse = True)


print('Some Movie Suggestions are : \n')

i = 1
for movie in sorted_similarity_score:
  index = movie[0]
  title_from_index = movies_data[movies_data.index == index]['title'].values[0]
  if i < 30:
    print(i, '.', title_from_index)
    i+=1