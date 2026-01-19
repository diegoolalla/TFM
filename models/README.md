# Models Directory

This directory contains trained machine learning models.

## Structure

Models are saved here after training and can be loaded for evaluation or prediction.

## File Naming Convention

Use descriptive names for your models:
```
{model_type}_{dataset}_{date}_{metric}.{extension}

Example: random_forest_iris_20260119_acc92.pkl
```

## Supported Formats

- `.pkl` - Scikit-learn models (pickle)
- `.joblib` - Scikit-learn models (joblib, recommended for large arrays)
- `.h5` / `.keras` - Keras/TensorFlow models
- `.pt` / `.pth` - PyTorch models
- `.json` - Model configurations

## Important Notes

⚠️ **Model files are not committed to the repository** due to their size (see `.gitignore`)

To share models:
- Use model versioning tools (MLflow, DVC)
- Upload to cloud storage
- Share via Kaggle or Google Drive
- Include model loading code in notebooks
