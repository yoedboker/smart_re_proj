# real_estate_advisor

## Project Overview
The Real Estate Advisor project is designed to provide insights and predictions related to real estate prices using machine learning techniques. This project includes data processing, model training, and a user interface for interaction.

## Directory Structure
- **data/**: Contains raw and processed data files.
  - **raw/**: Original CSV files.
  - **processed/**: Cleaned and feature-engineered data files.
  
- **src/**: Main package containing core modules.
  - **advisor/**: Core application modules for data processing, model training, and utility functions.
  
- **models/**: Directory for storing the trained model.
  
- **notebooks/**: Jupyter notebooks for exploratory data analysis (EDA).
  
- **streamlit_app/**: Streamlit application files for user interaction.
  
- **telegram_bot/**: Logic for the Telegram bot to provide real estate insights.
  
- **llm/**: Integration with language models for natural language explanations.
  
- **tests/**: Unit tests for ensuring code quality and functionality.
  
- **scripts/**: One-off scripts for tasks like model training.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd real_estate_advisor
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare the data:
   - Place your raw CSV files in the `data/raw/` directory.
   - Run the data processing script to clean and prepare the data.

4. Train the model:
   - Execute the training script located in the `scripts/` directory:
   ```
   python scripts/train_model.py
   ```

5. Run the Streamlit application:
   ```
   streamlit run streamlit_app/app.py
   ```

## Usage
- Use the Streamlit app to interact with the model and get predictions.
- The Telegram bot can be used to receive insights via messaging.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.