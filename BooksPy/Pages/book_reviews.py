import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("Datasets/customer reviews.csv") 
df_top100_books = pd.read_csv("Datasets/Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique() #Uniqueretorna uma lista de nomes dos livros sem repetir 
book = st.sidebar.selectbox("Books", books)

df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0] #Aqui ele traz só o titulo sem todos os outros dados que o panda traz
book_genre = df_book["genre"].iloc[0] 
book_price = f"${df_book['book price'].iloc[0]}" #Intercala entre " " e ' ' para ele não entender que a string acabou
book_rating= df_book["rating"].iloc[0] 
book_year = df_book["year of publication"].iloc[0] 

st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year", book_year)

st.divider()

for row in df_reviews_f.values: #Toda vez que ele rodar o for ele pega uma linha de dados e retorna numa lista
    message = st.chat_message(f"{row[4]}") #Nota
    message.write(f"**{row[2]}**") #Como ele retorna uma lista, o elemento 2 é o titulo 
    message.write(f"{row[5]}") # e o elemento 5 é a descrição
