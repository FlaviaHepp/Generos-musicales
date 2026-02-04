# Generos-musicales
Análisis de una encuesta según gustos de géneros musicales.

Se ingresó a Python y se visualizó el archivo generos_musicales.csv, utilizando la librería de Pandas. Este dataset, contiene información sobre datos de una encuesta de géneros musicales.
Se Realizó un análisis exploratorio de datos del Dataframe, especificando los principales hallazgos. 
Para desarrollar a profundidad el análisis se buscó dar respuestas a algunas inquietudes y a su vez segmentar la encuesta. 
Mediante la biblioteca de Matplotlib, se confeccionaron 2 visualizaciones de datos con sus correspondientes interpretaciones.
Por último, se generó una pequeña conclusión de la encuesta efectuada.

# Análisis de géneros musicales según edad y país

Este proyecto realiza un **análisis exploratorio de datos (EDA)** a partir de una encuesta sobre preferencias musicales, con el objetivo de **identificar patrones de consumo de géneros musicales según la edad y el país** de los encuestados.

El análisis combina filtrado de datos, estadísticas descriptivas y visualización para responder preguntas específicas.

---

## 🎵 Contexto del análisis

Las preferencias musicales varían según factores demográficos como la edad y el país.  
Este proyecto busca entender:

- qué géneros musicales son más populares
- cómo cambian las preferencias según el rango etario
- en qué países se escucha más cada género

---

## 🎯 Objetivos

- Analizar la distribución de géneros musicales
- Identificar preferencias musicales por rango de edad
- Detectar países con mayor consumo de ciertos géneros
- Visualizar resultados de forma clara e interpretables

---

## 📊 Dataset

El dataset proviene de una encuesta y contiene **4 columnas**:

- `Nombre`
- `Edad` (entre 12 y 75 años)
- `País`
- `Género musical`  
  - Electrónica  
  - Jazz  
  - Rock  
  - Pop  
  - Cumbia  

El archivo utilizado es `generos_musicales.csv`.

---

## 🧪 Metodología

### 1. Carga y exploración de datos
- Lectura del archivo CSV con pandas
- Visualización inicial del dataset
- Conteo de personas por género musical

### 2. Análisis por condiciones
- Personas mayores de 35 años que escuchan Rock
- País donde más se escucha Pop
- País donde más se escucha Jazz
- Géneros escuchados por personas entre 25 y 55 años

### 3. Segmentación por edad
- Análisis de preferencias musicales en el rango 25–55 años
- Comparación de géneros mediante conteos y porcentajes

---

## 📈 Visualizaciones

- **Gráfico de torta**:
  - distribución porcentual de géneros musicales para personas entre 25 y 55 años
- **Gráfico de barras**:
  - comparación de porcentajes por género musical
  - etiquetas personalizadas para facilitar la lectura

Las visualizaciones permiten observar rápidamente **tendencias de preferencia musical por edad**.

---

## 📌 Principales insights

- Algunos géneros musicales predominan en rangos etarios específicos
- El rango de 25 a 55 años presenta una distribución variada de preferencias
- Existen diferencias claras entre géneros más y menos populares
- El análisis por país permite detectar focos de consumo cultural

---

## 🛠️ Tecnologías utilizadas

- **Python**
- **pandas**
- **NumPy**
- **matplotlib**

---

## 📂 Estructura del repositorio

├── generos_musicales.csv
├── Análisis de géneros musicales.py
├── README.md


---

## 🚀 Próximos pasos

- Calcular porcentajes por país
- Analizar diferencias entre rangos etarios más pequeños
- Incorporar métricas de preferencia relativa
- Crear visualizaciones interactivas
- Ampliar el dataset para análisis más robustos

---

## 👤 Autor

**Flavia Hepp**  
Data Analyst en formación  
