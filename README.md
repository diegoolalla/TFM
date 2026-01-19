# TFM - Trabajo Final de Máster

## Descripción

Este proyecto contiene el desarrollo completo de un Trabajo Final de Máster (TFM) que consiste en analizar un dataset público siguiendo las fases de modelización analítica:

- ✅ Análisis descriptivo
- ✅ Transformaciones relevantes
- ✅ Generación de modelos predictivos con diferentes técnicas
- ✅ Evaluación de resultados
- ✅ Discusión de conclusiones

## 📁 Estructura del Proyecto

```
TFM/
├── notebooks/              # Jupyter notebooks con análisis
│   └── analisis_tfm.ipynb # Notebook principal del análisis
├── data/                   # Datasets (no incluidos en el repositorio)
│   ├── raw/               # Datos originales
│   └── processed/         # Datos procesados
├── src/                    # Código fuente reutilizable
│   ├── data_utils.py      # Utilidades para carga y procesamiento de datos
│   ├── visualization.py   # Utilidades para visualización
│   └── model_evaluation.py # Utilidades para evaluación de modelos
├── models/                 # Modelos entrenados (no incluidos)
├── results/               # Resultados del análisis
│   ├── visualizations/    # Gráficos y figuras
│   └── metrics/          # Métricas de evaluación
├── reports/              # Informes y documentación
├── docs/                 # Documentación adicional
├── requirements.txt      # Dependencias del proyecto
├── .gitignore           # Archivos ignorados por git
└── README.md            # Este archivo
```

## 🚀 Inicio Rápido

### 1. Clonar el Repositorio

```bash
git clone https://github.com/diegoolalla/TFM.git
cd TFM
```

### 2. Crear Entorno Virtual

```bash
# Con venv
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Con conda
conda create -n tfm python=3.8
conda activate tfm
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el Análisis

```bash
# Iniciar Jupyter Notebook
jupyter notebook notebooks/analisis_tfm.ipynb
```

## 📊 Dataset

Este proyecto está diseñado para trabajar con datasets públicos. Puedes obtener datasets de:

- [Kaggle](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [AWS Open Data](https://registry.opendata.aws/)
- [Data.gov](https://www.data.gov/)

### Cómo añadir tu dataset:

1. Descarga el dataset de tu elección
2. Colócalo en la carpeta `data/raw/`
3. Actualiza el notebook para cargar tu dataset específico
4. Ejecuta el análisis

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **Pandas** - Manipulación de datos
- **NumPy** - Computación numérica
- **Scikit-learn** - Machine Learning
- **Matplotlib/Seaborn** - Visualización
- **Jupyter Notebook** - Análisis interactivo

## 📝 Entregables del TFM

### 1. Notebook de Análisis
- ✅ Archivo: `notebooks/analisis_tfm.ipynb`
- Contiene todo el análisis completo con código, visualizaciones y resultados

### 2. Informe (Máximo 20 páginas)
- 📄 Ubicación recomendada: `reports/informe_tfm.pdf`
- Debe incluir:
  - Introducción y objetivos
  - Descripción del dataset
  - Metodología
  - Resultados principales
  - Conclusiones
  - Referencias

### 3. Video Explicativo (5 minutos, formato MP4)
- 🎥 Ubicación recomendada: `reports/video_tfm.mp4` (no subir a Git)
- Estructura sugerida:
  - 0:00-0:30: Introducción y contexto
  - 0:30-1:30: Dataset y análisis descriptivo
  - 1:30-3:00: Modelos y metodología
  - 3:00-4:30: Resultados principales
  - 4:30-5:00: Conclusiones

### 4. Compartir en Kaggle (Opcional)
- Mejora tu marca personal
- Permite que otros aprendan de tu trabajo
- Genera visibilidad profesional

## 📖 Uso de Utilidades

El proyecto incluye módulos reutilizables en `src/`:

### Cargar Datos

```python
from src.data_utils import load_dataset, get_basic_info

# Cargar dataset
df = load_dataset('data/raw/your_dataset.csv')

# Obtener información básica
info = get_basic_info(df)
```

### Visualización

```python
from src.visualization import plot_distribution, plot_correlation_matrix

# Visualizar distribuciones
plot_distribution(df, save_path='results/visualizations/distributions.png')

# Matriz de correlación
plot_correlation_matrix(df, save_path='results/visualizations/correlation.png')
```

### Evaluación de Modelos

```python
from src.model_evaluation import evaluate_classification_model, plot_confusion_matrix

# Evaluar modelo
metrics = evaluate_classification_model(y_true, y_pred, model_name='Random Forest')

# Matriz de confusión
plot_confusion_matrix(y_true, y_pred, save_path='results/visualizations/confusion_matrix.png')
```

## 🤝 Contribuciones

Este es un proyecto académico personal. Si encuentras errores o tienes sugerencias, siéntete libre de abrir un issue.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**Diego Olalla**

- GitHub: [@diegoolalla](https://github.com/diegoolalla)

## 📚 Referencias

- Documentación de Scikit-learn: https://scikit-learn.org/
- Documentación de Pandas: https://pandas.pydata.org/
- Guías de Machine Learning: https://www.kaggle.com/learn

---

**Nota:** Este README proporciona una guía completa para el desarrollo del TFM. Asegúrate de personalizar el contenido según tu dataset y análisis específico.
