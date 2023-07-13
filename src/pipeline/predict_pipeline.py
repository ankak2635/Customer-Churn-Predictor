import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import load_pickle

import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = os.path.join("artifacts/preprocessor.pkl")
            model_path = os.path.join("artifacts/model.pkl")

            # load the preprocessor and model
            preprocessor = load_pickle(preprocessor_path)
            model =load_pickle(model_path)

            # Preprocess the user input data
            processed_data = preprocessor.transform(features)

            # make prediction
            pred = model.predict(processed_data)

            return pred
        
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self, 
                 SeniorCitizen:str,
                 Partner:str,
                 Dependents:str, 
                 TenureMonths:str,
                 PhoneService:str,
                 MultipleLines:str,
                 InternetService:str,
                 OnlineSecurity:str, 
                 OnlineBackup:str, 
                 DeviceProtection:str, 
                 TechSupport:str,
                 StreamingTV:str, 
                 StreamingMovies:str, 
                 Contract:str,
                 PaperlessBilling:str,
                 PaymentMethod:str, 
                 MonthlyCharges:float,
                 ChurnScore:int,
                 CLTV:int):
        
        self.SeniorCitizen = SeniorCitizen
        self.Partner = Partner 
        self.Dependents = Dependents 
        self.TenureMonths = TenureMonths
        self.PhoneService = PhoneService
        self.MultipleLines = MultipleLines
        self.InternetService = InternetService
        self.OnlineSecurity = OnlineSecurity
        self.OnlineBackup = OnlineBackup 
        self.DeviceProtection = DeviceProtection
        self.TechSupport = TechSupport
        self.StreamingTV = StreamingTV 
        self.StreamingMovies = StreamingMovies 
        self.Contract = Contract
        self.PaperlessBilling = PaperlessBilling
        self.PaymentMethod = PaymentMethod 
        self.MonthlyCharges = MonthlyCharges
        self.ChurnScore = ChurnScore
        self.CLTV = CLTV

    def get_as_dataframe(self):
        try:
            input_dict = {
                        'SeniorCitizen' : [self.SeniorCitizen],
                        'Partner' : [self.Partner],
                        'Dependents' : [self.Dependents],
                        'TenureMonths' : [self.TenureMonths],
                        'PhoneService' : [self.PhoneService],
                        'MultipleLines' : [self.MultipleLines],
                        'InternetService' : [self.InternetService],
                        'OnlineSecurity' : [self.OnlineSecurity],
                        'OnlineBackup' : [self.OnlineBackup], 
                        'DeviceProtection' : [self.DeviceProtection],
                        'TechSupport' : [self.TechSupport],
                        'StreamingTV' : [self.StreamingTV], 
                        'StreamingMovies' : [self.StreamingMovies],
                        'Contract' : [self.Contract],
                        'PaperlessBilling' : [self.PaperlessBilling],
                        'PaymentMethod' : [self.PaymentMethod],
                        'MonthlyCharges' : [self.MonthlyCharges],
                        'ChurnScore' : [self.ChurnScore],
                        'CLTV' : [self.CLTV],
            }

            return pd.DataFrame(input_dict)
        

        except Exception as e:
            raise CustomException(e,sys)