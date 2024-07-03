# <h1 align="center">:bicyclist:Bike-Sharing Demand Prediction
## :briefcase:Overview
The Bike Share Prediction System is designed to forecast the demand for bike-sharing services using machine learning techniques. This system aims to provide accurate Tpredictive model to forecast bike rental counts based on various features such as date, weather conditions, and time of daypredictions on bike rentals, which can help operators optimize bike distribution, reduce maintenance costs, and enhance user experience.

## <h1 align="center">Repository Structure

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
     ├── templates

     
## <h1 align="center">:open_file_folder:Detailed Folder and File Descriptions
* `Data Base/`:Contains database connection and application scripts.
* `artifacts/`:Directory to store model and evaluation results and perform predictions.
* `notebook/`: Jupyter notebooks for data exploration, preprocessing, and model development.
* `src/pipeline/`:Source code for different implemented pipelines.
* `src/`: Source code for the project, including preprocessing functions and model training.
* `src/components/`: Source code for preprocessing functions and model training.
* `src/pipelines/`: Source code for different implemented pipelines.
* `templates/`: Contains the basic frontend framework for deployment using Flask.
  

##  <h1 align="center">:books:Dataset
  The data is on [UCI Repository](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset) 
  

## <h1 align="center">:desktop_computer:Setup and Dependencies
To run the project locally, ensure you have the following dependencies installed:
- Python 
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Flask
- streamlit

Once you have the dependencies, follow these steps to set up the project:
1. **Clone the repository:** `git clone https://github.com/RanaSanga85/Bike-Share-prediction.git`
2. **Create a virtual environment:** `conda create -p venv python`
3. **Activate the virtual environment:** `activate venv/`
4. **Install the required packages:** `pip install -r requirements.txt`

   
## <h1 align="center">:package:Model Building and Selection
To predict the bike rental count, several machine learning models were implemented and evaluated. The following algorithms were utilized:

 * Linear Regression
 * Lasso
 * Ridge
 * K-Neighbors Regressor
 * Decision Tree
 * Random Forest Regressor
 * AdaBoost Regressor

After training and evaluating these models, the Random Forest Regressor emerged as the final choice due to its superior accuracy and predictive power.


## Model Deployment
The chosen Random Forest model was deployed using Streamlit, a Python library designed for creating interactive web applications. This deployment allows users to enter relevant features such as date, weather conditions, and time to obtain the predicted bike rental count as the output.
 deploy link:https://ranasanga85-bike-share-prediction-system.streamlit.app/

 
##Streamlit Application
 1. Install the required dependencies:
        ```pip install -r requirements.txt```
 2. Train the model:
       ```python src/pipeline/training_pipeline.py```
 3. Run the Streamlit application:
       ```streamlit run streamlit_app.py```
 4. Open your web browser and navigate to the provided URL to access the application.
 5. Input the relevant features such as date, weather conditions, and time.
 6. Click the "Predict" button to see the predicted bike rental count.
   
Keep in mind that the accuracy of the predictions may vary depending on the input data and model performance.


##Conclusion
This project demonstrates the application of machine learning models in predicting bike rental counts. By leveraging the Random Forest Regressor and utilizing various input features such as date, weather conditions, and time, the model achieves accurate predictions. These predictions enable users to make informed decisions regarding bike rental management.

The deployment of the model using Streamlit provides a user-friendly and interactive way to access the predictions. This makes it accessible to a wide range of users, allowing for easy input of data and quick retrieval of rental count predictions.

##License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software, provided that the original copyright notice and this permission notice are included in all copies or substantial portions of the software.
