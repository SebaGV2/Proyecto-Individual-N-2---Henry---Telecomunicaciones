import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título del Dashboard
st.title("Comportamiento del Sector Internet en Argentina")
st.markdown("Este dashboard interactivo analiza indicadores clave y tendencias del acceso a internet en el país.")

# -------------------------------------------
# Función para cargar datos
# -------------------------------------------
@st.cache_data
def cargar_datos():
    # Cargar el archivo Excel y las hojas necesarias
    internet_data = pd.ExcelFile('Internet.xlsx')
    df_tecnologia = internet_data.parse('Accesos Por Tecnología')
    df_rangos = internet_data.parse('Accesos por rangos')
    df_penetracion_hogares = internet_data.parse('Penetracion-hogares')
    return df_tecnologia, df_rangos, df_penetracion_hogares

# Cargar los datos
df_tecnologia, df_rangos, df_penetracion_hogares = cargar_datos()

# -------------------------------------------
# Filtros interactivos
# -------------------------------------------
st.markdown("### Filtros Interactivos")

# Filtro de provincias
provincias = sorted(df_penetracion_hogares['Provincia'].dropna().unique())
if st.button("Seleccionar todas las provincias"):
    provincias_seleccionadas = provincias
else:
    provincias_seleccionadas = st.multiselect("Seleccione Provincias", provincias, default=provincias)

# Filtro por trimestre
df_penetracion_hogares['Trimestre'] = pd.to_numeric(df_penetracion_hogares['Trimestre'], errors='coerce')
trimestres = sorted(df_penetracion_hogares['Trimestre'].dropna().unique().astype(int))
trimestres_seleccionados = st.multiselect("Seleccione Trimestres", trimestres, default=trimestres)

# Aplicar filtros
df_penetracion_hogares_filtrado = df_penetracion_hogares[
    (df_penetracion_hogares['Provincia'].isin(provincias_seleccionadas)) &
    (df_penetracion_hogares['Trimestre'].isin(trimestres_seleccionados))
]

df_tecnologia_filtrado = df_tecnologia[df_tecnologia['Provincia'].isin(provincias_seleccionadas)]
df_rangos_filtrado = df_rangos[df_rangos['Provincia'].isin(provincias_seleccionadas)]

# -------------------------------------------
# Indicadores principales
# -------------------------------------------
st.markdown("### Indicadores Clave")

# Total accesos
total_accesos = df_tecnologia_filtrado[['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']].sum().sum()

# Velocidad promedio
vel_promedio = df_penetracion_hogares_filtrado['Accesos por cada 100 hogares'].mean()

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Total Accesos", value=f"{total_accesos:,.0f}")
with col2:
    st.metric(label="Velocidad Promedio (Mbps)", value=f"{vel_promedio:.2f}")

# -------------------------------------------
# KPI del 2%
# -------------------------------------------
st.markdown("### KPI del 2%: Accesos por cada 100 hogares")

# Calcular KPI dinámico
def calcular_kpi(df):
    if df.empty:
        return None
    df['Cambio (%)'] = df.groupby('Provincia')['Accesos por cada 100 hogares'].pct_change() * 100
    kpi_total = df['Cambio (%)'].mean()
    return kpi_total

kpi_total = calcular_kpi(df_penetracion_hogares_filtrado)
if kpi_total is not None:
    cumple_meta = "Cumple" if kpi_total >= 2 else "No cumple"
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; margin: 20px; padding: 20px; border: 2px solid #ddd; border-radius: 10px; background-color: {'#d4edda' if cumple_meta == 'Cumple' else '#f8d7da'};">
            <h2 style="margin: 0;">{kpi_total:.2f}%</h2>
            <p style="margin: 5px 0;">{cumple_meta}</p>
            <p style="margin: 0; font-size: 14px; color: #555;">Promedio de crecimiento según filtros seleccionados</p>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("No hay datos disponibles para los filtros seleccionados.")

# -------------------------------------------
# Gráficos principales
# -------------------------------------------
st.markdown("### Visualizaciones de Datos")

# Fila de gráficos
col1, col2 = st.columns(2)

with col1:
    # Gráfico de accesos por tecnología
    tecnologias = ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']
    if not df_tecnologia_filtrado.empty:
        df_tecnologia_filtrado['Total Tecnología'] = df_tecnologia_filtrado[tecnologias].sum(axis=1)
        for col in tecnologias:
            df_tecnologia_filtrado[f'Pct_{col}'] = (df_tecnologia_filtrado[col] / df_tecnologia_filtrado['Total Tecnología']) * 100

        fig, ax = plt.subplots(figsize=(5, 5))
        df_tecnologia_filtrado.groupby('Provincia')[[f'Pct_{col}' for col in tecnologias]].mean().plot(
            kind='bar', stacked=True, ax=ax
        )
        plt.title('Distribución de Accesos por Tecnología')
        st.pyplot(fig)
    else:
        st.warning("No hay datos disponibles para el gráfico de accesos por tecnología.")

with col2:
    # Gráfico de accesos por rango de velocidad
    rango_cols = ['HASTA 512 kbps', '+ 512 Kbps - 1 Mbps', '+ 1 Mbps - 6 Mbps',
                  '+ 6 Mbps - 10 Mbps', '+ 10 Mbps - 20 Mbps', '+ 20 Mbps - 30 Mbps', '+ 30 Mbps']
    if not df_rangos_filtrado.empty:
        df_rangos_grouped = df_rangos_filtrado.groupby('Provincia')[rango_cols].sum()

        fig, ax = plt.subplots(figsize=(5, 5))
        df_rangos_grouped.plot(kind='bar', stacked=True, ax=ax, colormap='plasma')
        plt.title('Accesos por Rango de Velocidad')
        st.pyplot(fig)
    else:
        st.warning("No hay datos disponibles para el gráfico de accesos por rango de velocidad.")

# Fila de gráficos inferiores
col3, col4 = st.columns(2)

with col3:
    # Gráfico de evolución de accesos por cada 100 hogares
    if not df_penetracion_hogares_filtrado.empty:
        fig, ax = plt.subplots(figsize=(5, 5))
        df_penetracion_hogares_filtrado.groupby('Año')['Accesos por cada 100 hogares'].mean().plot(kind='line', marker='o', ax=ax)
        plt.title('Evolución de Accesos por 100 Hogares')
        plt.xlabel('Año')
        plt.ylabel('Accesos por cada 100 hogares')
        plt.grid(True)
        st.pyplot(fig)
    else:
        st.warning("No hay datos disponibles para el gráfico de evolución de accesos.")

with col4:
    # Gráfico de conexiones por tecnología
    if not df_tecnologia_filtrado.empty:
        fig, ax = plt.subplots(figsize=(5, 5))
        df_tecnologia_filtrado[tecnologias].sum().plot(kind='pie', autopct='%1.1f%%', ax=ax, startangle=90)
        plt.title('Conexiones por Tecnología')
        plt.ylabel("")  # Ocultar etiqueta del eje Y
        st.pyplot(fig)
    else:
        st.warning("No hay datos disponibles para el gráfico de conexiones por tecnología.")
