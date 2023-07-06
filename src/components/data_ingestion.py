import os
import sys
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split

@dataclass
class data_ingestion_config:
    raw_data_path:str = os.path.join('artifacts', 'raw_data.csv')
    # train_data_path:str = os.path.join('artifacts', 'train_data.csv')
    # test_data_path:str = os.path.join('artifacts', 'test_data.csv')

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
            logging.info("Dropped unnecessary columns")

            # make directory and save the df
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, header=True, index=False)
            logging.info("Data ingestion complete")

            # data transformation
                # 1. treat the imbalance 
                # 2. separate X and y
                # 3. get cat and num cols
                # 4. transformation pipeline 

            return self.ingestion_config.raw_data_path

            
        except Exception as e:
            raise CustomException(e,sys)
            

# if __name__=="__main__":
#     obj = data_ingestion()
#     obj.initiate_data_ingestion()

    
