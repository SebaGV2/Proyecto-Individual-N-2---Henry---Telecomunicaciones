Análisis de Telecomunicaciones en Argentina 📊

Este proyecto presenta un análisis interactivo sobre el acceso a internet en Argentina, utilizando un dashboard desarrollado con Streamlit. El objetivo principal es explorar indicadores clave de conectividad, evaluar brechas digitales y proponer soluciones basadas en datos.

Contenido del Proyecto

Objetivo del Análisis

Descripción del Dashboard

KPIs Analizados

Filtros Interactivos

Requisitos para Ejecutar el Dashboard

Instrucciones de Ejecución

Conclusiones

Objetivo del Análisis

El acceso a internet es un factor crucial en el desarrollo económico, educativo y social. Este análisis tiene como propósito:

Identificar las brechas en conectividad entre provincias.

Evaluar la calidad y cantidad de accesos a internet en función de la tecnología y velocidad.

Proponer soluciones para mejorar la infraestructura digital en regiones rezagadas.

Descripción del Dashboard

El dashboard interactivo está dividido en tres paneles principales y cuatro filtros que permiten personalizar la visualización de los datos.

Paneles Principales:

Crecimiento de Accesos por Tecnología:

Visualización: Gráfico de barras apiladas.

Muestra la distribución de accesos por tecnología (ADSL, Cablemodem, Fibra Óptica, Wireless, Otros).

Distribución de Rangos de Velocidad:

Visualización: Gráfico de barras apiladas.

Representa cómo se distribuyen los accesos en diferentes rangos de velocidad (desde menos de 512 kbps hasta más de 30 Mbps).

Tendencias Temporales:

Visualización: Gráfico de líneas.

Muestra la evolución de los accesos por cada 100 hogares desde 2014 hasta 2024.

Conexiones por Tecnología:

Visualización: Gráfico de torta.

Representa la proporción de conexiones por tecnología en el total nacional.

KPIs Analizados

Distribución de Accesos por Tecnología:

Proporción de accesos en tecnologías como ADSL, Fibra Óptica, etc., en cada provincia.

Distribución de Accesos por Rangos de Velocidad:

Evaluación de la calidad de conexión en términos de velocidad.

Tendencia de Crecimiento:

Evolución de los accesos por cada 100 hogares a lo largo del tiempo.

KPI del 2%:

Evalúa si el crecimiento en los accesos por cada 100 hogares trimestre a trimestre cumple con el objetivo de al menos un 2%.

Filtros Interactivos

El dashboard incluye filtros dinámicos que permiten ajustar la visualización según los intereses del usuario:

Provincias: Selecciona una o varias provincias para el análisis.

Incluye un botón para seleccionar todas las provincias.

Trimestres: Filtra los datos por uno o varios trimestres.

Tecnologías: Permite elegir tecnologías específicas (ADSL, Cablemodem, etc.).

Rangos de Velocidad: Ajusta el análisis en función de los rangos de velocidad seleccionados.

Requisitos para Ejecutar el Dashboard

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes elementos:

Python 3.9 o superior.

Librerías necesarias:

streamlit

pandas

matplotlib

Instrucciones de Ejecución

Clona este repositorio en tu máquina local:

git clone <URL_DEL_REPOSITORIO>

Navega a la carpeta del proyecto:

cd <CARPETA_DEL_PROYECTO>

Instala las dependencias necesarias:

pip install -r requirements.txt

Ejecuta el dashboard:

streamlit run dashboard.py

Abre el enlace generado por Streamlit en tu navegador para interactuar con el dashboard.

Conclusiones

KPI del 2%:

Permite evaluar si las provincias seleccionadas cumplen con el objetivo de crecimiento trimestre a trimestre.

Brechas Tecnológicas:

Provincias con mayor uso de fibra óptica suelen estar más avanzadas tecnológicamente.

Las provincias con predominancia de ADSL y Wireless presentan retos en infraestructura.

Tendencias:

Crecimiento sostenido de accesos a internet en los últimos años, con aceleración en períodos críticos como la pandemia.

¡Gracias por explorar este análisis interactivo sobre las telecomunicaciones en Argentina! 🚀

