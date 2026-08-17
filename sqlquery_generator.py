from context import context_fetch
from execute_query import execute
from logging_config import logger
from model_db import llmmodel_conn


def generate_sql(user_query: str) -> str:
    """Generate a read-only PostgreSQL query for a natural-language question."""
    context = context_fetch(user_query)
    if not context:
        raise RuntimeError("Unable to retrieve database schema context.")

    prompt = f"""
You are a PostgreSQL SQL Query Generator.

Convert the user's natural language question into a valid PostgreSQL SQL query
using ONLY the database schema provided in the context.

IMPORTANT RULES:
1. The context contains PostgreSQL CREATE TABLE statements retrieved from RAG.
2. Use schema names, table names, and column names ONLY from the CREATE TABLE statement.
3. Never invent, rename, or modify table or column names.
4. Always enclose schema names, table names, and column names in double quotes.
5. For sample-record requests, use LIMIT 5 unless another number is specified.
6. Only generate read-only SELECT queries.
7. Return ONLY executable SQL. No explanation, markdown, code fences, or comments.
8. If the request cannot be answered from the schema, return exactly:
Unable to generate SQL from the provided schema

DATABASE SCHEMA CONTEXT:
{context}

USER QUESTION:
{user_query}

Generate the PostgreSQL SQL query now.
"""

    try:
        model = llmmodel_conn()
        if model is None:
            raise RuntimeError("Unable to connect to the language model.")
        sql = model.invoke(prompt).content.strip()
        logger.info("SQL generated successfully.")
        return sql
    
    except Exception as exc:
        logger.error("Unable to generate SQL: %s", exc)



def answer_question(user_query: str):
    """Return the generated SQL and its query result."""
    sql = generate_sql(user_query)

    data = execute(sql)
    if data is None:
        raise RuntimeError("The generated query could not be executed.")
    return sql, data


if __name__ == "__main__":
    question = input("Enter your question: ")
    if question:
        generated_sql, result = answer_question(question)
        print(generated_sql)
        if result is not None:
            print(result)

    else:
        print("Enter query Other wise it is not work :")
