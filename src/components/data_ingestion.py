import os
import sys
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException

from src.components.data_transformation import data_transformation, data_transform_config
from src.components.model_trainer import model_trainer_config, model_trainer

import pandas as pd
from sklearn.model_selection import train_test_split

@dataclass
class data_ingestion_config:
    raw_data_path:str = os.path.join('artifacts', 'raw_data.csv')

class data_ingestion:
    def __init__(self):
        self.ingestion_config = data_ingestion_config()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion initiated")
        try:
            # read the data
            df = pd.read_csv('notebook\churn_df.csv')
            logging.info("Read the data as dataframe")

            # drop unnecessary cols as observed in the notebook
            df.drop(columns=df.columns[:9], inplace=True, axis=1)
            df.drop(columns=['Churn Reason', 'Churn Label', 'Gender','Total Charges'], inplace= True, axis= 1)
            logging.info("Dropped unnecessary columns i.e. filtered data")

            # make directory and save the df
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, header=True, index=False)
            logging.info("Data ingestion complete")

            return self.ingestion_config.raw_data_path

            
        except Exception as e:
            raise CustomException(e,sys)
            

if __name__=="__main__":
    # call data ingestion
    obj = data_ingestion()
    raw_data_path = obj.initiate_data_ingestion()

    # call data transformation
    data_tranformation = data_transformation()
    _,X,y = data_tranformation.initiate_data_transformation(raw_data_path)
    print("Shape of features and target:", X.shape, y.shape)

    # call model trainer
    model_trainer = model_trainer()
    acc, recall, train_acc = model_trainer.initiate_model_trainer(X, y)
    print("Train Accuracy Score:", train_acc)
    print("Test Accuracy Score:", acc)
    print("Test Recall Score:", recall)





    
