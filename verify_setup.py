#!/usr/bin/env python
"""
Script de verificación del entorno TFM
Ejecuta este script para verificar que todo está configurado correctamente
"""

import sys
import importlib

def check_module(module_name, display_name=None):
    """Verifica si un módulo está instalado"""
    if display_name is None:
        display_name = module_name
    
    try:
        importlib.import_module(module_name)
        print(f"✅ {display_name:<20} - Instalado")
        return True
    except ImportError:
        print(f"❌ {display_name:<20} - NO instalado")
        return False

def check_python_version():
    """Verifica la versión de Python"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Versión correcta")
        return True
    else:
        print(f"⚠️  Python {version.major}.{version.minor}.{version.micro} - Se recomienda Python 3.8+")
        return False

def main():
    print("=" * 60)
    print("VERIFICACIÓN DEL ENTORNO TFM")
    print("=" * 60)
    print()
    
    # Verificar versión de Python
    print("1. Versión de Python:")
    print("-" * 60)
    python_ok = check_python_version()
    print()
    
    # Módulos esenciales
    print("2. Librerías Esenciales:")
    print("-" * 60)
    essential_modules = [
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
        ('matplotlib', 'Matplotlib'),
        ('seaborn', 'Seaborn'),
        ('sklearn', 'Scikit-learn'),
        ('scipy', 'SciPy'),
    ]
    
    essential_ok = all(check_module(mod, name) for mod, name in essential_modules)
    print()
    
    # Módulos adicionales
    print("3. Librerías Adicionales:")
    print("-" * 60)
    additional_modules = [
        ('jupyter', 'Jupyter'),
        ('joblib', 'Joblib'),
        ('tqdm', 'tqdm'),
        ('shap', 'SHAP'),
    ]
    
    additional_ok = all(check_module(mod, name) for mod, name in additional_modules)
    print()
    
    # Verificar módulos locales
    print("4. Módulos del Proyecto:")
    print("-" * 60)
    try:
        from src import data_utils, visualization, model_evaluation
        print("✅ src.data_utils      - Disponible")
        print("✅ src.visualization   - Disponible")
        print("✅ src.model_evaluation - Disponible")
        local_ok = True
    except ImportError as e:
        print(f"❌ Error importando módulos locales: {e}")
        local_ok = False
    print()
    
    # Verificar estructura de directorios
    print("5. Estructura de Directorios:")
    print("-" * 60)
    import os
    required_dirs = [
        'notebooks',
        'data',
        'src',
        'models',
        'results',
        'docs',
    ]
    
    dirs_ok = True
    for dir_name in required_dirs:
        if os.path.isdir(dir_name):
            print(f"✅ {dir_name:<20} - Existe")
        else:
            print(f"❌ {dir_name:<20} - NO existe")
            dirs_ok = False
    print()
    
    # Resultado final
    print("=" * 60)
    print("RESUMEN")
    print("=" * 60)
    
    all_ok = python_ok and essential_ok and additional_ok and local_ok and dirs_ok
    
    if all_ok:
        print("✅ Todo está configurado correctamente!")
        print("   Puedes comenzar a trabajar con el proyecto.")
        print()
        print("Próximos pasos:")
        print("  1. Obtén un dataset público")
        print("  2. Colócalo en data/raw/")
        print("  3. Abre notebooks/analisis_tfm.ipynb")
        print("  4. ¡Comienza tu análisis!")
        return 0
    else:
        print("⚠️  Hay algunos problemas con la configuración.")
        print("   Por favor, revisa los errores arriba.")
        print()
        if not essential_ok or not additional_ok:
            print("Para instalar las librerías faltantes:")
            print("  pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
