# Customer Churn Prediction Web Application

Welcome to the Customer Churn Prediction Web Application project repository! This machine learning application, developed using Python, is hosted on AWS Elastic Beanstalk. Its primary objective is to predict whether a company's customers are likely to churn (leave the company) or remain as active customers.

🔗 **Check out the hosted web application [here](http://customer-churn-predictor-env.eba-8imya9zv.ap-south-1.elasticbeanstalk.com/).**

## Business Logic and Focus

Throughout the project, I have prioritized the business logic associated with customer retention. While achieving high accuracy is important, I have placed significant emphasis on the recall score to minimize false negative predictions.

## Dataset

The dataset used for this project is the "Telco Customer Churn" dataset from IBM.

## Machine Learning Workflow

The machine learning workflow comprises the following steps:

1. **Exploratory Data Analysis (EDA)**: Employing pandas and effective visualizations to gain insights from the dataset.

2. **Feature Selection**: Evaluating the impact of each variable on the target variable to determine the most relevant features.

3. **Addressing Target Imbalance**: Upsampling technique has been applied to treat the imbalanced target variable and prevent data loss.

4. **Data Preprocessing**: Numeric variables are scaled, and categorical ones are encoded using a preprocessing pipeline.

5. **Model Comparison and Selection**: Eight classification models are compared, and the optimal models are fine-tuned using GridSearchCV.

6. **Model Performance**: The fine-tuned Random Forest model achieves an accuracy score of 95% and a remarkable recall score of 98%.

## Deployment Steps

The deployment process has been modularized into distinct tasks:

1. **Data Ingestion**: Reads and cleans the data, providing a cleaned dataset.

2. **Data Transformation**: Performs upsampling, separates features and target, and applies transformations. The preprocessing pipeline is saved as a pickle file.

3. **Model Training**: Splits data into train-test sets, trains the model, and predicts outcomes. Accuracy and recall scores are returned, and the model is saved as a pickle file.

4. **Flask Application**: Routes to the web interface hosted on AWS, allowing input of new data.

5. **Prediction Pipeline**: Feeds new data to the preprocessor and model to make predictions.

6. **Deployment**: The project has been successfully deployed on AWS Elastic Beanstalk.

## Hosted Web Application Link

For a hands-on experience with the Customer Churn Prediction Web Application, please visit the hosted web application [here](http://customer-churn-predictor-env.eba-8imya9zv.ap-south-1.elasticbeanstalk.com/).

Thank you for your interest in our project!
