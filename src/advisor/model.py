import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os

class PricePredictor:
    def __init__(self, config):
        self.config = config
        self.model = None

    def load_data(self):
        data_path = os.path.join(self.config['data_dir'], 'processed', 'featured_data.csv')
        data = pd.read_csv(data_path)
        X = data.drop('price', axis=1)
        y = data['price']
        return X, y

    def train(self):
        X, y = self.load_data()
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = xgb.XGBRegressor(**self.config['model_params'])
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_val)
        mse = mean_squared_error(y_val, y_pred)
        print(f'Model trained with MSE: {mse}')

    def save_model(self):
        model_path = os.path.join(self.config['model_dir'], 'price_predictor.pkl')
        joblib.dump(self.model, model_path)
        print(f'Model saved to {model_path}')

    def load_model(self):
        model_path = os.path.join(self.config['model_dir'], 'price_predictor.pkl')
        self.model = joblib.load(model_path)
        print(f'Model loaded from {model_path}')

    def predict(self, input_data):
        if self.model is None:
            self.load_model()
        return self.model.predict(input_data)