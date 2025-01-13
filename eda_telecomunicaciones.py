import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel
internet_data = pd.ExcelFile('Internet.xlsx')

# -------------------------------------------
# 1. Cargar Hojas Principales
# -------------------------------------------

# Penetración por hogares
df_penetracion_hogares = internet_data.parse('Penetracion-hogares')

# Penetración por población
df_poblacion = internet_data.parse('Penetración-poblacion')

# Velocidad por provincia
df_velocidad = internet_data.parse('Velocidad % por prov')

# Accesos por tecnología
df_tecnologia = internet_data.parse('Accesos Por Tecnología')

# Accesos por rangos de velocidad
df_rangos = internet_data.parse('Accesos por rangos')

# -------------------------------------------
# 2. KPI 1: Crecimiento de accesos por tecnología
# -------------------------------------------

# Calcular el total de accesos por tecnología
df_tecnologia['Total Tecnología'] = (df_tecnologia['ADSL'] + df_tecnologia['Cablemodem'] + 
                                     df_tecnologia['Fibra óptica'] + df_tecnologia['Wireless'] + 
                                     df_tecnologia['Otros'])

# Calcular el porcentaje por tecnología
for col in ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']:
    df_tecnologia[f'Pct_{col}'] = (df_tecnologia[col] / df_tecnologia['Total Tecnología']) * 100

# Agrupar y graficar
df_tecnologia_grouped = df_tecnologia.groupby('Provincia')[['Pct_ADSL', 'Pct_Cablemodem', 'Pct_Fibra óptica']].mean()

df_tecnologia_grouped.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis')
plt.title('Distribución porcentual de accesos por tecnología')
plt.ylabel('Porcentaje (%)')
plt.xlabel('Provincia')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# -------------------------------------------
# 3. KPI 2: Relación entre accesos y población
# -------------------------------------------

df_poblacion_grouped = df_poblacion.groupby('Provincia')['Accesos por cada 100 hab'].mean()

df_poblacion_grouped.sort_values().plot(kind='bar', figsize=(12, 6), color='green')
plt.title('Promedio de accesos por cada 100 habitantes')
plt.ylabel('Accesos por cada 100 habitantes')
plt.xlabel('Provincia')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# -------------------------------------------
# 4. Análisis de Rangos de Velocidad
# -------------------------------------------

rango_cols = ['HASTA 512 kbps', '+ 512 Kbps - 1 Mbps', '+ 1 Mbps - 6 Mbps', 
              '+ 6 Mbps - 10 Mbps', '+ 10 Mbps - 20 Mbps', '+ 20 Mbps - 30 Mbps', '+ 30 Mbps']

df_rangos_grouped = df_rangos.groupby('Provincia')[rango_cols].sum()

df_rangos_grouped.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='plasma')
plt.title('Distribución de accesos por rango de velocidad')
plt.ylabel('Número de accesos')
plt.xlabel('Provincia')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# -------------------------------------------
# 5. Tendencias Temporales
# -------------------------------------------

df_penetracion_hogares.groupby('Año')['Accesos por cada 100 hogares'].mean().plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Tendencia de accesos por cada 100 hogares')
plt.xlabel('Año')
plt.ylabel('Accesos por cada 100 hogares')
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------------------
# 6. Exportar Resultados
# -------------------------------------------

df_tecnologia_grouped.to_csv('KPI_Accesos_Tecnologia.csv', index=True)
df_poblacion_grouped.to_csv('KPI_Accesos_Poblacion.csv', header=True)
df_rangos_grouped.to_csv('Distribucion_Rangos.csv', index=True)
df_tendencia_temporal = df_penetracion_hogares.groupby('Año')['Accesos por cada 100 hogares'].mean()
df_tendencia_temporal.to_csv('Tendencia_Accesos_Por_Año.csv', header=True)







