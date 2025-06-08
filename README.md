# Proyecto 7 – Dashboard interactivo con Streamlit

Este proyecto forma parte del Bootcamp de Data Science. Consiste en la creación de una aplicación web desarrollada con Streamlit que permite explorar de forma interactiva un conjunto de datos de anuncios de vehículos en Estados Unidos.

**App desplegada en Render:** https://vehicle-app-sc1.onrender.com

## Descripción del proyecto

La aplicación permite:

- Visualizar los primeros registros del conjunto de datos
- Filtrar vehículos por tipo (SUV, sedan, pickup, etc.)
- Consultar el número total de registros filtrados
- Explorar la distribución de precios con un histograma (opcional mediante casilla)
- Visualizar un gráfico de dispersión de precio vs año del modelo

Los gráficos se generan usando Plotly, lo que permite una experiencia interactiva (zoom, hover, selección).

## Dataset utilizado

El dataset `vehicles_us.csv` contiene información real de anuncios de venta de autos, incluyendo:

- Precio
- Año del modelo
- Tipo de vehículo
- Estado (condición)
- Número de cilindros
- Tipo de transmisión
- Kilometraje (odómetro)
- Tipo de combustible

## Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- Plotly Express
- Git y GitHub
- Render (para despliegue en la web)

## Cómo ejecutar la app localmente

Clona este repositorio:

```bash
git clone https://github.com/andre0518/vehicle-app.git
cd vehicle-app
