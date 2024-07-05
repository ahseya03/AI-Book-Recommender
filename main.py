# main.py
import streamlit as st
import langchain_helper

st.title("Book Recommender")

# Sidebar for selecting genre
genre = st.sidebar.selectbox("Pick a Genre", ("Science Fiction", "Fantasy", "Mystery", "Non-fiction", "Historical Fiction"))

if genre:
    response = langchain_helper.recommend_books(genre)
    
    # Extract and display book titles
    book_titles = response['book_titles'].strip().split(",")
    st.header("Recommended Books")
    for title in book_titles:
        st.subheader(title.strip())
    
    # Extract and display book descriptions
    book_descriptions = response['book_descriptions'].strip().split("\n")
    st.write("**Book Descriptions**")
    for description in book_descriptions:
        st.write("-", description.strip())
