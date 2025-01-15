# Análisis de Telecomunicaciones en Argentina

## Introducción
Este proyecto presenta un dashboard interactivo desarrollado en **Streamlit** para analizar el estado actual de las telecomunicaciones en Argentina. Los indicadores clave analizados incluyen:

- Crecimiento de accesos por tecnología.
- Relación entre accesos y población.
- Distribución de accesos por rangos de velocidad.
- Tendencias temporales en la conectividad.

El objetivo es identificar oportunidades de mejora en infraestructura, cerrar brechas digitales entre provincias y guiar decisiones de inversión en el sector.



## Archivos del Proyecto
El repositorio contiene los siguientes archivos:

### Código
- `dashboard.py`: Archivo principal que ejecuta el dashboard interactivo.
- `eda_telecomunicaciones.py`: Script que realiza el análisis, genera gráficos y exporta los resultados.

### Resultados Exportados
- `KPI_Accesos_Tecnologia.csv`: Porcentaje de accesos por tecnología en cada provincia.
- `KPI_Accesos_Poblacion.csv`: Promedio de accesos por cada 100 habitantes en cada provincia.
- `Distribucion_Rangos.csv`: Distribución de accesos por rangos de velocidad en cada provincia.
- `Tendencia_Accesos_Por_Año.csv`: Evolución de accesos por cada 100 hogares a lo largo de los años.

### Datos Originales
- `Internet.xlsx`: Dataset principal con la información analizada.

## Metodología

El dashboard se organiza en **tres paneles principales**, cada uno enfocado en un aspecto clave del análisis:

### Panel 1: KPIs Globales
- **Crecimiento de accesos por tecnología:**
  - Analiza la distribución de accesos entre tecnologías como ADSL, Cablemodem y Fibra Óptica.
  - **Gráfico:** Barras apiladas.
  - **Conclusión:** Provincias con mayor penetración de fibra óptica, como Capital Federal, presentan mejor infraestructura.

- **Relación entre accesos y población:**
  - Mide el promedio de accesos por cada 100 habitantes en cada provincia.
  - **Gráfico:** Barras simples.
  - **Conclusión:** Hay disparidades significativas entre provincias como Capital Federal y Chaco.

---

### Panel 2: Rangos de Velocidad
- Analiza la distribución de accesos según rangos de velocidad (por ejemplo, menos de 512 kbps, entre 10 y 20 Mbps, más de 30 Mbps).
- **Gráfico:** Barras apiladas por provincia.
- **Conclusión:** Provincias con mayor cantidad de accesos en rangos altos reflejan mejor infraestructura tecnológica.

---

### Panel 3: Tendencias Temporales
- Estudia la evolución de accesos por cada 100 hogares a lo largo del tiempo.
- **Gráfico:** Línea que muestra el crecimiento desde 2014 hasta 2024.
- **Conclusión:** El acceso ha crecido de forma constante, con un pico significativo en 2020 debido a la pandemia.

---

#### **Conclusiones**
1. **Brechas regionales:** Provincias como Capital Federal lideran en conectividad, mientras que Chaco y Formosa están rezagadas.
2. **Importancia de la fibra óptica:** Esta tecnología es clave para mejorar la infraestructura tecnológica.
3. **Crecimiento sostenido:** Desde 2014, el acceso ha crecido consistentemente, con un aumento notable en 2020.

---



## Tecnologías Utilizadas
Este proyecto fue desarrollado íntegramente en **Python**, utilizando las siguientes herramientas:
- **Streamlit:** Framework para crear dashboards interactivos.
- **Pandas:** Manipulación y análisis de datos.
- **Matplotlib y Seaborn:** Visualización de datos.


