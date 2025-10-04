import streamlit as st
import joblib
import numpy as np
import pandas as pd
model=joblib.load("canteen_meals_predictor.pkl")
le_day=joblib.load("le_day.pkl")
le_weather=joblib.load("le_weather.pkl")
st.title("Canteen Meal Predictor")
st.write("Enter the details to predict the number of meals to be served in the canteen.")
day=st.selectbox("Select Day",options=['Monday','Tuesday','Wednesday','Thursday','Friday'])
weather=st.selectbox("Select Weather",options=['Sunny','Rainy','Cloudy'])
event=st.number_input("Enter Event (0 for No event, 1 for Event)",min_value=0,max_value=1,step=1)
# Encode
day_enc = le_day.transform([day])[0]
weather_enc = le_weather.transform([weather])[0]
event_enc = 1 if event == "Special Event" else 0

# Prediction
sample = pd.DataFrame([[day_enc, weather_enc, event_enc]], 
                      columns=["Day", "Weather", "Event"])
prediction = model.predict(sample)[0]

st.write(f"🍽️ Predicted Meals: **{int(prediction)}**")