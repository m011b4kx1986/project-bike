# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:10:38 2024

@author: hp
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  
import seaborn as sns

# Setting seaborn style
sns.set(style='white')

# Title for the Streamlit app
st.title('Data Penggunaan Sepeda Tahun 2011')

# Create function to aggregate monthly user data
def create_monthly_users_df(df):
    monthly_user_df = df.groupby(by="mnth").agg(
        user_count=('cnt', 'sum')
    ).reset_index()
    return monthly_user_df

# Create function to aggregate casual and registered users data
def create_category_users_df(df):
    category_user_df = df.groupby(by="mnth")[
        ['casual', 'registered']
    ].sum().reset_index()
    return category_user_df

# Load data
data = pd.read_csv('C:/Users/hp/Downloads/Project-Bike/dashboard/all-data.csv')

# Convert date column to datetime format
data['dteday'] = pd.to_datetime(data['dteday'])

# Get min and max dates for the sidebar date input
min_date = data["dteday"].min()
max_date = data["dteday"].max()

# Sidebar for date selection
with st.sidebar:
    start_date, end_date = st.date_input(
        label='Range Time', 
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data based on selected date range
main_df = data[(data["dteday"] >= pd.to_datetime(start_date)) &
               (data["dteday"] <= pd.to_datetime(end_date))]

# Prepare dataframes for visualizations
monthly_df = create_monthly_users_df(main_df)
category_df = create_category_users_df(main_df)

# Create header for visualization
st.header('Visualisasi Data')

# Create tabs for different visualizations
tab1, tab2 = st.tabs(["Total Pengguna", "Kategori"])

# Tab to display the total users
with tab1:
    with st.container():
        st.write("Jumlah Pengguna Sepeda Tahun 2011")
        
        plt.figure(figsize=(10, 5))
        monthly_counts = main_df.groupby('mnth')['cnt'].sum()  
        plt.bar(monthly_counts.index, monthly_counts.values, color='skyblue')  
        plt.xlabel("Bulan")
        plt.ylabel("Jumlah Pengguna")
        st.pyplot(plt)
        plt.clf()

# Tab to display casual and registered users
with tab2:
    with st.container():
        st.write("Pengguna Sepeda Kasual dan Terdaftar (Berdasarkan Bulan yang Tersedia)")
        
        plt.figure(figsize=(10, 5))
        
        # Agregasi data per bulan untuk 'casual' dan 'registered'
        category_df = main_df.groupby('mnth')[['casual', 'registered']].sum().reset_index()
        
        # Ambil jumlah bulan yang ada di data
        bulan_tersedia = category_df['mnth'].values
        x = np.arange(len(bulan_tersedia))  # Sesuaikan sumbu X dengan jumlah bulan yang tersedia
        lebar = 0.35  # Lebar bar
        
        fig, ax = plt.subplots()
        
        casual_counts = category_df['casual'].values  # Ambil data kasual sesuai bulan yang tersedia
        registered_counts = category_df['registered'].values  # Ambil data terdaftar sesuai bulan yang tersedia
        
        # Membuat bar untuk kategori kasual dan terdaftar
        bar_a = ax.bar(x - lebar/2, casual_counts, lebar, label='Kasual', color='blue')
        bar_b = ax.bar(x + lebar/2, registered_counts, lebar, label='Terdaftar', color='orange')
        
        # Set label sumbu dan judul
        ax.set_xlabel('Bulan')
        ax.set_ylabel('Jumlah Pengguna Sepeda')
        
        # Label bulan harus dinamis, sesuai dengan bulan yang tersedia
        ax.set_xticks(x)  
        ax.set_xticklabels([f"Bulan {int(bulan)}" for bulan in bulan_tersedia])  # Labelkan berdasarkan bulan yang ada
        
        ax.legend() 
        st.pyplot(fig)

