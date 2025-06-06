import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración inicial
st.set_page_config(page_title="Dashboard de vehículos", layout="centered")

# Título
st.title("Análisis de vehículos en EE.UU.")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    return df

df = load_data()

# Vista previa
st.subheader("Vista previa del dataset")
st.dataframe(df.head())

# Filtro por tipo de vehículo
tipos = df['type'].dropna().unique()
tipo = st.selectbox("Selecciona un tipo de vehículo", sorted(tipos))
df_filtrado = df[df['type'] == tipo]

# Mostrar cantidad si se activa la casilla
if st.checkbox("Mostrar cantidad de registros"):
    st.write(f"Total de vehículos tipo **{tipo}**: {df_filtrado.shape[0]}")

# Histograma: precios por tipo
st.subheader("Distribución de precios")
fig1, ax1 = plt.subplots()
df_filtrado['price'].hist(bins=30, color='lightgreen', edgecolor='black', ax=ax1)
ax1.set_title("Histograma de precios")
ax1.set_xlabel("Precio (USD)")
ax1.set_ylabel("Frecuencia")
st.pyplot(fig1)

# Gráfico de dispersión: precio vs año
st.subheader("Relación entre año del modelo y precio")
fig2, ax2 = plt.subplots()
ax2.scatter(df_filtrado['model_year'], df_filtrado['price'], alpha=0.5)
ax2.set_title("Precio vs Año del Modelo")
ax2.set_xlabel("Año del Modelo")
ax2.set_ylabel("Precio")
st.pyplot(fig2)