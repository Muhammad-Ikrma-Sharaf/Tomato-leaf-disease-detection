import streamlit as st
import pickle
import pandas as pd
import requests


def fetch(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=c66a49533de9762768abb0a54bf1aebe".format(movie_id))
    data=response.json()

    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]




def recommend(movie):
    recommended_movies =[]
    recommended_movies_posters =[]
    movie_index=movies_list1[movies_list1["title"]== movie].index[0]
    distances = similarity[movie_index]
    movie_list2=sorted(list(enumerate(distances)) ,reverse =True , key = lambda x:x[1])[1:6]
    for i in movie_list2 :
        movie_id =movies_list1.iloc[i[0]].movie_id
        recommended_movies.append(movies_list1.iloc[i[0]].title)
        recommended_movies_posters.append(fetch(movie_id))
    return recommended_movies,recommended_movies_posters

movies_list = pickle.load(open("movies1.pkl", "rb"))
movies_list1 = pd.DataFrame(movies_list)
similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Muhammad Ikrma Sharaf")
#st.markdown('**ML intern @Kyaas Solutions**')


option = st.selectbox("Select a movie!",movies_list1["title"].values)


if st.button("Recommend"):

    st.text("Here are the movies:")
    name,posters = recommend(option)
    col1 , col2 , col3 , col4 , col5 =st.columns(5)

    with col1:
        st.image(posters[0])
        st.text(name[0])

    with col2:
        st.image(posters[1])
        st.text(name[1])

    with col3:
        st.image(posters[2])
        st.text(name[2])

    with col4:
        st.image(posters[3])
        st.text(name[3])

    with col5:
        st.image(posters[4])
        st.text(name[4])
