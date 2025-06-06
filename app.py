import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración inicial
st.set_page_config(page_title="Dashboard de vehículos", layout="centered")

# Título
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
tipos = df['type'].dropna().unique()
tipo = st.selectbox("Selecciona un tipo de vehículo", sorted(tipos))
df_filtrado = df[df['type'] == tipo]

# Mostrar cantidad si se activa la casilla
if st.checkbox("Mostrar cantidad de registros"):
    st.write(f"Total: {df_filtrado.shape[0]} vehículos tipo **{tipo}**")

# Casilla de verificación para construir histograma
if st.checkbox('Construir un histograma'):
    st.subheader("Distribución de precios (interactivo)")
    fig1 = px.histogram(
        df_filtrado,
        x="price",
        nbins=30,
        title="Histograma de precios",
        color_discrete_sequence=["royalblue"]
    )
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico de dispersión siempre visible
st.subheader("Precio vs Año del Modelo (interactivo)")
fig2 = px.scatter(
    df_filtrado,
    x="model_year",
    y="price",
    title="Precio vs Año del Modelo",
    opacity=0.6,
    color_discrete_sequence=["darkorange"]
)
st.plotly_chart(fig2, use_container_width=True)