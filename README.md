# <h1 align="center">:bicyclist:Bike-Sharing Demand Prediction
## :briefcase:Overview
The Bike Share Prediction System is designed to forecast the demand for bike-sharing services using machine learning techniques. This system aims to provide accurate Tpredictive model to forecast bike rental counts based on various features such as date, weather conditions, and time of daypredictions on bike rentals, which can help operators optimize bike distribution, reduce maintenance costs, and enhance user experience.

## Repository Structure

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
     ├── flask_app.py
     ├── requirements.txt
     ├── setup.py
     ├── streamlit_app.py


## :open_file_folder:Detailed Folder and File Descriptions
* `Data Base/`:Contains database connection and application scripts.
* `artifacts/`:Directory to store model and evaluation results and perform predictions.
* `notebook/`: Jupyter notebooks for data exploration, preprocessing, and model development.
* `src/pipeline/`:Source code for different implemented pipelines.
* `src/`: Source code for the project, including preprocessing functions and model training.
* `src/components/`: Source code for preprocessing functions and model training.
* `src/pipelines/`: Source code for different implemented pipelines.
* `templates/`: Contains the basic frontend framework for deployment using Flask.

##  :books:Dataset
  The data is on [UCI Repository](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset)

## Setup and Dependencies
To run the project locally, ensure you have the following dependencies installed:
- Python 
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Flask
- streamlit

Once you have the dependencies, follow these steps to set up the project:
1. Clone the repository:```git clone https://github.com/Pratik.94229/Bike-sharing-demand-prediction.git```
2. Navigate to the project directory: cd Bike-sharing-demand-prediction
3. Create a virtual environment (optional): conda create -p venv python==3.8
4. Activate the virtual environment (optional): activate venv/
5. Install the required packages: pip install -r requirements.txt
  


deploy link:https://ranasanga85-bike-share-prediction-system.streamlit.app/
