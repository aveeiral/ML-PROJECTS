# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from tkinter import messagebox, END




import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

result = []

movie_name = ""

def m_recommendation():
    
    movie_name = cityEntry.get()
    movies_data = pd.read_csv('movies.csv')
    
    selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
    
    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna('') 
        
    combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
    
    vectorizer = TfidfVectorizer()

    feature_vectors = vectorizer.fit_transform(combined_features)
    
    similarity = cosine_similarity(feature_vectors)
    
    list_of_all_titles = movies_data['title'].tolist()
    
    find_close_match = list(difflib.get_close_matches(movie_name, list_of_all_titles))
    
    close_match = find_close_match[0]
    
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]


#calculating similarity with all other movies
    similarity_score = list(enumerate(similarity[index_of_the_movie]))

# sorting based on similarity
    sorted_similarity_score = sorted(similarity_score, key = lambda x:x[1], reverse = True)
    
    print('Some Movie Suggestions are : \n')

    i = 1
    for movie in sorted_similarity_score:
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        if i < 30:
            temp = str(i)+' . ' + title_from_index
            result.append(temp)
            #print(i, '.', title_from_index)
            i+=1
            
    #print(result)



root = tk.Tk()

canvas = tk.Canvas(root, width =600, height = 300)
canvas.grid(columnspan=3)

# Creating a logo

"""logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.iamge = logo
logo_label.grid(column=0, row=0)"""



cityLabel = tk.Label(root, text="Enter Movie Name : ", bg="skyblue")
cityLabel.grid(row=0, column=0, padx=10, pady=5)
cityEntry = tk.Entry(root, width=36)
cityEntry.grid(row=0, column=1, padx=10, pady=5)

findButton = tk.Button(root, text="Find Similar Movies", command=m_recommendation)
findButton.grid(row=1, column=0, padx=10, pady=5, columnspan = 2)
    
my_listbox = tk.Listbox(root)
my_listbox.grid(row =1, column = 2, pady=15)

for item in result:
    my_listbox.insert(END, item)

    

root.mainloop()




























