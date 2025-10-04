🍽️ Canteen Meal Demand Predictor
📌 Project Overview

This project predicts the number of meals required in a canteen based on day, weather, and events.
The goal is to help canteens avoid food wastage and ensure adequate meal preparation using Machine Learning.

The app is built using:

Python (scikit-learn, pandas, numpy) for ML model

Streamlit for the web app interface

Joblib for saving/loading trained models

🚀 Features

✅ Predicts meal demand based on Day, Weather, Event
✅ Interactive Streamlit Web App
✅ Prevents food shortage or wastage
✅ Can be extended with features like holidays, exam periods, special occasions

🛠️ Tech Stack

Machine Learning → Linear Regression / RandomForestRegressor (tweakable)

Preprocessing → Label Encoding for categorical features

Model Deployment → Streamlit App

Version Control → Git + GitHub

📊 Dataset

The dataset contains:

Day → Day of the week (Monday–Sunday)

Weather → Weather condition (Sunny, Rainy, Cloudy, etc.)

Event → Whether a special event is happening (0 = No Event, 1 = Event)

Meals_Sold → Number of meals sold (target variable)

▶️ How to Run Locally

Clone the repo:

git clone https://github.com/janiarithvika11/canteen_predictor.git
cd canteen_predictor


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

🌍 Deployment

The app is deployed on Streamlit Cloud.
👉 Click here to try the live demo -->  https://canteenpredictor-sgeafubtc7mxupu2j2adnv.streamlit.app/

📷 Screenshots

<img width="969" height="602" alt="image" src="https://github.com/user-attachments/assets/30c1abc6-33a9-43f3-96ea-f8fc8d630cb6" />


📌 Future Improvements

Add more features (holidays, exam periods, student strength)

Use time-series forecasting for long-term predictions

Improve accuracy with advanced ML models (XGBoost, LSTM)
