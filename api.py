from fastapi import FastAPI
from pydantic import BaseModel,Field
import pandas as pd
from typing import Annotated
from model_db import database_conn
from logging_config import logger
from embedding_ingestion import embedding_ingest

app=FastAPI(title="Sql Script Api :")
@app.get('/')

def home():
    return "Sql script Api Endpoint :"


##Pydantic model
class script_request(BaseModel):
    script:Annotated[str,Field(description="sql script :")]

class embedding(BaseModel):
    script:Annotated[str,Field(description="sql script :")]



##script insert
@app.post('/script_insert')
def script_insert(request:script_request):
    try:
        conn=database_conn()
        query="""
             Select "Script" from "Rudra"."Sql_Script"
             """

        script_list=pd.read_sql_query(sql=query,
                                      con=conn)

        script_list=script_list["Script"].to_list()

        if request.script in script_list:
            return "Script Is already Present :"
        
        
        logger.info("Inserting script to Database :")
        query="""
              Insert into  "Rudra"."Sql_Script" ("Script")
              Values(%s)"""

        cur=conn.cursor()
        cur.execute(query,(request.script,))
        conn.commit()

        logger.info("Script Inserted Successfully :")
        conn.close()
        return {"Script Inserted successfully :"}

    except Exception as exc:
        logger.error("failed to insert script in database :%s",exc)



##embediing insert
@app.post('/embedding_insert')
def embedding_insert(request:embedding):

    try:
        response=embedding_ingest(request.script)
        return response

    except Exception as exc:
        return {"Failed In Api side :"}
