import sys
import os 
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from src.utils import save_as_pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score

@dataclass
class model_trainer_config:
    model_path: str = os.path.join('artifacts', 'model.pkl')

class model_trainer:
    def __init__(self):
        self.trainer_config = model_trainer_config()

    def initiate_model_trainer(self, features, target):
        try:
            logging.info("Entered model trainer")

            X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=1)
            logging.info("Train test split completed")

            # define model using the best parameters obtained from notebook experiment
            model = RandomForestClassifier(n_estimators=100, max_depth= 50, max_samples= 2500) 

            # model training 
            model.fit(X_train, y_train)
            logging.info("Model trained")

            # make prediction
            train_preds = model.predict(X_train)
            preds = model.predict(X_test)
            logging.info("Made predictions")

            # evaluate model
            test_accuracy = accuracy_score(y_train, train_preds)
            accuracy = accuracy_score(y_test, preds)
            recall = recall_score(y_test, preds)

            # save model
            save_as_pickle(self.trainer_config.model_path, model)

            return accuracy, recall, test_accuracy


        except Exception as e:
            raise CustomException(e,sys)





