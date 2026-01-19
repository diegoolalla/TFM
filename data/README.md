# Data Directory

This directory contains the datasets used in the TFM project.

## Structure

- `raw/` - Original, immutable data dumps
- `processed/` - Cleaned and transformed data ready for analysis
- `external/` - Data from third-party sources

## Important Notes

⚠️ **Large data files are not committed to the repository** (see `.gitignore`)

### How to use

1. Download your public dataset and place it in the `raw/` subdirectory
2. Run the data preprocessing notebooks to generate processed data
3. Processed data will be saved in the `processed/` subdirectory

### Recommended Public Datasets

You can find public datasets on:
- [Kaggle](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [AWS Open Data](https://registry.opendata.aws/)
- [Data.gov](https://www.data.gov/)

### Dataset Documentation

When adding a dataset, create a `DATASET.md` file with:
- Dataset name and source
- Description
- Number of instances and features
- Target variable (if applicable)
- License information
- Download instructions
