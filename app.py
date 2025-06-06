import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la app
st.title("Análisis de vehículos en EE.UU.")

# Cargar los datos
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

df = load_data()

# Vista previa
st.subheader("Vista previa del dataset")
st.dataframe(df.head())

# Filtro por tipo de vehículo
st.subheader("Filtrar por tipo de vehículo")
tipos = df['type'].dropna().unique()
tipo_seleccionado = st.selectbox("Selecciona un tipo", tipos)
df_filtrado = df[df['type'] == tipo_seleccionado]

# Mostrar tabla filtrada
st.write(f"Mostrando resultados para: {tipo_seleccionado}")
st.dataframe(df_filtrado)

# 🔹 Histograma de precios
st.subheader("Distribución de precios")
fig1, ax1 = plt.subplots()
df_filtrado['price'].hist(bins=30, color='skyblue', edgecolor='black', ax=ax1)
ax1.set_title("Histograma de precios")
ax1.set_xlabel("Precio")
ax1.set_ylabel("Frecuencia")
st.pyplot(fig1)

# 🔹 Gráfico de dispersión: precio vs año del modelo
st.subheader("Precio vs Año del Modelo")
fig2, ax2 = plt.subplots()
ax2.scatter(df_filtrado['model_year'], df_filtrado['price'], alpha=0.5)
ax2.set_title("Dispersión: Año vs Precio")
ax2.set_xlabel("Año del Modelo")
ax2.set_ylabel("Precio")
st.pyplot(fig2)

# 🔹 Casilla para mostrar número de registros
if st.checkbox("Mostrar número de registros filtrados"):
    st.write(f"Total de vehículos mostrados: {df_filtrado.shape[0]}")