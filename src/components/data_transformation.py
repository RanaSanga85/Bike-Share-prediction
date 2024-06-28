import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    #A string attribute that holds the path to save the preprocessing object.
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            logging.info('Data Transformation initiated')
            numerical_columns = ["season", "year", "month", "hour", "holiday", "weekday", "workingday", "weather", "temp",
                                 "atemp", "humidity", "windspeed"]
            categorical_columns = []

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("outlier_treatment", FunctionTransformer(self.outlier_treatment, validate=False)),
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder(handle_unknown="ignore"))
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipelines", cat_pipeline, categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def outlier_treatment(self, X):
        '''
        This function is responsible for outlier treatment using IQR method
        '''
        try:
            Q1 = np.percentile(X, 25, axis=0)
            Q3 = np.percentile(X, 75, axis=0)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            #Replaces values below the lower bound with the lower bound.
            X = np.where(X < lower_bound, lower_bound, X)
            #Replaces values above the upper bound with the upper bound.
            X = np.where(X > upper_bound, upper_bound, X)
            #Returns the data with outliers treated.
            return X

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            
            logging.info(f"Train DataFrame columns: {train_df.columns}")
            logging.info(f"Test DataFrame columns: {test_df.columns}")

            logging.info("Obtaining preprocessing object")

            # Calls the get_data_transformer_object method to get the preprocessing object.
            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "count"
            drop_columns = [target_column_name, "casual", "registered", "day"]

            # Check if drop columns are in DataFrame
            for col in drop_columns:
                if col not in train_df.columns:
                    raise CustomException(f"Column {col} not found in training data", sys)
                if col not in test_df.columns:
                    raise CustomException(f"Column {col} not found in test data", sys)

            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            # Extracts the target column from the training DataFrame.
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
            # Extracts the target column from the test DataFrame.
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training dataframe and testing dataframe.")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            #Concatenates the transformed training features and the target column into a single array.
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            #Concatenates the transformed test features and the target column into a single array.
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path, obj=preprocessing_obj
            )
            
            logging.info('Preprocessor pickle file saved')

            return (
                train_arr,
                test_arr,
                #Returns the transformed training and test arrays, and the path to the saved preprocessing object.
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
