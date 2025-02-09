import streamlit as st
import xgboost as xgb
import numpy as np

# Load trained model
model_path = "/content/optimized_xgboost_Optuna.model"
loaded_model = xgb.XGBRegressor()
loaded_model.load_model(model_path)

# Title of the web app
st.title("Concrete Strength Prediction App")
st.write("Enter the input values below to predict compressive strength.")

# Input fields for user
cement = st.number_input("Cement (kg/m³)", min_value=0.0, format="%.2f")
fly_ash = st.number_input("Fly Ash (kg/m³)", min_value=0.0, format="%.2f")
water = st.number_input("Water (kg/m³)", min_value=0.0, format="%.2f")
superplasticizer = st.number_input("Superplasticizer (kg/m³)", min_value=0.0, format="%.2f")
coarse_aggregate = st.number_input("Coarse Aggregate (kg/m³)", min_value=0.0, format="%.2f")
fine_aggregate = st.number_input("Fine Aggregate (kg/m³)", min_value=0.0, format="%.2f")
age = st.number_input("Age of Concrete (Days)", min_value=1, format="%d")

# Prediction
if st.button("Predict Strength"):
    input_data = np.array([[cement, fly_ash, water, superplasticizer, coarse_aggregate, fine_aggregate, age]])
    prediction = loaded_model.predict(input_data)
    st.success(f"Predicted Compressive Strength: {prediction[0]:.2f} MPa")
