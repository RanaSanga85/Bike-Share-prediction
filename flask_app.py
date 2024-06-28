from flask import Flask, request, render_template, redirect, url_for, flash
import pandas as pd
import logging
import os
import joblib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key for security

# Function to set up the logger
def setup_logger():
    """
    Sets up a logger to log information to a file named 'web_logs.log'.
    Creates a 'logs' directory in the script's directory if it doesn't exist.
    Returns the logger object.
    """
    web_log = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    os.makedirs(web_log, exist_ok=True)
    log_file = "web_logs.log"
    log_file_path = os.path.join(web_log, log_file)
    logging.basicConfig(
        filename=log_file_path,
        format="[%(asctime)s] %(levelname)s - %(message)s",
        level=logging.INFO,
        filemode='a'
    )
    logger = logging.getLogger()
    return logger


logger = setup_logger()

# Load the pre-trained Random Forest model from a file
try:
    model = joblib.load('random_forest_model.joblib')
except FileNotFoundError:
    logger.error("Model file not found. Ensure 'random_forest_model.joblib' is in the correct directory.")
    raise

# Function to make predictions using the loaded model
def predict(data):
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)
    logger.info("User input received correctly.")
    logger.info(f"Input Data: {data}")
    logger.info(f"The predicted count is {prediction[0]}.")
    return prediction[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        input_data = {
            'hour': request.form.get('hour', type=int),
            'temp': request.form.get('temp', type=float),
            'workingday': request.form.get('workingday', type=int),
            'humidity': request.form.get('humidity', type=float),
            'season': request.form.get('season', type=int),
            'atemp': request.form.get('atemp', type=float),
            'weather': request.form.get('weather', type=int),
            'month': request.form.get('month', type=int),
            'weekday': request.form.get('weekday', type=int),
            'windspeed': request.form.get('windspeed', type=float),
            'casual': request.form.get('casual', type=int),
            'registered': request.form.get('registered', type=int)
        }
        # Make prediction
        try:
            prediction = predict(input_data)
            flash(f'Predicted Bike Demand: {round(prediction)}', 'success')
        except Exception as e:
            logger.error(f"Error during prediction: {e}")
            flash('Error during prediction. Check the input values.', 'danger')
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
