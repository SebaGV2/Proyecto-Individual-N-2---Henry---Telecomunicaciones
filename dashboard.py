import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título del Dashboard
st.title("Análisis de Telecomunicaciones en Argentina")
st.markdown("Este dashboard interactivo analiza KPIs clave sobre el acceso a internet en Argentina.")

# -------------------------------------------
# Función para cargar datos
# -------------------------------------------
@st.cache_data
def cargar_datos():
    # Cargar el archivo Excel y las hojas necesarias
    internet_data = pd.ExcelFile('Internet.xlsx')
    df_tecnologia = internet_data.parse('Accesos Por Tecnología')  # Datos sobre accesos por tecnología
    df_rangos = internet_data.parse('Accesos por rangos')  # Datos sobre rangos de velocidad
    df_penetracion_hogares = internet_data.parse('Penetracion-hogares')  # Datos sobre penetración por hogares
    return df_tecnologia, df_rangos, df_penetracion_hogares

# Cargar los datos
df_tecnologia, df_rangos, df_penetracion_hogares = cargar_datos()

# -------------------------------------------
# Filtros horizontales debajo de los gráficos
# -------------------------------------------
st.markdown("### Filtros")

# Crear una fila con filtros en columnas
col_f1, col_f2, col_f3, col_f4 = st.columns(4)  # Cuatro columnas para los filtros

with col_f1:
    # Filtro de provincias
    provincias = sorted(df_tecnologia['Provincia'].dropna().unique())  # Eliminar NaN y ordenar
    provincias_seleccionadas = st.multiselect("Provincias", provincias, default=provincias)

    # Botón para seleccionar todas las provincias
    if st.button("Seleccionar todas las provincias"):
        provincias_seleccionadas = provincias  # Selecciona todas las provincias disponibles

with col_f2:
    # Filtro por trimestre
    df_tecnologia['Trimestre'] = pd.to_numeric(df_tecnologia['Trimestre'], errors='coerce')
    trimestres = sorted(df_tecnologia['Trimestre'].dropna().unique().astype(int))
    trimestres_seleccionados = st.multiselect("Trimestres", trimestres, default=trimestres)

with col_f3:
    # Filtro por tecnología
    tecnologias = ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']
    tecnologias_seleccionadas = st.multiselect("Tecnologías", tecnologias, default=tecnologias)

with col_f4:
    # Filtro por rangos de velocidad
    rango_cols = ['HASTA 512 kbps', '+ 512 Kbps - 1 Mbps', '+ 1 Mbps - 6 Mbps', 
                  '+ 6 Mbps - 10 Mbps', '+ 10 Mbps - 20 Mbps', '+ 20 Mbps - 30 Mbps', '+ 30 Mbps']
    rangos_seleccionados = st.multiselect("Rangos de Velocidad", rango_cols, default=rango_cols)

# Aplicar filtros a los datos
df_tecnologia_filtrado = df_tecnologia[
    (df_tecnologia['Provincia'].isin(provincias_seleccionadas)) &
    (df_tecnologia['Trimestre'].isin(trimestres_seleccionados))
]

df_rangos_filtrado = df_rangos[
    (df_rangos['Provincia'].isin(provincias_seleccionadas)) &
    (df_rangos['Trimestre'].isin(trimestres_seleccionados))
]

df_penetracion_hogares_filtrado = df_penetracion_hogares[
    (df_penetracion_hogares['Provincia'].isin(provincias_seleccionadas)) &
    (df_penetracion_hogares['Trimestre'].isin(trimestres_seleccionados))
]

# -------------------------------------------
# Gráficos horizontales en la parte superior
# -------------------------------------------
# Dividimos la pantalla en tres columnas para mostrar los gráficos en la misma línea
col1, col2, col3 = st.columns(3)

with col1:
    # Panel 1: KPIs Globales
    st.subheader("Crecimiento de accesos por tecnología")
    df_tecnologia_filtrado['Total Tecnología'] = df_tecnologia_filtrado[tecnologias_seleccionadas].sum(axis=1)
    for col in tecnologias_seleccionadas:
        df_tecnologia_filtrado[f'Pct_{col}'] = (df_tecnologia_filtrado[col] / df_tecnologia_filtrado['Total Tecnología']) * 100

    # Crear gráfico de barras apiladas
    fig, ax = plt.subplots(figsize=(5, 5))
    df_tecnologia_filtrado.groupby('Provincia')[[f'Pct_{col}' for col in tecnologias_seleccionadas]].mean().plot(kind='bar', stacked=True, ax=ax)
    plt.title('Accesos por Tecnología')
    st.pyplot(fig)

with col2:
    # Panel 2: Rangos de Velocidad
    st.subheader("Distribución de rangos de velocidad")
    df_rangos_grouped = df_rangos_filtrado.groupby('Provincia')[rangos_seleccionados].sum()

    # Crear gráfico de barras apiladas
    fig, ax = plt.subplots(figsize=(5, 5))
    df_rangos_grouped.plot(kind='bar', stacked=True, ax=ax, colormap='plasma')
    plt.title('Accesos por Velocidad')
    st.pyplot(fig)

with col3:
    # Panel 3: Tendencias Temporales
    st.subheader("Evolución de accesos por cada 100 hogares")
    fig, ax = plt.subplots(figsize=(5, 5))
    df_penetracion_hogares_filtrado.groupby('Año')['Accesos por cada 100 hogares'].mean().plot(kind='line', marker='o', ax=ax)
    plt.title('Tendencia Temporal')
    plt.xlabel('Año')
    plt.ylabel('Accesos por cada 100 hogares')
    plt.grid(True)
    st.pyplot(fig)


