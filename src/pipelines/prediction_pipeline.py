import os
import sys
import pandas as pd
from src.exception import CustomException
import pickle
from src.utils import save_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts","model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            print("Before Loading")
            with open(model_path, 'rb') as model_file:
                model = pickle.load(model_file)
            with open(preprocessor_path, 'rb') as preprocessor_file:
                preprocessor = pickle.load(preprocessor_file)
            
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 season: int,
                 year: int,
                 month: int,
                 hour: int,
                 holiday: int,
                 weekday: int,
                 workingday: int,
                 weather: int,
                 temp: float,
                 atemp: float,
                 humidity: float,
                 windspeed: float):

        self.season = season
        self.year = year
        self.month = month
        self.hour = hour
        self.holiday = holiday
        self.weekday = weekday
        self.workingday = workingday
        self.weather = weather
        self.temp = temp
        self.atemp = atemp
        self.humidity = humidity
        self.windspeed = windspeed

    def get_data_as_data_frame(self):
        try:
            #Creates a dictionary where each key is a feature name and each value is a
            #list containing the corresponding attribute.
            custom_data_input_dict = {
                "season": [self.season],
                "year": [self.year],
                "month": [self.month],
                "hour": [self.hour],
                "holiday": [self.holiday],
                "weekday": [self.weekday],
                "workingday": [self.workingday],
                "weather": [self.weather],
                "temp": [self.temp],
                "atemp": [self.atemp],
                "humidity": [self.humidity],
                "windspeed": [self.windspeed]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
