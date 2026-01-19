"""
Utilidades para visualización de datos
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from pathlib import Path


def setup_plot_style(style='whitegrid', context='notebook', palette='deep'):
    """
    Configura el estilo de las visualizaciones
    
    Parameters:
    -----------
    style : str
        Estilo de seaborn
    context : str
        Contexto de seaborn
    palette : str
        Paleta de colores
    """
    sns.set_style(style)
    sns.set_context(context)
    sns.set_palette(palette)
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 10


def plot_distribution(df, columns=None, bins=30, figsize=(15, 10), save_path=None):
    """
    Visualiza la distribución de variables numéricas
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset a visualizar
    columns : list, optional
        Columnas a visualizar
    bins : int
        Número de bins para histogramas
    figsize : tuple
        Tamaño de la figura
    save_path : str, optional
        Ruta para guardar la figura
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    n_cols = len(columns)
    n_rows = (n_cols + 2) // 3
    
    fig, axes = plt.subplots(n_rows, 3, figsize=figsize)
    axes = axes.flatten() if n_cols > 1 else [axes]
    
    for idx, col in enumerate(columns):
        if idx < len(axes):
            axes[idx].hist(df[col].dropna(), bins=bins, edgecolor='black', alpha=0.7)
            axes[idx].set_title(f'Distribución de {col}')
            axes[idx].set_xlabel(col)
            axes[idx].set_ylabel('Frecuencia')
            axes[idx].grid(alpha=0.3)
    
    # Ocultar ejes no utilizados
    for idx in range(n_cols, len(axes)):
        axes[idx].axis('off')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figura guardada en: {save_path}")
    
    plt.show()


def plot_correlation_matrix(df, figsize=(12, 10), annot=True, save_path=None):
    """
    Visualiza la matriz de correlación
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset a analizar
    figsize : tuple
        Tamaño de la figura
    annot : bool
        Si mostrar valores en el mapa de calor
    save_path : str, optional
        Ruta para guardar la figura
    """
    numeric_df = df.select_dtypes(include=[np.number])
    
    if numeric_df.empty:
        print("No hay columnas numéricas para calcular correlación")
        return
    
    plt.figure(figsize=figsize)
    correlation_matrix = numeric_df.corr()
    
    sns.heatmap(
        correlation_matrix,
        annot=annot,
        fmt='.2f',
        cmap='coolwarm',
        center=0,
        square=True,
        linewidths=1,
        cbar_kws={"shrink": 0.8}
    )
    
    plt.title('Matriz de Correlación')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figura guardada en: {save_path}")
    
    plt.show()
    
    return correlation_matrix


def plot_boxplots(df, columns=None, figsize=(15, 10), save_path=None):
    """
    Crea boxplots para variables numéricas
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset a visualizar
    columns : list, optional
        Columnas a visualizar
    figsize : tuple
        Tamaño de la figura
    save_path : str, optional
        Ruta para guardar la figura
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    n_cols = len(columns)
    n_rows = (n_cols + 2) // 3
    
    fig, axes = plt.subplots(n_rows, 3, figsize=figsize)
    axes = axes.flatten() if n_cols > 1 else [axes]
    
    for idx, col in enumerate(columns):
        if idx < len(axes):
            axes[idx].boxplot(df[col].dropna())
            axes[idx].set_title(f'Boxplot de {col}')
            axes[idx].set_ylabel(col)
            axes[idx].grid(alpha=0.3)
    
    # Ocultar ejes no utilizados
    for idx in range(n_cols, len(axes)):
        axes[idx].axis('off')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figura guardada en: {save_path}")
    
    plt.show()


def plot_target_distribution(df, target_column, figsize=(12, 5), save_path=None):
    """
    Visualiza la distribución de la variable objetivo
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset
    target_column : str
        Nombre de la columna objetivo
    figsize : tuple
        Tamaño de la figura
    save_path : str, optional
        Ruta para guardar la figura
    """
    if target_column not in df.columns:
        print(f"Columna '{target_column}' no encontrada")
        return
    
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    
    value_counts = df[target_column].value_counts()
    
    # Gráfico de barras
    axes[0].bar(range(len(value_counts)), value_counts.values)
    axes[0].set_xticks(range(len(value_counts)))
    axes[0].set_xticklabels(value_counts.index, rotation=45)
    axes[0].set_title(f'Distribución de {target_column}')
    axes[0].set_xlabel('Clase')
    axes[0].set_ylabel('Frecuencia')
    axes[0].grid(alpha=0.3)
    
    # Gráfico de pastel
    axes[1].pie(value_counts.values, labels=value_counts.index, autopct='%1.1f%%')
    axes[1].set_title(f'Proporción de {target_column}')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figura guardada en: {save_path}")
    
    plt.show()


def plot_feature_vs_target(df, feature_columns, target_column, figsize=(15, 10), save_path=None):
    """
    Visualiza la relación entre características y la variable objetivo
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset
    feature_columns : list
        Columnas de características
    target_column : str
        Columna objetivo
    figsize : tuple
        Tamaño de la figura
    save_path : str, optional
        Ruta para guardar la figura
    """
    n_features = len(feature_columns)
    n_rows = (n_features + 2) // 3
    
    fig, axes = plt.subplots(n_rows, 3, figsize=figsize)
    axes = axes.flatten() if n_features > 1 else [axes]
    
    for idx, feature in enumerate(feature_columns):
        if idx < len(axes):
            for target_val in df[target_column].unique():
                subset = df[df[target_column] == target_val]
                axes[idx].hist(subset[feature].dropna(), alpha=0.5, label=f'{target_column}={target_val}')
            
            axes[idx].set_title(f'{feature} vs {target_column}')
            axes[idx].set_xlabel(feature)
            axes[idx].set_ylabel('Frecuencia')
            axes[idx].legend()
            axes[idx].grid(alpha=0.3)
    
    # Ocultar ejes no utilizados
    for idx in range(n_features, len(axes)):
        axes[idx].axis('off')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figura guardada en: {save_path}")
    
    plt.show()


def save_figure(fig, path, dpi=300):
    """
    Guarda una figura en el path especificado
    
    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        Figura a guardar
    path : str
        Ruta donde guardar
    dpi : int
        Resolución
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches='tight')
    print(f"Figura guardada en: {path}")
