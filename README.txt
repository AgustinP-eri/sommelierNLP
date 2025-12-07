# 🍷 Sommelier Virtual con NLP

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

Este proyecto es una aplicación web interactiva que funciona como un **Sommelier de Vinos Inteligente**. Utiliza técnicas de Procesamiento de Lenguaje Natural (NLP) para analizar descripciones de vinos y recomendar la mejor opción basada en las preferencias del usuario.

## 🚀 Descripción del Proyecto

El objetivo principal de este proyecto fue construir un sistema de recomendación "End-to-End", abarcando desde la limpieza de datos crudos hasta el despliegue de una interfaz de usuario funcional.

La aplicación permite al usuario ingresar una descripción de lo que busca (ej: *"Un vino tinto con notas de madera y frutos rojos"*) y el modelo devuelve las mejores coincidencias basándose en la similitud del texto.

## 📂 Estructura del Repositorio

* **`app.py`**: Código fuente de la aplicación web construida con Streamlit. Contiene la lógica de inferencia y la interfaz de usuario.
* **`notebooks/NLP_EDA_Limpieza.ipynb`**: 📓 **Notebook Principal**. Aquí se encuentra el "corazón" del análisis de datos. Incluye:
    * Limpieza y Preprocesamiento de datos (Manejo de nulos, normalización de texto).
    * **EDA (Exploratorio de Datos)**: Gráficos y análisis de distribución de las variables.
    * Construcción del modelo de NLP (Vectorización).
* **`requirements.txt`**: Lista de dependencias necesarias para ejecutar el proyecto.
* **`data/`**: Contiene el dataset utilizado (si aplica).

## 🛠️ Tecnologías y Herramientas

* **Python**: Lenguaje principal.
* **Pandas & NumPy**: Manipulación y análisis de datos.
* **Scikit-learn**: Para la vectorización de texto (TF-IDF/CountVectorizer) y cálculo de similitud (Cosine Similarity).
* **Streamlit**: Framework para la creación rápida de la web app.
* **Matplotlib/Seaborn**: Para la visualización de datos en el EDA.

## 🧠 Metodología y Colaboración con IA

Este proyecto destaca por combinar habilidades técnicas tradicionales con flujos de trabajo modernos:

1.  **Fundamentos de Data Science**: La limpieza, el análisis exploratorio (EDA) y la creación del modelo de recomendación fueron desarrollados meticulosamente en el entorno de Jupyter Notebook.
2.  **Desarrollo Acelerado con IA Generativa**: Para la etapa de despliegue ("Deployment"), utilicé **Inteligencia Artificial Generativa** como asistente de programación (pair-programmer). Esto me permitió iterar rápidamente sobre el diseño de la interfaz en Streamlit y llevar el modelo de un notebook a una web funcional en tiempo récord.

## 💻 Cómo ejecutarlo localmente

Si deseas correr este proyecto en tu máquina local:

1.  Clona el repositorio:
    ```bash
    git clone [https://github.com/AgustinP-eri/somelierNLP.git](https://github.com/AgustinP-eri/somelierNLP.git)
    ```
2.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Ejecuta la aplicación:
    ```bash
    streamlit run app.py
    ```

## 📊 Visualización del EDA

Te invito a revisar el archivo `notebooks/NLP_EDA_Limpieza.ipynb` para ver el detalle del análisis de los datos y cómo se limpiaron las descripciones de los vinos antes de entrenar el modelo.