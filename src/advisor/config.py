# Configuration settings for the real estate advisor project

# Global settings
DATA_DIR = 'data/'
RAW_DATA_DIR = f'{DATA_DIR}raw/'
PROCESSED_DATA_DIR = f'{DATA_DIR}processed/'

# Model settings
MODEL_DIR = 'models/'
MODEL_FILENAME = 'price_predictor.pkl'

# Hyperparameters
HYPERPARAMETERS = {
    'learning_rate': 0.1,
    'n_estimators': 100,
    'max_depth': 5,
    'subsample': 0.8,
    'colsample_bytree': 0.8
}

# Streamlit app settings
STREAMLIT_PORT = 8501

# Telegram bot settings
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'