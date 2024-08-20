import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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

# Visualisasi RQ2
st.subheader("Perkembangan omset penjualan per Bulan")

st.line_chart(
    rq2_df,
    x='thn_bln',
    y='jual',
    x_label = 'Periode',
    y_label = 'Omset',
)


# Visualisasi RQ3
st.subheader("Segmentasi Customer")

fig, ax = plt.subplots(figsize=(20, 10))

sns.barplot(
    x="jml_customer", 
    y="customer_segment",
    data=rq3_df.sort_values(by="customer_segment", ascending=False),
    hue="customer_segment"
)

ax.set_title("Segmentasi Customer", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.xaxis.grid(True)
ax.yaxis.grid(True)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.caption('Copyright (c) 2024')
