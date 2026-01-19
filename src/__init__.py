"""
TFM - Paquete de utilidades para análisis de datos y modelización
"""

from .data_utils import (
    load_dataset,
    get_basic_info,
    detect_column_types,
    remove_duplicates,
    handle_missing_values,
    detect_outliers_iqr,
    save_processed_data
)

from .visualization import (
    setup_plot_style,
    plot_distribution,
    plot_correlation_matrix,
    plot_boxplots,
    plot_target_distribution,
    plot_feature_vs_target,
    save_figure
)

from .model_evaluation import (
    evaluate_classification_model,
    evaluate_regression_model,
    plot_confusion_matrix,
    compare_models,
    plot_roc_curves,
    plot_feature_importance,
    plot_learning_curve,
    save_evaluation_report,
    print_classification_summary
)

__all__ = [
    # Data utilities
    'load_dataset',
    'get_basic_info',
    'detect_column_types',
    'remove_duplicates',
    'handle_missing_values',
    'detect_outliers_iqr',
    'save_processed_data',
    # Visualization
    'setup_plot_style',
    'plot_distribution',
    'plot_correlation_matrix',
    'plot_boxplots',
    'plot_target_distribution',
    'plot_feature_vs_target',
    'save_figure',
    # Model evaluation
    'evaluate_classification_model',
    'evaluate_regression_model',
    'plot_confusion_matrix',
    'compare_models',
    'plot_roc_curves',
    'plot_feature_importance',
    'plot_learning_curve',
    'save_evaluation_report',
    'print_classification_summary',
]

__version__ = '0.1.0'
