import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from src.utils import evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def evaluate_model(self, y_true, y_pred):
        mae = mean_absolute_error(y_true, y_pred)
        mse = mean_squared_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        rmse = np.sqrt(mse)
        return mae, mse, r2, rmse

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor()
            }

            results = []

            for model_name, model in models.items():
                logging.info(f"Training {model_name}")
                model.fit(X_train, y_train)
                
                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)
                
                train_mae_val, train_mse_val, train_r2_val, train_rmse_val = self.evaluate_model(y_train, y_train_pred)
                test_mae_val, test_mse_val, test_r2_val, test_rmse_val = self.evaluate_model(y_test, y_test_pred)
                
                results.append({
                    'Model': model_name,
                    'Train_RMSE': train_rmse_val,
                    'Test_RMSE': test_rmse_val,
                    'Train_MAE': train_mae_val,
                    'Test_MAE': test_mae_val,
                    'Train_R2': train_r2_val,
                    'Test_R2': test_r2_val
                })
            
            # Find the best model
            best_model_result = max(results, key=lambda x: x['Test_R2'])
            best_model_name = best_model_result['Model']
            best_model = models[best_model_name]
            best_model_score = best_model_result['Test_R2']

            if best_model_score < 0.6:
                raise CustomException("No best model found")
            
            logging.info(f"Best model found: {best_model_name} with R2 score: {best_model_score}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            return best_model_score
        
        except Exception as e:
            raise CustomException(e, sys)
