import mysql.connector

connection = mysql.connector.connect(host = "localhost", user = "root", password = "",database = "learning")
cursor = connection.cursor()
cursor.execute("select * from student")

data = cursor.fetchall()

for i in data:
    print(i)

