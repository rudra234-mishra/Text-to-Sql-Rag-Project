CREATE TABLE "Rudra"."Sql_Script_Embedding"
(
"Id" SERIAL PRIMARY KEY,
"Script" TEXT,
"Embedding" VECTOR(1536)
)

DROP TABLE "Rudra"."Sql_Script_Embedding"
SELECT * FROM "Rudra"."Sql_Script_Embedding"
TRUNCATE TABLE "Rudra"."Sql_Script_Embedding"