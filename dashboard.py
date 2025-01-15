import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título del Dashboard
st.title("Análisis de Telecomunicaciones en Argentina")
st.markdown("Este dashboard interactivo analiza KPIs clave sobre el acceso a internet en Argentina.")

# Cargar datos
@st.cache_data
def cargar_datos():
    internet_data = pd.ExcelFile('Internet.xlsx')
    df_tecnologia = internet_data.parse('Accesos Por Tecnología')
    df_poblacion = internet_data.parse('Penetración-poblacion')
    df_rangos = internet_data.parse('Accesos por rangos')
    df_penetracion_hogares = internet_data.parse('Penetracion-hogares')
    return df_tecnologia, df_poblacion, df_rangos, df_penetracion_hogares

df_tecnologia, df_poblacion, df_rangos, df_penetracion_hogares = cargar_datos()

# Panel 1: KPIs Globales
st.header("KPIs Globales")
st.subheader("Crecimiento de accesos por tecnología")
df_tecnologia['Total Tecnología'] = (df_tecnologia['ADSL'] + df_tecnologia['Cablemodem'] + 
                                     df_tecnologia['Fibra óptica'] + df_tecnologia['Wireless'] + 
                                     df_tecnologia['Otros'])

# Calcular porcentajes
for col in ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']:
    df_tecnologia[f'Pct_{col}'] = (df_tecnologia[col] / df_tecnologia['Total Tecnología']) * 100

# Gráfico
fig, ax = plt.subplots(figsize=(10, 6))
df_tecnologia.groupby('Provincia')[['Pct_ADSL', 'Pct_Cablemodem', 'Pct_Fibra óptica']].mean().plot(kind='bar', stacked=True, ax=ax)
plt.title('Distribución porcentual de accesos por tecnología')
st.pyplot(fig)

# Panel 2: Rangos de Velocidad
st.header("Análisis de Rangos de Velocidad")
st.subheader("Distribución de accesos por rangos de velocidad")
rango_cols = ['HASTA 512 kbps', '+ 512 Kbps - 1 Mbps', '+ 1 Mbps - 6 Mbps', 
              '+ 6 Mbps - 10 Mbps', '+ 10 Mbps - 20 Mbps', '+ 20 Mbps - 30 Mbps', '+ 30 Mbps']
df_rangos_grouped = df_rangos.groupby('Provincia')[rango_cols].sum()

fig, ax = plt.subplots(figsize=(10, 6))
df_rangos_grouped.plot(kind='bar', stacked=True, ax=ax, colormap='plasma')
plt.title('Distribución de accesos por rango de velocidad')
st.pyplot(fig)

# Panel 3: Tendencias Temporales
st.header("Tendencias Temporales")
st.subheader("Evolución de accesos por cada 100 hogares")
fig, ax = plt.subplots(figsize=(10, 6))
df_penetracion_hogares.groupby('Año')['Accesos por cada 100 hogares'].mean().plot(kind='line', marker='o', ax=ax)
plt.title('Tendencia de accesos por cada 100 hogares')
plt.xlabel('Año')
plt.ylabel('Accesos por cada 100 hogares')
plt.grid(True)
st.pyplot(fig)

st.markdown("### Conclusiones")
st.markdown("""
1. Hay una brecha significativa en la conectividad entre provincias.
2. Las provincias con mayor penetración de fibra óptica lideran en infraestructura tecnológica.
3. El acceso ha crecido constantemente desde 2014, con un aumento significativo en 2020.
""")

