import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Tampilkan judul
st.title('Proyek Analisa Data : E-Commerce')


# Load data csv hasil explorasi RQ1, RQ2, RQ3
rq1_df = pd.read_csv("data/rq1.csv")
rq2_df = pd.read_csv("data/rq2.csv")
rq3_df = pd.read_csv("data/rq3.csv")

with st.sidebar:
    # Menambahkan logo perusahaan
    st.caption('Nama: Eddy Muntina Dharma')
    st.caption('Email: aguseddy@gmail.com')
    st.caption('ID Dicoding: aguseddy')
    

# Visualisasi RQ1
st.subheader("10 Besar Kategori Produk yang paling banyak terjual")

st.bar_chart(
    rq1_df,
    y='counts',
    x='product_category_name_english',
    x_label = 'Jumlah terjual',
    y_label = 'Kategori',
    horizontal=True
)


st.caption('Copyright (c) 2024')
