from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            season=int(request.form.get('season')),
            year=int(request.form.get('year')),
            month=int(request.form.get('month')),
            hour=int(request.form.get('hour')),
            holiday=int(request.form.get('holiday')),
            weekday=int(request.form.get('weekday')),
            workingday=int(request.form.get('workingday')),
            weather=int(request.form.get('weather')),
            temp=float(request.form.get('temp')),
            atemp=float(request.form.get('atemp')),
            humidity=float(request.form.get('humidity')),
            windspeed=float(request.form.get('windspeed')),
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("After Prediction")
        return render_template('home.html', results=int(results[0]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
