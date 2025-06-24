import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """Clean the dataset by handling missing values and duplicates."""
    data = data.drop_duplicates()
    data = data.fillna(method='ffill')  # Forward fill for missing values
    return data

def feature_engineering(data):
    """Perform feature engineering on the dataset."""
    # Example: Create new features or modify existing ones
    data['price_per_sqft'] = data['price'] / data['sqft']
    return data

def preprocess_data(file_path):
    """Load, clean, and perform feature engineering on the data."""
    data = load_data(file_path)
    data = clean_data(data)
    data = feature_engineering(data)
    return data

def split_data(data, target_column):
    """Split the data into training and testing sets."""
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def scale_features(X_train, X_test):
    """Scale features using StandardScaler."""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler