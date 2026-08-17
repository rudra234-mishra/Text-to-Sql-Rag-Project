CREATE TABLE "Rudra"."Sql_Script"
(
"Id" SERIAL PRIMARY KEY,
"Script" TEXT
)
INSERT INTO "Rudra"."Sql_Script"("Script") VALUES
('CREATE TABLE "Rudra"."Student_Sql"
(
"Student_Id" int,
"Name" TEXT,
"Marks" INT,
"City" TEXT
)'),
(
'CREATE TABLE "Rudra"."Emp_Sql"
(
"Emp_Id" int,
"Name" TEXT,
"Salary" INT,
"Dept" TEXT
)'
)

SELECT * FROM "Rudra"."Sql_Script"