#!/usr/bin/env python
"""
Script de ejemplo que demuestra el uso de las utilidades del proyecto TFM
Usa el dataset Iris como ejemplo
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

# Configurar para que funcione desde cualquier directorio
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Importar utilidades del proyecto
from src.data_utils import get_basic_info, detect_column_types
from src.visualization import (
    setup_plot_style, 
    plot_distribution, 
    plot_correlation_matrix,
    plot_target_distribution
)
from src.model_evaluation import (
    evaluate_classification_model,
    compare_models,
    plot_confusion_matrix
)

def main():
    print("=" * 70)
    print("EJEMPLO DE USO DE UTILIDADES TFM")
    print("Dataset: Iris (ejemplo)")
    print("=" * 70)
    print()
    
    # 1. Cargar datos de ejemplo
    print("1. Cargando dataset Iris...")
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df['target_name'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    print(f"   ✅ Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")
    print()
    
    # 2. Análisis básico con utilidades
    print("2. Análisis básico del dataset:")
    print("-" * 70)
    info = get_basic_info(df)
    print(f"   - Forma: {info['shape']}")
    print(f"   - Valores nulos: {sum(info['missing_values'].values())}")
    print(f"   - Duplicados: {info['duplicates']}")
    print(f"   - Memoria: {info['memory_usage_mb']:.2f} MB")
    print()
    
    # 3. Detectar tipos de columnas
    print("3. Tipos de columnas detectados:")
    print("-" * 70)
    column_types = detect_column_types(df)
    print(f"   - Numéricas: {len(column_types['numeric'])} columnas")
    print(f"     {column_types['numeric'][:3]}...")
    print(f"   - Categóricas: {len(column_types['categorical'])} columnas")
    if column_types['categorical']:
        print(f"     {column_types['categorical']}")
    print()
    
    # 4. Configurar estilo de visualización
    print("4. Configurando estilo de visualización...")
    setup_plot_style()
    print("   ✅ Estilo configurado")
    print()
    
    # 5. Crear visualizaciones
    print("5. Generando visualizaciones...")
    os.makedirs('results/visualizations', exist_ok=True)
    
    # Distribuciones
    numeric_cols = [col for col in df.columns if col not in ['target', 'target_name']]
    plot_distribution(
        df[numeric_cols], 
        columns=numeric_cols[:2],  # Solo las primeras 2 para el ejemplo
        figsize=(10, 4),
        save_path='results/visualizations/example_distributions.png'
    )
    print("   ✅ Distribuciones guardadas")
    
    # Correlación
    plot_correlation_matrix(
        df[numeric_cols],
        figsize=(8, 6),
        save_path='results/visualizations/example_correlation.png'
    )
    print("   ✅ Matriz de correlación guardada")
    
    # Distribución del target
    plot_target_distribution(
        df,
        'target',
        figsize=(10, 4),
        save_path='results/visualizations/example_target.png'
    )
    print("   ✅ Distribución del target guardada")
    print()
    
    # 6. Preparar datos para modelización
    print("6. Preparando datos para modelización...")
    X = df[numeric_cols]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"   ✅ Train: {X_train.shape}, Test: {X_test.shape}")
    print()
    
    # 7. Entrenar múltiples modelos
    print("7. Entrenando modelos...")
    print("-" * 70)
    
    models = {
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=200),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100)
    }
    
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        metrics = evaluate_classification_model(y_test, y_pred, model_name=name)
        results[name] = metrics
        print(f"   {name}:")
        print(f"      Accuracy:  {metrics['accuracy']:.4f}")
        print(f"      Precision: {metrics['precision']:.4f}")
        print(f"      Recall:    {metrics['recall']:.4f}")
        print(f"      F1-Score:  {metrics['f1_score']:.4f}")
    print()
    
    # 8. Comparar modelos
    print("8. Comparando modelos visualmente...")
    compare_models(
        results,
        metric='accuracy',
        figsize=(10, 5),
        save_path='results/visualizations/example_model_comparison.png'
    )
    print("   ✅ Comparación guardada")
    print()
    
    # 9. Matriz de confusión del mejor modelo
    print("9. Generando matriz de confusión del mejor modelo...")
    best_model_name = max(results, key=lambda x: results[x]['accuracy'])
    best_model = models[best_model_name]
    y_pred_best = best_model.predict(X_test)
    
    plot_confusion_matrix(
        y_test,
        y_pred_best,
        labels=['setosa', 'versicolor', 'virginica'],
        figsize=(8, 6),
        save_path='results/visualizations/example_confusion_matrix.png'
    )
    print(f"   ✅ Matriz de confusión guardada ({best_model_name})")
    print()
    
    # 10. Guardar resultados
    print("10. Guardando resultados...")
    os.makedirs('results/metrics', exist_ok=True)
    results_df = pd.DataFrame(results).T
    results_df.to_csv('results/metrics/example_model_results.csv')
    print("   ✅ Resultados guardados en results/metrics/example_model_results.csv")
    print()
    
    # Resumen final
    print("=" * 70)
    print("✅ EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print()
    print("Archivos generados:")
    print("  - results/visualizations/example_distributions.png")
    print("  - results/visualizations/example_correlation.png")
    print("  - results/visualizations/example_target.png")
    print("  - results/visualizations/example_model_comparison.png")
    print("  - results/visualizations/example_confusion_matrix.png")
    print("  - results/metrics/example_model_results.csv")
    print()
    print(f"Mejor modelo: {best_model_name}")
    print(f"Accuracy: {results[best_model_name]['accuracy']:.4f}")
    print()
    print("Las utilidades están funcionando correctamente!")
    print("Ahora puedes usarlas en tu notebook para tu propio análisis.")
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except Exception as e:
        print(f"\n❌ Error durante la ejecución: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
