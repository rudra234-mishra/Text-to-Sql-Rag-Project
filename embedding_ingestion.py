from logging_config import logger
from model_db import embd_model,database_conn
import pandas as pd



def embedding_ingest(script:str):
    embeding_model=embd_model()
    conn=database_conn()
    
    query="""
       Select "Script"
       FROM "Rudra"."Sql_Script_Embedding"
    """

    script_list=pd.read_sql_query(sql=query,
                                      con=conn)
    script_list=script_list["Script"].to_list()

    if script in script_list:
        logger.info("Script Is Already Present In Embedding Table :")
        return "Try New Script ,Script Is Already Present"

    else:
        logger.info("Embedding User Query :")
        embedding_vector=embeding_model.embed_query(script)
        logger.info("Embedding Successfull :")

        insert_query="""
            insert into  "Rudra"."Sql_Script_Embedding"("Script","Embedding")
            Values(%s,%s)"""

        try:
            cur=conn.cursor()
            logger.info("Inserting Embedding :")
            cur.execute(insert_query,(script,embedding_vector))

            conn.commit()
            conn.close()
            logger.info("Embedding Inserted Successfully :")
            return {"Embedding Inserted Successfully :"}
        

        except Exception as exc:
            logger.error("failed to insert embedding :%s",exc)
            return f"Failed To Insert {exc}"        