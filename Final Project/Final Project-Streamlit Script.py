import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=0d1e050a74d7a315039429611592c158&language=en-US')
    data = response.json()
    poster_path = data['poster_path']
    try:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except:
        pass
    
def get_recommendations(title):
    
    indices = pd.Series(movies_rec.index, index=movies_rec['title'])
    idx = indices[title]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
        
    recommended_movies = []
    recommended_movies_posters = []
    
    for i in sim_scores:
        movie_id = movies_rec['id'].iloc[i[0]]
        recommended_movies.append(movies_rec['title'].iloc[i[0]])
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_rec = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.image("./logo_mvdb.png")

st.title('Movie Recommender System')

st.sidebar.image("./ironhack_logo.png", use_column_width=True)

selected_movie_name = st.selectbox(
    'Which movie do you like?',
    movies_rec['title'].values)

if st.button('Recommend'):
    recommended_movies, recommended_movies_posters = get_recommendations(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    try:
        with col1:
            st.text(recommended_movies[0])
            st.image(recommended_movies_posters[0])                                
        with col2:
            st.text(recommended_movies[1])
            st.image(recommended_movies_posters[1]) 
        with col3:
            st.text(recommended_movies[2])
            st.image(recommended_movies_posters[2])                                       
        with col4:
            st.text(recommended_movies[3])
            st.image(recommended_movies_posters[3])           
        with col5:
            st.text(recommended_movies[4])
            st.image(recommended_movies_posters[4])  
    except:
        pass
        
        
    col6, col7, col8, col9, col10 = st.columns(5) 
    try:
        with col6:
            st.text(recommended_movies[5])
            st.image(recommended_movies_posters[5]) 
        with col7:
            st.text(recommended_movies[6])
            st.image(recommended_movies_posters[6])                                       
        with col8:
            st.text(recommended_movies[7])
            st.image(recommended_movies_posters[7])    
        with col9:
            st.text(recommended_movies[8])
            st.image(recommended_movies_posters[8])                                       
        with col10:
            st.text(recommended_movies[9])
            st.image(recommended_movies_posters[9])       
    except:
        pass
                                          