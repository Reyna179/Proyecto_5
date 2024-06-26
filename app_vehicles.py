import pandas as pd
import plotly express as px
import streamlit as st


data_vehicles = pd.read_csv('vehicles_us.csv') #leer archivo de datos

#st.header()

hist_button = st.button('Construir histograma') #crear un histograma
if hist_button:
   #escribir un mensaje
   st.write('Creacion de un histograma para el conjunto de datos de anuncio de venta de coches')

#crea un histograma
fig = px.histogram(car_data, x='odometer')

#mostrar grafico Plotly interactivo
st.plotly_chart(fig, use_container_width = True)
