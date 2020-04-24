import mysql.connector
# Below is a queree t connect database in mysql
mydb = mysql.connector.connect(host="localhost", user = "root", passwd = "1234", database = "mechatron")

mycursor = mydb.cursor()

# mycursor.execute("show databases") # read all the databases name from mysql
mycursor.execute("select * from student")

for i in mycursor:
    print(i)  # read all the databases name from mysql