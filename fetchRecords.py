import mysql.connector
mydb=mysql.connector.Connect(host='localhost',user='root',password='gytworkZ@71',database='db1')

cur=mydb.cursor()

s='select * from employee'
cur.execute(s)
result=cur.fetchall()

print(type(result))
print(result)


