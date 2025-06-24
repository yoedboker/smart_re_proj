# Import necessary libraries
import pandas as pd
from src.advisor.data_processing import clean_data, feature_engineering
from src.advisor.model import train_model, save_model
from src.advisor.config import Config

def main():
    # Load raw data
    raw_data_path = Config.RAW_DATA_PATH
    data = pd.read_csv(raw_data_path)

    # Clean and process data
    cleaned_data = clean_data(data)
    featured_data = feature_engineering(cleaned_data)

    # Train the model
    model = train_model(featured_data)

    # Save the trained model
    model_path = Config.MODEL_PATH
    save_model(model, model_path)

if __name__ == "__main__":
    main()