#script is to connect to a DataStax Cassandra database, create or access a collection, and insert data into it.


import pandas as pd
from datetime import datetime
from astrapy import DataAPIClient

from astrapy.exceptions import InsertManyException, CollectionAlreadyExistsException

# Prompt the user for Astra DB API endpoint and application token
ASTRA_DB_API_ENDPOINT = ("ASTRA_DB_API_ENDPOINT = ")
ASTRA_DB_APPLICATION_TOKEN = ("ASTRA_DB_APPLICATION_TOKEN = ")

# Initialize Astra client using the provided application token
client = DataAPIClient(ASTRA_DB_APPLICATION_TOKEN)

# Get the database instance using the API endpoint
db = client.get_database_by_api_endpoint(ASTRA_DB_API_ENDPOINT)

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

   # Prepare data for insertion into the database
data = [
        {
                "_id": str(uuid.uuid4()),
                "hour": input_data['hour'],
                "temp": input_data['temp'],
                "workingday": input_data['workingday'],
                "humidity": input_data['humidity'],
                "season": input_data['season'],
                "atemp": input_data['atemp'],
                "weather": input_data['weather'],
                "month": input_data['month'],
                "weekday": input_data['weekday'],
                "windspeed": input_data['windspeed'],
                "casual": input_data['casual'],
                "registered": input_data['registered'],
                "prediction": round(prediction)
            }
        ]

        # Insert the data into the collection
try:
    collection.insert_many(data)
    flash("Data inserted successfully!")
except InsertManyException as e:
    flash(f"Error inserting data: {e}")