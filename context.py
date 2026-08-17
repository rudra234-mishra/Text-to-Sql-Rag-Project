from logging_config import logger
from model_db import embd_model,database_conn



def context_fetch(user_query:str):

    embedding_model=embd_model()

    conn=database_conn()
    query="""
          Select "Script"
          From "Rudra"."Sql_Script_Embedding"
          Order By "Embedding"<=>%s::VECTOR
          Limit 1
          """
    
    try:
        logger.info("Embedding User Query :")
        embedding_vector=embedding_model.embed_query(user_query)
        logger.info("Embedding User Query Successfull :")

        cur=conn.cursor()
        logger.info("Context Fetching From Database :")
        cur.execute(query,(embedding_vector,))
        context=cur.fetchall()
        logger.info("Context Fetch Successfully From Database :")

        conn.close()
        return context

    except Exception as exc:
        logger.error("Failed To Embed User Query :%s",exc)
   