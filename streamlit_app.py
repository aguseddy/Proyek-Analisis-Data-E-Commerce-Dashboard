import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Tampilkan judul
st.title('Proyek Analisa Data : E-Commerce')


# Load data csv hasil explorasi RQ1, RQ2, RQ3
rq1_df = pd.read_csv("rq1.csv")
rq2_df = pd.read_csv("rq2.csv")
rq3_df = pd.read_csv("rq3.csv")



st.caption('Copyright (c) 2024')
