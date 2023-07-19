import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="OmkarSQL@2023",
    database="student_records"
)
# print(mydb)
mycursor=mydb.cursor()
query="create table students(s_id int,s_name varchar(30),s_age int,)"