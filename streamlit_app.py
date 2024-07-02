import streamlit as st
import pandas as pd
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

# Set up the Streamlit app
st.title("Bike Share Prediction System")

# Form for user input
st.sidebar.header('User Input Parameters')
def user_input_features():
    season_options = {'Winter': 1, 'Spring': 2, 'Summer': 3, 'Fall': 4}
    weather_options = {'Clear': 1, 'Mist': 2, 'Light Snow, Light Rain': 3, 'Heavy Rain': 4}
    
    season = st.sidebar.selectbox('Season', list(season_options.keys()))
    year = st.sidebar.slider('Year', 2011, 2012, 2011)
    month = st.sidebar.slider('Month', 1, 12, 1)
    hour = st.sidebar.slider('Hour', 0, 23, 0)
    holiday = st.sidebar.selectbox('Holiday', [0, 1])
    weekday = st.sidebar.selectbox('Weekday', [0, 1, 2, 3, 4, 5, 6])
    workingday = st.sidebar.selectbox('Working Day', [0, 1])
    weather = st.sidebar.selectbox('Weather', list(weather_options.keys()))
    temp = st.sidebar.slider('Temperature', 0.0, 50.0, 25.0)
    atemp = st.sidebar.slider('Atemp', 0.0, 50.0, 25.0)
    humidity = st.sidebar.slider('Humidity', 0.0, 100.0, 50.0)
    windspeed = st.sidebar.slider('Windspeed', 0.0, 100.0, 10.0)

    data = {'season': season_options[season],
            'year': year,
            'month': month,
            'hour': hour,
            'holiday': holiday,
            'weekday': weekday,
            'workingday': workingday,
            'weather': weather_options[weather],
            'temp': temp,
            'atemp': atemp,
            'humidity': humidity,
            'windspeed': windspeed}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display user input features
st.subheader('User Input parameters')
st.write(input_df)

# Prediction
if st.button('Predict'):
    data = CustomData(
        season=int(input_df['season'].values[0]),
        year=int(input_df['year'].values[0]),
        month=int(input_df['month'].values[0]),
        hour=int(input_df['hour'].values[0]),
        holiday=int(input_df['holiday'].values[0]),
        weekday=int(input_df['weekday'].values[0]),
        workingday=int(input_df['workingday'].values[0]),
        weather=int(input_df['weather'].values[0]),
        temp=float(input_df['temp'].values[0]),
        atemp=float(input_df['atemp'].values[0]),
        humidity=float(input_df['humidity'].values[0]),
        windspeed=float(input_df['windspeed'].values[0])
    )

    pred_df = data.get_data_as_data_frame()
    st.write('Input DataFrame:')
    st.write(pred_df)
    
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    
    st.subheader('Prediction')
    st.write(int(results[0]))
