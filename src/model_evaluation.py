"""
Utilidades para evaluación de modelos de Machine Learning
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_curve, auc,
    mean_squared_error, mean_absolute_error, r2_score
)
from sklearn.model_selection import cross_val_score, learning_curve
from pathlib import Path


def evaluate_classification_model(y_true, y_pred, model_name='Model', average='weighted'):
    """
    Evalúa un modelo de clasificación y retorna métricas
    
    Parameters:
    -----------
    y_true : array-like
        Valores reales
    y_pred : array-like
        Predicciones del modelo
    model_name : str
        Nombre del modelo
    average : str
        Estrategia de promediado para métricas
    
    Returns:
    --------
    dict
        Diccionario con métricas de evaluación
    """
    metrics = {
        'model': model_name,
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average=average, zero_division=0),
        'recall': recall_score(y_true, y_pred, average=average, zero_division=0),
        'f1_score': f1_score(y_true, y_pred, average=average, zero_division=0)
    }
    
    return metrics


def evaluate_regression_model(y_true, y_pred, model_name='Model'):
    """
    Evalúa un modelo de regresión y retorna métricas
    
    Parameters:
    -----------
    y_true : array-like
        Valores reales
    y_pred : array-like
        Predicciones del modelo
    model_name : str
        Nombre del modelo
    
    Returns:
    --------
    dict
        Diccionario con métricas de evaluación
    """
    metrics = {
        'model': model_name,
        'mse': mean_squared_error(y_true, y_pred),
        'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
        'mae': mean_absolute_error(y_true, y_pred),
        'r2': r2_score(y_true, y_pred)
    }
    
    return metrics


def plot_confusion_matrix(y_true, y_pred, labels=None, normalize=False, 
                         figsize=(8, 6), save_path=None):
    """
    Visualiza la matriz de confusión
    
    Parameters:
    -----------
    y_true : array-like
        Valores reales
    y_pred : array-like
        Predicciones
    labels : list, optional
        Etiquetas de las clases
    normalize : bool
        Si normalizar la matriz
    figsize : tuple
        Tamaño de la figura
    save_path : str, optional
        Ruta para guardar la figura
    """
    cm = confusion_matrix(y_true, y_pred)
    
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    plt.figure(figsize=figsize)
    sns.heatmap(cm, annot=True, fmt='.2f' if normalize else 'd', 
                cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.title('Matriz de Confusión' + (' (Normalizada)' if normalize else ''))
    plt.ylabel('Valor Real')
    plt.xlabel('Predicción')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figura guardada en: {save_path}")
    
    plt.show()


def compare_models(results_dict, metric='accuracy', figsize=(12, 6), save_path=None):
    """
    Compara múltiples modelos visualmente
    
    Parameters:
    -----------
    results_dict : dict
        Diccionario con resultados de modelos
    metric : str
        Métrica a visualizar
    figsize : tuple
        Tamaño de la figura
    save_path : str, optional
        Ruta para guardar la figura
    """
    models = list(results_dict.keys())
    values = [results_dict[m].get(metric, 0) for m in models]
    
    plt.figure(figsize=figsize)
    bars = plt.bar(models, values, alpha=0.7, edgecolor='black')
    
    # Colorear la mejor barra
    best_idx = np.argmax(values)
    bars[best_idx].set_color('green')
    
    plt.xlabel('Modelo')
    plt.ylabel(metric.replace('_', ' ').title())
    plt.title(f'Comparación de Modelos - {metric.replace("_", " ").title()}')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figura guardada en: {save_path}")
    
    plt.show()


def plot_roc_curves(models_dict, X_test, y_test, figsize=(10, 8), save_path=None):
    """
    Visualiza curvas ROC para múltiples modelos (clasificación binaria)
    
    Parameters:
    -----------
    models_dict : dict
        Diccionario {nombre: modelo}
    X_test : array-like
        Datos de prueba
    y_test : array-like
        Etiquetas de prueba
    figsize : tuple
        Tamaño de la figura
    save_path : str, optional
        Ruta para guardar la figura
    """
    plt.figure(figsize=figsize)
    
    for name, model in models_dict.items():
        if hasattr(model, 'predict_proba'):
            y_score = model.predict_proba(X_test)[:, 1]
            fpr, tpr, _ = roc_curve(y_test, y_score)
            roc_auc = auc(fpr, tpr)
            plt.plot(fpr, tpr, label=f'{name} (AUC = {roc_auc:.3f})')
    
    plt.plot([0, 1], [0, 1], 'k--', label='Random')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Curvas ROC - Comparación de Modelos')
    plt.legend(loc='lower right')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figura guardada en: {save_path}")
    
    plt.show()


def plot_feature_importance(model, feature_names, top_n=15, figsize=(10, 6), save_path=None):
    """
    Visualiza la importancia de características
    
    Parameters:
    -----------
    model : sklearn model
        Modelo entrenado con feature_importances_
    feature_names : list
        Nombres de las características
    top_n : int
        Número de características a mostrar
    figsize : tuple
        Tamaño de la figura
    save_path : str, optional
        Ruta para guardar la figura
    """
    if not hasattr(model, 'feature_importances_'):
        print("El modelo no tiene atributo feature_importances_")
        return
    
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1][:top_n]
    
    plt.figure(figsize=figsize)
    plt.barh(range(top_n), importances[indices], alpha=0.7)
    plt.yticks(range(top_n), [feature_names[i] for i in indices])
    plt.xlabel('Importancia')
    plt.title(f'Top {top_n} Características Más Importantes')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figura guardada en: {save_path}")
    
    plt.show()


def plot_learning_curve(estimator, X, y, cv=5, figsize=(10, 6), save_path=None):
    """
    Visualiza la curva de aprendizaje del modelo
    
    Parameters:
    -----------
    estimator : sklearn estimator
        Modelo a evaluar
    X : array-like
        Datos de entrenamiento
    y : array-like
        Etiquetas
    cv : int
        Número de folds para validación cruzada
    figsize : tuple
        Tamaño de la figura
    save_path : str, optional
        Ruta para guardar la figura
    """
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=-1,
        train_sizes=np.linspace(0.1, 1.0, 10),
        scoring='accuracy'
    )
    
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    
    plt.figure(figsize=figsize)
    plt.plot(train_sizes, train_mean, label='Entrenamiento', marker='o')
    plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.2)
    plt.plot(train_sizes, test_mean, label='Validación', marker='s')
    plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.2)
    
    plt.xlabel('Tamaño del conjunto de entrenamiento')
    plt.ylabel('Accuracy')
    plt.title('Curva de Aprendizaje')
    plt.legend(loc='best')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figura guardada en: {save_path}")
    
    plt.show()


def save_evaluation_report(metrics_df, file_path):
    """
    Guarda el reporte de evaluación en CSV
    
    Parameters:
    -----------
    metrics_df : pd.DataFrame
        DataFrame con métricas de evaluación
    file_path : str
        Ruta del archivo
    """
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_df.to_csv(file_path, index=False)
    print(f"Reporte guardado en: {file_path}")


def print_classification_summary(y_true, y_pred, model_name='Model'):
    """
    Imprime un resumen completo de clasificación
    
    Parameters:
    -----------
    y_true : array-like
        Valores reales
    y_pred : array-like
        Predicciones
    model_name : str
        Nombre del modelo
    """
    print("=" * 60)
    print(f"REPORTE DE CLASIFICACIÓN - {model_name}")
    print("=" * 60)
    print(classification_report(y_true, y_pred))
    print("\nMatriz de Confusión:")
    print(confusion_matrix(y_true, y_pred))
