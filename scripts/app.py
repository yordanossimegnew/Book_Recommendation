import pickle
import streamlit as st
import numpy as np

st.header("Book Recommender System using Machine Learning")
# loading a model
model = pickle.load(open("C:\\Users\\yozil\\Desktop\\My_Projects\\Book_Recommendation\\models\\model.pkl","rb"))

# laoding files
books_name = pickle.load(open("C:\\Users\\yozil\\Desktop\\My_Projects\\Book_Recommendation\\data\\processed_data\\books_name.pkl","rb"))
book_pivot = pickle.load(open("C:\\Users\\yozil\\Desktop\\My_Projects\\Book_Recommendation\\data\\processed_data\\book_pivot.pkl","rb"))
final_rating = pickle.load(open("C:\\Users\\yozil\\Desktop\\My_Projects\\Book_Recommendation\\data\\processed_data\\final_rating.pkl","rb"))

# creat a selection box containing all the book names
selected_books= st.selectbox(
    "Type or Select a book",
    books_name
)

def fetch_poster(suggestion):
    book_name= []
    ids_index = []
    poster_url= []
    
    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])
        
    for name in book_name[0]:
        ids = np.where(final_rating["title"] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]["url"]
        poster_url.append(url)
        
    return poster_url

def recommend_books(book_name):
    book_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)
    
    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    return book_list, poster_url


if st.button("Show Recommendation"):
    recommendation_books, poster_url = recommend_books(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommendation_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommendation_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommendation_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommendation_books[5])
        st.image(poster_url[5])