import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('rf_model.pkl')

# App title
st.title("🏡 House Price Prediction")

# User input interface
area = st.slider("Area (sqft)", 1000, 15000, step=100)
bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5, 6])
bathrooms = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])
stories = st.selectbox("Number of Stories", [1, 2, 3, 4])
parking = st.selectbox("Parking Spaces", [0, 1, 2, 3])

mainroad = st.radio("Is the property on the main road?", ["yes", "no"])
guestroom = st.radio("Guestroom available?", ["yes", "no"])
basement = st.radio("Basement available?", ["yes", "no"])
hotwater = st.radio("Hot water heating?", ["yes", "no"])
aircon = st.radio("Air Conditioning?", ["yes", "no"])
prefarea = st.radio("In Preferred Area?", ["yes", "no"])
furnishing = st.radio("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

# Prepare input data
input_data = pd.DataFrame([[
    area,
    bedrooms,
    bathrooms,
    stories,
    1 if mainroad == "yes" else 0,
    1 if guestroom == "yes" else 0,
    1 if basement == "yes" else 0,
    1 if hotwater == "yes" else 0,
    1 if aircon == "yes" else 0,
    parking,
    1 if prefarea == "yes" else 0,
    ["furnished", "semi-furnished", "unfurnished"].index(furnishing)
]], columns=[
    "area", "bedrooms", "bathrooms", "stories", "mainroad", "guestroom",
    "basement", "hotwaterheating", "airconditioning", "parking",
    "prefarea", "furnishingstatus"
])

# Make prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Normalized Price: {prediction:.4f}")
