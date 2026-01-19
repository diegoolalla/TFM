"""
Utilidades para carga y preprocesamiento de datos
"""

import pandas as pd
import numpy as np
from pathlib import Path


def load_dataset(file_path, **kwargs):
    """
    Carga un dataset desde diferentes formatos
    
    Parameters:
    -----------
    file_path : str
        Ruta al archivo de datos
    **kwargs : dict
        Argumentos adicionales para pandas read functions
    
    Returns:
    --------
    pd.DataFrame
        Dataset cargado
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"El archivo {file_path} no existe")
    
    # Determinar el tipo de archivo y cargarlo
    if file_path.suffix == '.csv':
        return pd.read_csv(file_path, **kwargs)
    elif file_path.suffix in ['.xlsx', '.xls']:
        return pd.read_excel(file_path, **kwargs)
    elif file_path.suffix == '.json':
        return pd.read_json(file_path, **kwargs)
    elif file_path.suffix == '.parquet':
        return pd.read_parquet(file_path, **kwargs)
    elif file_path.suffix == '.feather':
        return pd.read_feather(file_path, **kwargs)
    else:
        raise ValueError(f"Formato de archivo no soportado: {file_path.suffix}")


def get_basic_info(df):
    """
    Obtiene información básica del dataset
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset a analizar
    
    Returns:
    --------
    dict
        Diccionario con información del dataset
    """
    info = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'missing_percentage': (df.isnull().sum() / len(df) * 100).to_dict(),
        'duplicates': df.duplicated().sum(),
        'memory_usage_mb': df.memory_usage(deep=True).sum() / 1024**2
    }
    return info


def detect_column_types(df):
    """
    Detecta automáticamente los tipos de columnas
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset a analizar
    
    Returns:
    --------
    dict
        Diccionario con tipos de columnas categorizados
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    datetime_cols = df.select_dtypes(include=['datetime64']).columns.tolist()
    boolean_cols = df.select_dtypes(include=['bool']).columns.tolist()
    
    return {
        'numeric': numeric_cols,
        'categorical': categorical_cols,
        'datetime': datetime_cols,
        'boolean': boolean_cols
    }


def remove_duplicates(df, subset=None, keep='first'):
    """
    Elimina filas duplicadas del dataset
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset original
    subset : list, optional
        Columnas a considerar para detectar duplicados
    keep : str
        Qué duplicado mantener ('first', 'last', False)
    
    Returns:
    --------
    pd.DataFrame
        Dataset sin duplicados
    """
    n_duplicates = df.duplicated(subset=subset).sum()
    df_clean = df.drop_duplicates(subset=subset, keep=keep)
    print(f"Eliminadas {n_duplicates} filas duplicadas")
    return df_clean


def handle_missing_values(df, strategy='mean', threshold=0.5):
    """
    Maneja valores faltantes en el dataset
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset con valores faltantes
    strategy : str
        Estrategia de imputación ('mean', 'median', 'mode', 'drop')
    threshold : float
        Porcentaje máximo de valores faltantes para mantener la columna
    
    Returns:
    --------
    pd.DataFrame
        Dataset con valores faltantes manejados
    """
    df_clean = df.copy()
    
    # Eliminar columnas con demasiados valores faltantes
    missing_pct = df_clean.isnull().sum() / len(df_clean)
    cols_to_drop = missing_pct[missing_pct > threshold].index.tolist()
    
    if cols_to_drop:
        print(f"Eliminando columnas con más de {threshold*100}% valores faltantes: {cols_to_drop}")
        df_clean = df_clean.drop(columns=cols_to_drop)
    
    # Imputar valores faltantes según estrategia
    if strategy == 'drop':
        df_clean = df_clean.dropna()
        print(f"Eliminadas filas con valores faltantes. Nuevo tamaño: {df_clean.shape}")
    else:
        numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            if df_clean[col].isnull().any():
                if strategy == 'mean':
                    fill_value = df_clean[col].mean()
                elif strategy == 'median':
                    fill_value = df_clean[col].median()
                elif strategy == 'mode':
                    mode_values = df_clean[col].mode()
                    if len(mode_values) > 0:
                        fill_value = mode_values[0]
                    else:
                        # If no mode, fallback to median
                        fill_value = df_clean[col].median()
                else:
                    continue
                
                df_clean[col].fillna(fill_value, inplace=True)
                print(f"Columna '{col}' imputada con {strategy}: {fill_value:.2f}")
    
    return df_clean


def detect_outliers_iqr(df, columns=None, multiplier=1.5):
    """
    Detecta outliers usando el método IQR
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset a analizar
    columns : list, optional
        Columnas a analizar (por defecto todas las numéricas)
    multiplier : float
        Multiplicador para el rango IQR
    
    Returns:
    --------
    dict
        Diccionario con información de outliers por columna
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    outliers_info = {}
    
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - multiplier * IQR
        upper_bound = Q3 + multiplier * IQR
        
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        
        outliers_info[col] = {
            'count': len(outliers),
            'percentage': (len(outliers) / len(df)) * 100,
            'lower_bound': lower_bound,
            'upper_bound': upper_bound,
            'indices': outliers.index.tolist()
        }
    
    return outliers_info


def save_processed_data(df, file_path, format='csv'):
    """
    Guarda el dataset procesado
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset a guardar
    file_path : str
        Ruta donde guardar el archivo
    format : str
        Formato del archivo ('csv', 'parquet', 'feather')
    """
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    if format == 'csv':
        df.to_csv(file_path, index=False)
    elif format == 'parquet':
        df.to_parquet(file_path, index=False)
    elif format == 'feather':
        df.to_feather(file_path)
    else:
        raise ValueError(f"Formato no soportado: {format}")
    
    print(f"Dataset guardado en: {file_path}")
