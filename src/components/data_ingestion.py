import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.model_tranier import ModelTrainer

@dataclass
class DataIngestionConfig:
    #The DataIngestionConfig class is a configuration class that holds the file paths used for data ingestion
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self): #Constructor method that initializes the DataIngestion instance.
        #Initializes the DataIngestionConfig instance to store file paths.
        self.ingestion_config = DataIngestionConfig() 

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv(r'C:\Users\risha\Desktop\bike share\notebook\data\hour.csv')
            logging.info("Read the dataset as dataframe")

            #Creates directories for the data paths if they don't exist.
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
 
            #Saves the sets to the specified path.
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of data is completedd")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)



if __name__ == "__main__":
    obj = DataIngestion()
    #Initiates data ingestion and gets the paths of the training and test data files.
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    # Initiates data transformation on the training and test data.
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    modeltrainer=ModelTrainer()
    # Initiates model training using the transformed training and test data and prints the result.
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))