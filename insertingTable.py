import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='gytworkZ@71', database='DB1')
cur=mydb.cursor()

#cur.execute('CREATE DATABASE DB1')
# s='insert into employee(emp_id, name, role)values(%s,5s,%s)'
s='insert into employee(emp_id, name, role)values(301,"ranjan","devops")'

#b1=(201,"raj","dev")

cur.execute(s)


mydb.commit()
