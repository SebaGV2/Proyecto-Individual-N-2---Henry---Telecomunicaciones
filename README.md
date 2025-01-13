# Análisis de Telecomunicaciones en Argentina

## Introducción
Este proyecto se enfoca en analizar el estado actual de las telecomunicaciones en Argentina, evaluando indicadores clave como:
- Crecimiento de accesos por tecnología.
- Relación entre accesos y población.
- Distribución de accesos por rangos de velocidad.
- Tendencias temporales en la conectividad.

El análisis tiene como objetivo identificar oportunidades de mejora en infraestructura, guiar inversiones y comprender las brechas regionales en el acceso a internet.

## Archivos del Proyecto
El repositorio contiene los siguientes archivos:

### Código
- `eda_telecomunicaciones.py`: Script principal que realiza el análisis, genera gráficos y exporta los resultados.

### Resultados Exportados
- `KPI_Accesos_Tecnologia.csv`: Porcentaje de accesos por tecnología en cada provincia.
- `KPI_Accesos_Poblacion.csv`: Promedio de accesos por cada 100 habitantes en cada provincia.
- `Distribucion_Rangos.csv`: Distribución de accesos por rangos de velocidad en cada provincia.
- `Tendencia_Accesos_Por_Año.csv`: Evolución de accesos por cada 100 hogares a lo largo de los años.

### Datos Originales
- `Internet.xlsx`: Dataset principal con la información analizada.

## Metodología
El proyecto sigue una estructura de análisis en tres paneles principales:

### Panel 1: KPIs Globales
- **Crecimiento de accesos por tecnología:**
  - Calculamos el porcentaje de accesos por tecnología (ADSL, Cablemodem, Fibra óptica, etc.) en cada provincia.
  - **Gráfico:** Barras apiladas que muestran la distribución porcentual por tecnología.
  - **Conclusión:** Provincias como Capital Federal destacan en penetración de fibra óptica, mientras que otras dependen de tecnologías más antiguas.

- **Relación entre accesos y población:**
  - Calculamos el promedio de accesos por cada 100 habitantes en cada provincia.
  - **Gráfico:** Barras simples que comparan el acceso entre provincias.
  - **Conclusión:** Hay desigualdades significativas en el acceso, con provincias como Chaco muy por debajo del promedio nacional.

### Panel 2: Análisis de Rangos de Velocidad
- Agrupamos accesos en diferentes rangos de velocidad (hasta 512 kbps, entre 10-20 Mbps, más de 30 Mbps, etc.).
- **Gráfico:** Barras apiladas por provincia.
- **Conclusión:** Provincias con mayor cantidad de accesos en rangos altos muestran mejor infraestructura tecnológica.

### Panel 3: Tendencias Temporales
- Analizamos la evolución de accesos por cada 100 hogares a lo largo de los años.
- **Gráfico:** Línea que muestra cómo ha crecido la conectividad desde 2014.
- **Conclusión:** El acceso ha crecido constantemente, con un aumento significativo en 2020, posiblemente relacionado con la pandemia.


## Tecnologías Utilizadas
El análisis fue realizado en **Python**, utilizando las siguientes librerías:
- `pandas`: Manipulación y análisis de datos.
- `matplotlib`: Visualización de gráficos.
- `seaborn`: Visualización avanzada.



