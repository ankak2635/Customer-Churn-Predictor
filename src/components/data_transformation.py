import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import save_as_pickle
from dataclasses import dataclass

import pandas as pd
from sklearn.utils import resample
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

@dataclass
class data_transform_config:
    preprocessor_path:str = os.path.join('artifacts', 'preprocessor.pkl')
    # train_data_path:str = os.path.join('artifacts', 'train_data.csv')
    # test_data_path:str = os.path.join('artifacts', 'test_data.csv')


class data_transformation:
    def __init__(self):
        self.data_transformation_config = data_transform_config()

    def data_transformer(self, data_path):
        ''' 
        A function which defines how the data will be transformed
        '''

        try:

            # Read the filtered data
            filtered_df = pd.read_csv(data_path)
            

            # extract catagorical and numerical features 
            cat_features = [i for i in filtered_df.columns if filtered_df[i].dtype == 'object']
            num_cols = ['TenureMonths', 'MonthlyCharges', 'CLTV',  'ChurnScore']
            logging.info("Got numerical and catagorical cols")

            # define column transformer
            num_transformer = StandardScaler()
            cat_transformers = OneHotEncoder()


            logging.info("Reached transformation pipeline")
            # define pipeline
            preprocessor = ColumnTransformer(
                [
                    ('Scaling', num_transformer, num_cols),
                    ('OneHotEncoder', cat_transformers, cat_features)
                ]
            )

            return preprocessor

        except Exception as e:
             raise CustomException(e,sys)



    def initiate_data_transformation(self, data_path): # takes raw data path

        try:

            logging.info("Entered data transformation")

            # Read the filtered data 
            filtered_df = pd.read_csv(data_path)
            logging.info("Read the filtered data")

            # treat the imbalance in the target variable
            # make two seperate dfs for churned and not churned
            churned = filtered_df[filtered_df['ChurnValue']==1]
            not_churned = filtered_df[filtered_df['ChurnValue'] == 0] 

            # upsample the churned df
            churned_upsampled = resample(churned, 
                             replace = True, 
                             n_samples = len(not_churned),
                             random_state = 1)
            
            # combine the upsampled data
            combined_df = pd.concat([churned_upsampled, not_churned])
            logging.info("Target imbalance treated")

            # Separate X and y
            X = combined_df.drop(columns=['ChurnValue'], axis= 1)
            y = combined_df['ChurnValue']
            logging.info("X and y separated")


            # Get the preprocessor object
            preprocessor_obj = self.data_transformer(data_path)
        

            # Transform the data
            X= preprocessor_obj.fit_transform(X)
            logging.info("Tranformed X")

            # Save preprocessor object as pickle file 
            save_as_pickle(self.data_transformation_config.preprocessor_path,
                           preprocessor_obj)

            return self.data_transformation_config.preprocessor_path, X, y

        except Exception as e:
            raise CustomException(e,sys)
            






