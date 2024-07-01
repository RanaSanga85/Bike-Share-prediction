# Data Insertion to AstraDB Using AstraPy
The Python script facilitates data insertion into an AstraDB instance using AstraPy,
a library for managing DataStax Astra databases. Here's a breakdown of how it works:

## 1.AstraDB Setup:
The script begins by prompting the user to input the Astra DB API endpoint and application token, 
which are essential for connecting to the AstraDB instance.

## 2.Database Connection:
Using the provided API endpoint and application token, AstraPy's DataAPIClient is initialized to establish a 
connection to the AstraDB instance.

## 3.Collection Management:
The script attempts to create a collection named "bike_predict" with a dimension of 13. 
If the collection already exists, it retrieves the existing collection instance.

## 4.Data Preparation:
Mock data is prepared using the CustomData class from src.pipelines.prediction_pipeline to simulate input parameters
such as season, year, month, hour, etc.These values are placeholders ('season', 'year', etc.) 
and can be replaced with actual data sources.

## 5.Prediction Pipeline:
A prediction pipeline (PredictPipeline) is instantiated to simulate a prediction result. 
The round() function is applied to the prediction output to ensure it's an integer, 
which is then stored in the "prediction" field.

## 6.Data Insertion:
The prepared data, including a unique _id, is structured into a list of dictionaries (data). 
This data is then inserted into the "bike_predict" collection using insert_many() method. 
Success or failure messages are printed based on the outcome.

## 7.Error Handling:
The script includes error handling to catch and display any exceptions that may occur during the data 
insertion process, such as InsertManyException, providing clarity on issues encountered during insertion attempts.
This script serves as a foundational example of how to connect to AstraDB, manage collections, 
prepare and insert data, and handle potential errors in the process.