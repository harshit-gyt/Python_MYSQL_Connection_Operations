import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='gytworkZ@71')
print(mydb.connection_id)
