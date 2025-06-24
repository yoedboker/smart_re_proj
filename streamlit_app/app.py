import streamlit as st
from src.advisor import data_processing, model, utils

# Load the trained model
model_path = 'models/price_predictor.pkl'
loaded_model = utils.load_model(model_path)

# Title of the app
st.title("Real Estate Price Advisor")

# Sidebar for user input
st.sidebar.header("User Input Features")

def user_input_features():
    # Collect user inputs for the model
    area = st.sidebar.number_input("Area (in sq ft)", min_value=0)
    bedrooms = st.sidebar.number_input("Number of Bedrooms", min_value=0)
    bathrooms = st.sidebar.number_input("Number of Bathrooms", min_value=0)
    location = st.sidebar.selectbox("Location", options=["Location A", "Location B", "Location C"])
    
    data = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "location": location
    }
    return data

input_data = user_input_features()

# Process the input data
processed_data = data_processing.process_input_data(input_data)

# Make predictions
prediction = loaded_model.predict(processed_data)

# Display the prediction
st.write(f"Predicted Price: ${prediction[0]:,.2f}")