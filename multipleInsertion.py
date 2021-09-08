import mysql.connector
mydb = mysql.connector.Connect(host='localhost', user='root', password='gytworkZ@71', database='db1')

cur=mydb.cursor()

s='insert into employee(emp_id,name,role)values(%s,%s,%s)'

emp_list = [(301, "ram", "dev"),(401, "shyam", "dev"),(501, "ravi", "dev")]

cur.executemany(s,emp_list)

mydb.commit()

