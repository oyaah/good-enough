import os
import sys 
from source.MLproject.logger import logging 
from source.MLproject.exception import CustomException
import pandas as pd 
from dotenv import load_dotenv
import pymysql
import pickle
import numpy as np

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')


def read_sql_data():
    logging.info('Reading SQL database has started')
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db='college'

        )
        logging.info("Connectio established",mydb)
        df=pd.read_sql_query('Select * from student',mydb)
        print(df.head())


        return df 

    except Exception as e:
        raise CustomException(e,sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)



