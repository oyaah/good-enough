import os
import sys 
from source.MLproject.logger import logging 
from source.MLproject.exception import CustomException
import pandas as pd 
from dotenv import load_dotenv
import pymysql

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


