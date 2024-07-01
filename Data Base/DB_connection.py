import pandas as pd
import uuid
from datetime import datetime
from astrapy import DataAPIClient
from astrapy.exceptions import InsertManyException, CollectionAlreadyExistsException
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

# Prompt the user for Astra DB API endpoint and application token
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

# Mock data for example purposes
input_data = CustomData(
      season=int('season'),
            year=int('year'),
            month=int('month'),
            hour=int('hour'),
            holiday=int('holiday'),
            weekday=int('weekday'),
            workingday=int('workingday'),
            weather=int('weather'),
            temp=float('temp'),
            atemp=float('atemp'),
            humidity=float('humidity'),
            windspeed=float('windspeed')
)

# Mock prediction result for example purposes
predict_pipeline = PredictPipeline()
# Prepare data for insertion into the database
data = [
    {
        "_id": str(uuid.uuid4()),
        "hour": input_data['hour'],
        "year":input_data['year'],
        "temp": input_data['temp'],
        "workingday": input_data['workingday'],
        "humidity": input_data['humidity'],
        "season": input_data['season'],
        "atemp": input_data['atemp'],
        "weather": input_data['weather'],
        "month": input_data['month'],
        "weekday": input_data['weekday'],
        "windspeed": input_data['windspeed'],
        "prediction": round(predict_pipeline)
    }
]

# Insert the data into the collection
try:
    collection.insert_many(data)
    print("Data inserted successfully.")
except InsertManyException as e:
    print(f"Error inserting data: {e}")
