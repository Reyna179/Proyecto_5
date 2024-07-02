import pandas as pd
import plotly_express as px
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv')  # leer archivo de datos

# Crear una columna con el nombre del manufacturero por cada modelo, sacandolo de la columna de modelo
separado = car_data["model"].str.split(" ", n=1, expand=True)
car_data['mfg'] = separado[0]


st.title('Análisis de venta de coches')

st.header('En esta aplicación mostramos gráficos interactivos del análisis de la venta de coches de un distribuidor')

st.dataframe(car_data)

# Histograma de condiciones vs año
hist_button = st.button('Construir histograma')
if hist_button:

    st.write(
        # escribir un mensaje
        'Creacion de un histograma para el conjunto de datos de anuncio de venta de coches')
    fig_hist_1 = px.histogram(car_data, color='condition', x='model_year')
    fig_hist_1.update_layout(
        title="Condicion vs Año",
        xaxis_title="Año",
        yaxis_title="Cantidad",
        width=1000,
        height=600)
    # fig_hist_1.show()
    # mostrar grafico Plotly interactivo
    st.plotly_chart(fig_hist_1, use_container_width=True)

# Grafico de dispersion comparativo Precio - Año - Millaje
checkbox = st.checkbox('Ver comparativo Precio - Año - Millaje')
if checkbox:
    st.write(
        'Creacion de grafico de dispersion comparativo de Precio-Año-Millaje')
    # crear un grafico de dispersion
    fig_scatter = px.scatter(
        car_data, x='price', y='odometer', color='model_year')
    fig_scatter.update_layout(
        title="Grafico de comparativa: Precio - Año - Millaje",
        xaxis_title="Millaje",
        yaxis_title="Precio",
        legend_title_text='Año',
        width=1000,
        height=600)
    # mostrar grafico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)


# Grafico de linea para el promedio de dias en venta por tipo de auto
car_data_days = car_data.groupby('type')['days_listed'].mean()
# print(car_data_days)
fig_line = px.line(car_data_days, y='days_listed', orientation="v")
fig_line.update_layout(
    title="Promedio de dias en venta por tipo de modelo",
    xaxis_title="Tipo de auto",
    yaxis_title="Dias en venta",
    width=1000,
    height=600)
fig_line.update_traces(marker={"color": "red"})
st.plotly_chart(fig_line, use_container_width=True)


# Grafico de distribucion de precios por manufacturero de autos
car_data_hist2 = car_data[car_data['price'] < 150000]
bar = st.selectbox('Seleccione la marca de su interes', car_data['mfg'].unique(),
                   index=None,
                   placeholder='Seleccione tipo de auto')

if bar:
    car_data_hist2 = car_data_hist2[car_data_hist2['mfg'] == bar]
    fig_hist_2 = px.histogram(car_data_hist2, color='mfg', x='price')
    fig_hist_2.update_layout(
        title="Distribución de precios por marca de auto",
        xaxis_title="Precio",
        yaxis_title="Cantidad",
        width=1000,
        height=600)
    st.plotly_chart(fig_hist_2, use_container_width=True)
else:
    fig_hist_2 = px.histogram(car_data_hist2, color='mfg', x='price')
    fig_hist_2.update_layout(
        title="Distribución de precios por marca de auto",
        xaxis_title="Precio",
        yaxis_title="Cantidad",
        width=1000,
        height=600)
    st.plotly_chart(fig_hist_2, use_container_width=True)

st.header('Muchas gracias por su visita')
