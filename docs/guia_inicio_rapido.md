# Guía de Inicio Rápido - TFM

Esta guía te ayudará a comenzar con tu TFM en pocos minutos.

## 📋 Pre-requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git
- Jupyter Notebook o JupyterLab

## 🚀 Configuración Inicial

### 1. Clonar el Repositorio

```bash
git clone https://github.com/diegoolalla/TFM.git
cd TFM
```

### 2. Crear Entorno Virtual

**Opción A: Con venv (recomendado)**
```bash
# Crear entorno virtual
python -m venv venv

# Activar en Linux/Mac
source venv/bin/activate

# Activar en Windows
venv\Scripts\activate
```

**Opción B: Con conda**
```bash
conda create -n tfm python=3.8
conda activate tfm
```

### 3. Instalar Dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verificar Instalación

```bash
python -c "import pandas, numpy, sklearn, matplotlib; print('✅ Todas las librerías instaladas correctamente!')"
```

---

## 📊 Trabajar con tu Dataset

### Paso 1: Obtener un Dataset

Elige un dataset público de:
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)
- [Google Dataset Search](https://datasetsearch.research.google.com/)

### Paso 2: Colocar el Dataset

```bash
# Crear subdirectorio para datos crudos
mkdir -p data/raw

# Copiar tu dataset
cp /ruta/a/tu/dataset.csv data/raw/
```

### Paso 3: Documentar el Dataset

Crea un archivo `data/DATASET.md` con información:

```markdown
# Nombre del Dataset

- **Fuente**: [URL]
- **Fecha de descarga**: [Fecha]
- **Licencia**: [Tipo de licencia]
- **Descripción**: [Breve descripción]

## Características
- Número de instancias: [N]
- Número de características: [M]
- Variable objetivo: [nombre]

## Columnas
- columna1: [descripción]
- columna2: [descripción]
...
```

---

## 💻 Trabajar con el Notebook

### Opción 1: Jupyter Notebook

```bash
jupyter notebook notebooks/analisis_tfm.ipynb
```

### Opción 2: JupyterLab (recomendado)

```bash
jupyter lab notebooks/analisis_tfm.ipynb
```

### Opción 3: VS Code

1. Instala la extensión de Python
2. Instala la extensión de Jupyter
3. Abre el archivo `.ipynb`

### Opción 4: Google Colab

1. Sube el notebook a Google Drive
2. Abre con Google Colab
3. Sube tu dataset o conéctalo desde Drive

---

## 📝 Flujo de Trabajo Recomendado

### Fase 1: Exploración (Semana 1-2)

1. **Familiarízate con el dataset**
   - Ejecuta las primeras secciones del notebook
   - Explora las distribuciones
   - Identifica problemas de calidad de datos

2. **Análisis descriptivo**
   - Genera estadísticas descriptivas
   - Crea visualizaciones
   - Identifica patrones y correlaciones

### Fase 2: Preprocesamiento (Semana 2-3)

1. **Limpieza de datos**
   - Maneja valores nulos
   - Identifica y trata outliers
   - Elimina duplicados

2. **Transformaciones**
   - Codifica variables categóricas
   - Normaliza/estandariza variables numéricas
   - Crea nuevas características si es necesario

### Fase 3: Modelización (Semana 3-4)

1. **Implementa múltiples modelos**
   - Comienza con modelos simples (baseline)
   - Avanza a modelos más complejos
   - Prueba al menos 5-7 modelos diferentes

2. **Validación**
   - Usa validación cruzada
   - Compara métricas
   - Selecciona el mejor modelo

### Fase 4: Optimización (Semana 4-5)

1. **Ajusta hiperparámetros**
   - Grid Search o Random Search
   - Optimiza el mejor modelo
   - Valida resultados

2. **Análisis de errores**
   - Estudia predicciones incorrectas
   - Identifica patrones de error
   - Propón mejoras

### Fase 5: Documentación (Semana 5-6)

1. **Informe escrito**
   - Usa la plantilla en `docs/plantilla_informe.md`
   - Máximo 20 páginas
   - Incluye visualizaciones clave

2. **Video explicativo**
   - Usa la guía en `docs/guion_video.md`
   - 5 minutos exactos
   - Formato MP4

3. **Publicación (opcional)**
   - Sigue la guía en `docs/guia_kaggle.md`
   - Comparte en Kaggle
   - Promociona en LinkedIn/Twitter

---

## 🛠️ Uso de Utilidades

### Cargar y Explorar Datos

```python
from src.data_utils import load_dataset, get_basic_info

# Cargar dataset
df = load_dataset('data/raw/mi_dataset.csv')

# Información básica
info = get_basic_info(df)
print(f"Shape: {info['shape']}")
print(f"Missing values: {info['missing_values']}")
```

### Visualizaciones

```python
from src.visualization import plot_distribution, plot_correlation_matrix

# Distribuciones
plot_distribution(df, save_path='results/visualizations/dist.png')

# Correlaciones
plot_correlation_matrix(df, save_path='results/visualizations/corr.png')
```

### Evaluación de Modelos

```python
from src.model_evaluation import evaluate_classification_model, compare_models

# Evaluar modelo
metrics = evaluate_classification_model(y_test, y_pred, model_name='Random Forest')
print(f"Accuracy: {metrics['accuracy']:.4f}")

# Comparar múltiples modelos
results = {...}  # Diccionario con resultados
compare_models(results, metric='accuracy', save_path='results/visualizations/comparison.png')
```

---

## 📁 Estructura de Archivos Durante el Desarrollo

```
TFM/
├── notebooks/
│   └── analisis_tfm.ipynb          # Tu notebook principal (modificar)
├── data/
│   ├── raw/
│   │   └── mi_dataset.csv          # Tu dataset (añadir)
│   ├── processed/
│   │   └── clean_data.csv          # Datos procesados (generar)
│   └── DATASET.md                  # Documentación (crear)
├── models/
│   ├── random_forest.pkl           # Modelo guardado (generar)
│   └── model_config.json           # Configuración (generar)
├── results/
│   ├── visualizations/
│   │   ├── eda_*.png               # Gráficos EDA (generar)
│   │   ├── model_*.png             # Gráficos modelos (generar)
│   │   └── ...
│   └── metrics/
│       ├── model_comparison.csv    # Comparación (generar)
│       └── best_model_metrics.json # Métricas finales (generar)
├── reports/
│   ├── informe_tfm.pdf             # Informe final (crear)
│   └── presentacion.pptx           # Diapositivas (crear)
└── docs/
    └── notas.md                    # Tus notas (opcional)
```

---

## ⚠️ Problemas Comunes

### Problema: "Module not found"

**Solución:**
```bash
# Asegúrate de estar en el entorno virtual
# Reinstala las dependencias
pip install -r requirements.txt
```

### Problema: "FileNotFoundError" al cargar datos

**Solución:**
```python
# Verifica la ruta relativa correcta
# Desde el notebook:
df = pd.read_csv('../data/raw/mi_dataset.csv')

# O usa ruta absoluta
import os
data_path = os.path.join(os.getcwd(), '..', 'data', 'raw', 'mi_dataset.csv')
df = pd.read_csv(data_path)
```

### Problema: Jupyter no encuentra las utilidades

**Solución:**
```python
# Añade el directorio padre al path
import sys
sys.path.append('..')

# Ahora importa
from src.data_utils import load_dataset
```

### Problema: Memoria insuficiente

**Solución:**
```python
# Trabaja con una muestra del dataset
df_sample = df.sample(frac=0.1, random_state=42)

# O carga solo columnas necesarias
df = pd.read_csv('data.csv', usecols=['col1', 'col2', 'target'])

# O usa chunks
for chunk in pd.read_csv('data.csv', chunksize=10000):
    # Procesa cada chunk
    pass
```

---

## 📚 Recursos Adicionales

### Tutoriales
- [Scikit-learn Documentation](https://scikit-learn.org/stable/tutorial/index.html)
- [Pandas Tutorials](https://pandas.pydata.org/docs/getting_started/tutorials.html)
- [Kaggle Learn](https://www.kaggle.com/learn)

### Ejemplos de TFM
- Busca "master thesis machine learning" en GitHub
- Explora notebooks en Kaggle con tag "thesis"

### Comunidades
- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/machine-learning)
- [Kaggle Discussion](https://www.kaggle.com/discussion)

---

## ✅ Checklist de Progreso

### Semana 1-2: Exploración
- [ ] Dataset seleccionado y descargado
- [ ] Entorno configurado
- [ ] Análisis descriptivo completado
- [ ] Primeras visualizaciones creadas

### Semana 2-3: Preprocesamiento
- [ ] Valores nulos manejados
- [ ] Outliers analizados
- [ ] Variables transformadas
- [ ] Datos divididos en train/test

### Semana 3-4: Modelización
- [ ] Baseline model implementado
- [ ] 5+ modelos entrenados
- [ ] Validación cruzada aplicada
- [ ] Mejor modelo identificado

### Semana 4-5: Optimización
- [ ] Hiperparámetros optimizados
- [ ] Análisis de errores realizado
- [ ] Características importantes identificadas
- [ ] Resultados finales validados

### Semana 5-6: Documentación
- [ ] Notebook limpio y documentado
- [ ] Informe escrito (≤20 páginas)
- [ ] Video grabado (5 minutos)
- [ ] Código en GitHub
- [ ] (Opcional) Publicado en Kaggle

---

## 🎯 Consejos Finales

1. **Empieza simple**: No intentes hacer todo perfecto desde el inicio
2. **Itera**: El análisis de datos es iterativo, no lineal
3. **Documenta mientras trabajas**: No dejes la documentación para el final
4. **Pide feedback**: Muestra tu trabajo a compañeros o mentores
5. **Gestiona el tiempo**: Usa la planificación semanal sugerida
6. **Haz commits frecuentes**: Usa Git para versionar tu trabajo
7. **Backup**: Mantén copias de seguridad de tu trabajo

---

**¡Mucho éxito con tu TFM!** 🎓🚀

Para preguntas o problemas, consulta la documentación en la carpeta `docs/` o abre un issue en GitHub.
