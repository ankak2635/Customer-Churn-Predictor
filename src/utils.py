import sys
import os
from src.logger import logging
from src.exception import CustomException


import pickle


# Function to save objects as pickle file
def save_as_pickle(file_path, obj):
    try:
        # Get the file path
        dir_path = os.path.dirname(file_path)

        # Create a directory
        os.makedirs(dir_path, exist_ok=True)

        # Save as pickle file
        with open (file_path, "wb") as obj_file:
            pickle.dump(obj, obj_file)
    except Exception as e:
        raise CustomException(e,sys)
    
# Function which loads a pickle file
def load_pickle(file_path):
    try:
        with open(file_path,"rb") as obj_file:
            return pickle.load(obj_file)

    except Exception as e:
        raise CustomException(e,sys)
        
