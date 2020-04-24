import mysql.connector

mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "1234", database = "mechatron")

mycorsor = mydb.cursor()

mycorsor.execute("select * from student")

result = mycorsor.fetchone()

for i in result:
    print(i)