import streamlit as st
import pickle
import pandas as pd
import numpy as np


movies_list=pickle.load(open("movies_dict.pkl","rb"))
movies=pd.DataFrame(movies_list)
similarity=pickle.load(open("similarity.pkl","rb"))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies=[]
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select the movie : ",
    (movies["title"].values)
)


if st.button("Recommend"):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
  