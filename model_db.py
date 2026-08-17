import os
from dotenv import load_dotenv
load_dotenv()
from logging_config import logger
from langchain_openai import AzureOpenAIEmbeddings,AzureChatOpenAI
import psycopg2

##model 
def llmmodel_conn():
    try:
        logger.info("connecting to (llm model) :")
        llm_model=AzureChatOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            model=os.getenv("AZURE_OPENAI_MODEL"),
            temperature=0.2,
            api_version=os.getenv("api_version")
        )

        logger.info("connection successfull (llm model) :")
        return llm_model

    except Exception as exc:
        logger.error("connection failed (llm model) :%s",exc)


##embedding model
def embd_model():
    try:
        logger.info("connecting to (embedding model) :")
        embdding_model=AzureOpenAIEmbeddings(
             api_key=os.getenv("AZURE_OPENAI_API_KEY"),
             azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
             model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
             api_version=os.getenv("api_version")
        )

        logger.info("connection successfull (embedding model) :")
        return embdding_model

    except Exception as exc:
        logger.error("connection failed (embedding model) :%s",exc)



##database
def database_conn():
    try:
        logger.info("connecting database :")
        conn=psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )

        logger.info("connection successfull (database) :")
        return conn

    except Exception as exc:
        logger.error("connection failed (database) :%s",exc)


