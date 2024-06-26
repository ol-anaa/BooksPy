import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("Datasets/customer reviews.csv")  #df = DataFrame
df_top100_books = pd.read_csv("Datasets/Top-100 Trending Books.csv")


price_max = df_top100_books["book price"].max() #Ele vai na coluna "book price" de df_top100_books 
                                                # e vai pegar o valor máximo que tem naquela coluna.
price_min = df_top100_books["book price"].min() #Aqui ele pega o minimo

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
df_books = df_top100_books[df_top100_books["book price"]  <= max_price]
img = px.bar(df_books["year of publication"].value_counts()) #value_counts() pega a ocorrencia de determinado dado
                                                       # na coluna que eu dei "year of publication".
                                                       #O px.bar cria uma iamgem de um grafico de barras
img2 = px.histogram(df_books["book price"])

df_books
col1, col2 = st.columns(2) #Define duas colunas na tela
col1.plotly_chart(img) # mostra para o streamlit que é um gráfico, ele segue filtrando, colocando nas colunas
col2.plotly_chart(img2)