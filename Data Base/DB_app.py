from flask import Flask, request, render_template
import uuid
from astrapy import DataAPIClient
from astrapy.exceptions import InsertManyException, CollectionAlreadyExistsException
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

# Flask application setup
application = Flask(__name__)
app = application

# Astra DB credentials (replace with your actual endpoint and token)
ASTRA_DB_API_ENDPOINT = input("ASTRA_DB_API_ENDPOINT: ")
ASTRA_DB_APPLICATION_TOKEN = input("ASTRA_DB_APPLICATION_TOKEN: ")

# Initialize Astra client using the provided application token
client = DataAPIClient(ASTRA_DB_APPLICATION_TOKEN)

# Get the database instance using the API endpoint
db = client.get_database(ASTRA_DB_API_ENDPOINT)

# Attempt to create the collection or get the existing one
try:
    collection = db.create_collection(
        "bike_predict",  # Collection name
        dimension=13,    # Dimension of the collection
        check_exists=True  # Check if collection already exists
    )
except CollectionAlreadyExistsException:
    # If the collection already exists, get the existing collection
    collection = db.get_collection("bike_predict")

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

        # Prepare data for insertion into the database
        data_to_insert = {
            "_id": str(uuid.uuid4()),
            "hour": data.hour,
            "year": data.year,
            "temp": data.temp,
            "workingday": data.workingday,
            "humidity": data.humidity,
            "season": data.season,
            "atemp": data.atemp,
            "weather": data.weather,
            "month": data.month,
            "weekday": data.weekday,
            "windspeed": data.windspeed,
            "prediction": int(results[0])
        }

        try:
            collection.insert_one(data_to_insert)
            print("Data inserted successfully.")
        except InsertManyException as e:
            print(f"Error inserting data: {e}")

        return render_template('home.html', results=int(results[0]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
