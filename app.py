import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:8]

    recommended_movies = []
    for i in movie_list :
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

similarity=pickle.load(open('similarity.pkl','rb'))
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title("movie recommender system")
selected_movie =st.selectbox('choose the movie for reccomendation realted to that ',movies['title'].values)

if st.button('Recommend movie'):
    recommendation = recommend(selected_movie)
    for i in recommendation:
        st.write(i)