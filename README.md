# Análisis de Telecomunicaciones en Argentina 📊

Este proyecto presenta un análisis interactivo sobre el acceso a internet en Argentina, utilizando un dashboard desarrollado con **Streamlit**. El objetivo principal es explorar indicadores clave de conectividad, evaluar brechas digitales y proponer soluciones basadas en datos.

## **Contenido del Proyecto**

1. [Objetivo del Análisis](#objetivo-del-análisis)
2. [Descripción del Dashboard](#descripción-del-dashboard)
3. [KPIs Analizados](#kpis-analizados)
4. [Filtros Interactivos](#filtros-interactivos)
5. [Requisitos para Ejecutar el Dashboard](#requisitos-para-ejecutar-el-dashboard)
6. [Instrucciones de Ejecución](#instrucciones-de-ejecución)
7. [Conclusiones](#conclusiones)

---

## **Objetivo del Análisis**

El acceso a internet es un factor crucial en el desarrollo económico, educativo y social. Este análisis tiene como propósito:
- Identificar las brechas en conectividad entre provincias.
- Evaluar la calidad y cantidad de accesos a internet en función de la tecnología y velocidad.
- Proponer soluciones para mejorar la infraestructura digital en regiones rezagadas.

---

## **Descripción del Dashboard**

El dashboard interactivo está dividido en **tres paneles principales** y **cuatro filtros** que permiten personalizar la visualización de los datos.

### **Paneles Principales:**
1. **Crecimiento de Accesos por Tecnología:**
   - Visualización: Gráfico de barras apiladas.
   - Muestra la distribución de accesos por tecnología (ADSL, Cablemodem, Fibra Óptica, Wireless, Otros).
   
2. **Distribución de Rangos de Velocidad:**
   - Visualización: Gráfico de barras apiladas.
   - Representa cómo se distribuyen los accesos en diferentes rangos de velocidad (desde menos de 512 kbps hasta más de 30 Mbps).

3. **Tendencias Temporales:**
   - Visualización: Gráfico de líneas.
   - Muestra la evolución de los accesos por cada 100 hogares desde 2014 hasta 2024.

4. **Conexiones por Tecnología:**
   - Visualización: Gráfico de torta.
   - Representa la proporción de conexiones por tecnología en el total nacional.

---

## **KPIs Analizados**

1. **Distribución de Accesos por Tecnología:**
   - Proporción de accesos en tecnologías como ADSL, Fibra Óptica, etc., en cada provincia.
   
2. **Distribución de Accesos por Rangos de Velocidad:**
   - Evaluación de la calidad de conexión en términos de velocidad.
   
3. **Tendencia de Crecimiento:**
   - Evolución de los accesos por cada 100 hogares a lo largo del tiempo.

4. **KPI del 2%:**
   - Evalúa si el crecimiento en los accesos por cada 100 hogares trimestre a trimestre cumple con el objetivo de al menos un 2%.

---

## **Filtros Interactivos**

El dashboard incluye **filtros dinámicos** que permiten ajustar la visualización según los intereses del usuario:
1. **Provincias:** Selecciona una o varias provincias para el análisis.
   - Incluye un botón para seleccionar todas las provincias.
2. **Trimestres:** Filtra los datos por uno o varios trimestres.
3. **Tecnologías:** Permite elegir tecnologías específicas (ADSL, Cablemodem, etc.).
4. **Rangos de Velocidad:** Ajusta el análisis en función de los rangos de velocidad seleccionados.

---

## **Requisitos para Ejecutar el Dashboard**

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes elementos:
- **Python 3.9 o superior.**
- Librerías necesarias:
  - `streamlit`
  - `pandas`
  - `matplotlib`

---

