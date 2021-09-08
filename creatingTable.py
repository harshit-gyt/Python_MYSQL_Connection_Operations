import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='gytworkZ@71', database='DB1')
cur=mydb.cursor()

#cur.execute('CREATE DATABASE DB1')
cur.execute('CREATE TABLE EMPLOYEE( Emp_ID  integer(5), Name varchar(10), Role varchar(10))')


mydb.cursor()
