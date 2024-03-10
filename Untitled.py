import numpy as np
import pandas as pd
import streamlit as st 

st.title('Filter')

df=pd.read_csv('output.csv')
m=df['Price($)'].max()
n=df['Price($)'].mean()
n1=df['Price($)'].min()
values_price = st.slider('Select a range of Prices (in $)', 0.0, m, (n1, n))
st.write('Price Values:', values_price)

values_ratings = st.slider('Select a range of Ratings', 1, 5, (1, 5))
st.write('Rating Values:', values_ratings)


df_filtered = df[df['Price($)'] >= values_price[0]]


df_filtered = df_filtered[df_filtered['Price($)'] <= values_price[1]]


df_filtered = df_filtered[df_filtered['Ratings'] >= values_ratings[0]]


df_filtered = df_filtered[df_filtered['Ratings'] <= values_ratings[1]]
st.dataframe(df_filtered)

