import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título de la aplicación
st.title("Despliegue de Tabla y Gráficos con Streamlit")

# Subir archivo de datos (CSV)
uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Cargar datos
    df = pd.read_csv(uploaded_file)
    
    # Mostrar tabla de datos
    st.write("Tabla de datos:")
    st.dataframe(df)
    
    # Seleccionar columnas para gráficos
    numeric_columns = df.select_dtypes(['float64', 'int64']).columns
    selected_x = st.selectbox("Seleccionar columna para eje X", numeric_columns)
    selected_y = st.selectbox("Seleccionar columna para eje Y", numeric_columns)

    # Gráfico de barras
    st.write("Gráfico de Barras")
    plt.figure(figsize=(10, 5))
    sns.barplot(x=df[selected_x], y=df[selected_y])
    st.pyplot(plt)

    # Gráfico de dispersión
    st.write("Gráfico de Dispersión")
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=df[selected_x], y=df[selected_y])
    st.pyplot(plt)

    # Resumen estadístico
    st.write("Resumen Estadístico:")
    st.write(df.describe())

else:
    st.write("Por favor, carga un archivo CSV para continuar.")
