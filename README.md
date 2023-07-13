A machine learning **web application** created using python and hosted on AWS elastic beanstalk to predict whether the company's customer will churn (leave the company) or not.

🔗 [Checkout the hosted web application](http://customer-churn-predictor-env.eba-8imya9zv.ap-south-1.elasticbeanstalk.com/) 

The bussiness logic of the use case have been kept in mind throughout the project i.e. the idea is that we have to focus on customer retention. Therefore, along with the accuracy score huge consederation is given to the recall score to minimize false negatives predictions. 

**Dataset:** [Telco customer churn: IBM dataset](https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset) 

**ML Steps**
1. **EDA** using pandas and effective visualisation.
2. **Feature Selection** by checking impact of each variable on the target variable.
3. Target impbalance variable has been treated using **upsampling** technique to avoid data loss.
4. Numeric variable have been scaled and catagorical ones are enocoded using a **preprocessing pipeline.**
5. Compared 8 classification model and fine-tuned the selected optimum models using **GridSearchCV** 
6. The fine-tuned Random Forest model achieves an **accuracy score** of 95% and **recall score** of 98%, respectively

**Deployment Steps**
1. **Goes modular** to define each tasks
2. Create basics - logger, exception, requirements and code setup
3. **Data ingestion** reads the data and performs data cleaning, return cleaned dataset
4. **Data transformation** upsamples, separates X and y, transforms X; returns pre-processing pipeline as a pickle file
5. **Model trainer** splits the data into train-test sets, trains, predicts and returns accuracy and recall scores, returns model as a pickle file
6. **Flask Application** routes to the website hosted on AWS and takes new data 
7. **Predict pipline** feeds the new data to the preprocessor, model and makes prediction
8. **Deployed** the project on AWS beanstalk  
