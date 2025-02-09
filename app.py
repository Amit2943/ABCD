import streamlit as st
import xgboost as xgb
import numpy as np

# Load the trained model
model = xgb.XGBRegressor()
model.load_model("optimized_xgboost_Optuna.model")  # Replace with your actual model file

# Streamlit UI
st.title("Concrete Strength Prediction")
st.write("Enter the mix design parameters to predict strength")

# User input fields
Cement = st.number_input("Cement (kg/m³)", min_value=0.0, value=300.0)
Blast Furnace Slag = st.number_input("Blast Furnace Slag (kg/m³)", min_value=0.0, value=250.0)
Fly Ash = st.number_input("Fly Ash (kg/m³)", min_value=0.0, value=100.0)
Water = st.number_input("Water (kg/m³)", min_value=0.0, value=180.0)
Superplasticizer = st.number_input("Superplasticizer (kg/m³)", min_value=0.0, value=5.0)
Coarse Aggregate = st.number_input("Coarse Aggregate (kg/m³)", min_value=0.0, value=1000.0)
Fine Aggregate = st.number_input("Fine Aggregate (kg/m³)", min_value=0.0, value=800.0)
Age (day) = st.number_input("Age (days)", min_value=1, value=28)

# Prediction
if st.button("Predict"):
    features = np.array([[Cement, Blast Furnace Slag, Fly Ash, Water, Superplasticizerr, Coarse Aggregate, Fine Aggregate, Age (day)]])
    prediction = model.predict(features)
    st.success(f"Predicted Compressive Strength: {prediction[0]:.2f} MPa")
