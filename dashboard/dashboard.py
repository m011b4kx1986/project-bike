# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:10:38 2024

@author: hp
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  

st.title('Data Penggunaan Sepeda Tahun 2011')
st.header('Visualisasi Data')

data = pd.read_csv('all-data.csv')

tab1, tab2 = st.tabs(["Total Pengguna", "Kategori"])

#Tab untuk menampilkan total pengguna
with tab1:
    with st.container():
        st.write("Jumlah Pengguna Sepeda Tahun 2011")
        
        plt.figure(figsize=(10, 5))
        monthly_counts = data.groupby('mnth')['cnt'].sum()  
        plt.bar(monthly_counts.index, monthly_counts.values, color='skyblue')  
        plt.xlabel("Bulan")
        plt.ylabel("Jumlah Pengguna")
        plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])  
        st.pyplot(plt)
        plt.clf()  

#Tab untuk menampilkan pengguna sepeda kasual dan terdaftar
with tab2:
    with st.container():
        st.write("Pengguna Sepeda Kasual dan Terdaftar Tahun 2011")
        
        plt.figure(figsize=(10, 5))
        bulan = data['mnth'].unique()  
        x = np.arange(len(bulan))  
        lebar = 0.35  # Lebar bar
        fig, ax = plt.subplots()
        # Mengelompokkan dan menghitung jumlah kasual dan terdaftar per bulan
        casual_counts = data.groupby('mnth')['casual'].sum().values
        registered_counts = data.groupby('mnth')['registered'].sum().values

        # Membuat bar untuk kategori kasual dan terdaftar
        bar_a = ax.bar(x - lebar/2, casual_counts, lebar, label='Kasual', color='blue')
        bar_b = ax.bar(x + lebar/2, registered_counts, lebar, label='Terdaftar', color='orange')

        ax.set_xlabel('Bulan')
        ax.set_ylabel('Jumlah Pengguna Sepeda')
        ax.set_xticks(x)  
        ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])  
        ax.legend() 
        st.pyplot(fig) 

