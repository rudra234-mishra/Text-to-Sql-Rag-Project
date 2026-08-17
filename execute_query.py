from logging_config import logger
from model_db import database_conn
import pandas as pd


def execute(query:str):
    try:
        conn=database_conn()
        logger.info("Query Execution Start :")
        data=pd.read_sql_query(query,con=conn)

        logger.info("Query Execution Successfull :")
        return data 


    except Exception as exc:
        logger.error("Query Execution Failed :%s",exc)

    
