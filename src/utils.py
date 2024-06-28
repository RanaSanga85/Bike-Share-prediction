import os
import sys

import numpy as np 
import pickle
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


from src.logger import logging

from src.exception import CustomException


#Defines a function to save an object to a specified file path.
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    

#Defines a function to evaluate multiple machine learning models.
def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        #Iterates over the models dictionary, where model_name is the name of the model and model is the model object.
        for model_name, model in models.items():
            # Train model
            model.fit(X_train, y_train)

            # Predict Testing data
            y_test_pred = model.predict(X_test)

            #Computes the R2 score for the test data predictions.
            test_model_score = r2_score(y_test, y_test_pred)
             
            #Stores the R2 score in the report dictionary with the model name as the key.
            report[model_name] = test_model_score
        
        # Returns the report dictionary containing R2 scores for all models.
        return report

    except Exception as e:
        logging.info('Exception occurred during models evaluation')
        raise CustomException(e, sys)
