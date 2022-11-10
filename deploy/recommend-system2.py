import os
import pickle

import numpy as np
import streamlit as st

path = r"C:\Users\julio\OneDrive\Documentos\deploy_ml_project\deploy"
os.chdir(path)

st.set_page_config(page_title="Film Recommendation",
                   page_icon="📽️", layout="wide")

popular_df = pickle.load(open('dataset.pkl', 'rb'))
pt = pickle.load(open('pivot_table.pkl', 'rb'))
films = pickle.load(open('filmes.pkl', 'rb'))
similarity_scores = pickle.load(open('similaridade.pkl', 'rb'))
film_titles = list(pt.index.values)

film_name = list(popular_df['titulo'].values),
generos = list(popular_df['generos'].values),
votes = list(popular_df['total_votos'].values),
rating = list((round(popular_df['nota_media'], 2).values))


def recommend(user_input):
    # user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = films[films['titulo'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('titulo')['titulo'].values))
        item.extend(list(temp_df.drop_duplicates('titulo')['generos'].values))

        data.append(item)

    return data


st.title('Film Recommendation System')
user_input = st.selectbox(
    'Please type or select a film from the dropdown to get recommendations',
    film_titles)
if st.button('Show Recommendation'):
    st.header('Recommendations for the film:  {}'.format(user_input))
    data = recommend(user_input)
    cols = st.columns(4)
    for c in range(len(cols)):
        with cols[c]:
            st.write(data[c][0])
            st.write(data[c][1])

st.markdown('___')
st.markdown('___')
st.title('Top rated films')
d = 0
for i in range(12):
    cols = st.columns(4)
    for c in range(4):
        with cols[c]:
            st.write(film_name[0][d])
            st.write(generos[0][d])
            st.write('avg rating', rating[d])
            st.write('total votes', votes[0][d])
        d = d+1
# d = d+4


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
st.markdown(hide_st_style, unsafe_allow_html=True)
