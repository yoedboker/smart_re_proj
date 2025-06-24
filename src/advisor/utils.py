# Utility functions for the real estate advisor project

import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

def load_data(file_path):
    """Load data from a CSV file."""
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

def save_data(data, file_path):
    """Save DataFrame to a CSV file."""
    data.to_csv(file_path, index=False)

def calculate_metrics(y_true, y_pred):
    """Calculate and return regression metrics."""
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return {'MSE': mse, 'R2': r2}

def preprocess_data(df):
    """Preprocess the DataFrame (placeholder for actual preprocessing steps)."""
    # Example preprocessing steps
    df = df.dropna()  # Drop missing values
    # Add more preprocessing as needed
    return df

def feature_engineering(df):
    """Create new features from the DataFrame (placeholder for actual feature engineering)."""
    # Example feature engineering steps
    df['new_feature'] = df['existing_feature'] * 2  # Example transformation
    # Add more feature engineering as needed
    return df