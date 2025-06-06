import streamlit as st
import pandas as pd

# Título de la app
st.title("Análisis de vehículos en EE.UU.")

# Cargar el dataset
@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    return df

df = load_data()

# Mostrar una vista previa de los datos
st.subheader("Vista previa del dataset")
st.dataframe(df.head())

# Filtro por tipo de vehículo
st.subheader("Filtrar por tipo de vehículo")
tipos = df['type'].dropna().unique()
tipo_seleccionado = st.selectbox("Selecciona un tipo", tipos)
df_filtrado = df[df['type'] == tipo_seleccionado]

# Mostrar resultados filtrados
st.write(f"Mostrando resultados para: {tipo_seleccionado}")
st.dataframe(df_filtrado)