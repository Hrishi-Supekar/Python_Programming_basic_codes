# Database connectivity with MySql
# Open Mysql workbench
# create database in mysql-
#   •create database user
# Now use python to create table.
import mysql.connector  # use mysql-python-connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="OmkarSQL@2023",
    database="user"
)
# print(mydb)
# mycursor = mydb.cursor()
# query = "create table Employee(empid int,ename varchar(20),salary int,dept_no int)"
# mycursor.execute(query)
# print("Table created successfully")
# ========================================================================
# query = "insert into employee values(%s,%s,%s,%s)"
# val = (101, "Hrishi", 88000, 10)
# mycursor.execute(query, val)
# ========================================================================
# query = "insert into employee values(102,'Omkar',90000,20)"
# query = "insert into employee values(%s,%s,%s,%s)"
# ========================================================================
# val = [(103, "Alisha", 89000, 10),(104, "Kirti", 99000, 20),(105, "Vijay", 87000, 10),(106, "Rewa", 80000, 30)]
# mycursor.executemany(query,val)
# ========================================================================
# query="select * from employee"
# mycursor.execute(query)
# resultset=mycursor.fetchall()
# for i in resultset:
#     print(i)
# ========================================================================
# mycursor = mydb.cursor()
# query = "update employee set salary=100000,dept_no=50 where ename='Hrishi'"
# mycursor.execute(query)
# print(mycursor.rowcount, "record updated successfully")
# ========================================================================
# mycursor=mydb.cursor()
# query="delete from employee where ename='Rewa'"
# mycursor.execute(query)
# print(mycursor.rowcount, "record deleted successfully")
# ========================================================================
mydb.commit()  # should commit always as the data will not be sent to mysql database


