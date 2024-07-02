# :bicyclist:Bike-Sharing Demand Prediction
## :briefcase:Overview
The Bike Share Prediction System is designed to forecast the demand for bike-sharing services using machine learning techniques. This system aims to provide accurate Tpredictive model to forecast bike rental counts based on various features such as date, weather conditions, and time of daypredictions on bike rentals, which can help operators optimize bike distribution, reduce maintenance costs, and enhance user experience.

## Folder structure

     ├── Data Base/
     │   ├── DB_app.py
     │   ├── DB_connection.py
     │   ├── Readme.txt
     ├── artifacts/
     │   ├── data.csv
     │   ├── model.pkl
     │   ├── preprocessor.pkl
     │   ├── test.csv
     │   ├── train.csv
     ├── notebook/
     │   ├── data/
     │   │   ├── Readme.txt
     │   │   ├── day.csv
     │   │   ├── hour.csv
     │   │   ├── hour1.csv
     │   ├── MODEL_TRAINING.ipynb
     │   ├── bike share prediction EDA.ipynb
     ├── src/
     │   ├── components/
     │   │   ├── __init__.py
     │   │   ├── data_ingestion.py
     │   │   ├── data_transformation.py
     │   │   ├── model_trainer.py
     │   ├── pipelines/
     │   │   ├── __init__.py
     │   │   ├── prediction_pipeline.py
     │   ├── __init__.py
     │   ├── exception.py
     │   ├── logger.py
     │   ├── utils.py
     ├── templates/
     │   ├── home.html
     │   ├── index.html
     ├── .gitattributes
     ├── .gitignore
     ├── README.md
     ├── flask_app.py
     ├── requirements.txt
     ├── setup.py
     ├── streamlit_app.py


## Detailed Folder and File Descriptions
* Data Base/: Contains database connection and application scripts.
* artifacts/:Directory to store model and evaluation results and perform predictions.
 notebook/: Jupyter notebooks for data exploration, preprocessing, and model development.
src/pipeline/:Source code for different implemented pipelines.
 src/: Source code for the project, including preprocessing functions and model training.
 src/components/: Source code for preprocessing functions and model training.
 src/pipelines/: Source code for different implemented pipelines.
 templates/: Contains the basic frontend framework for deployment using Flask.
 flask_app.py: Flask application script.
 setup.py: Setup script for the project.
 streamlit_app.py: Streamlit application script.

deploy link:https://ranasanga85-bike-share-prediction-system.streamlit.app/
