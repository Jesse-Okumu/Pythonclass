import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase"
)
mycursor = mydb.cursor()

mydb.commit()

#mycursor.execute("CREATE DATABASE mydatabase")

sqltable = """CREATE TABLE IF NOT EXISTS users (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255),
            age INT,
            address VARCHAR(255))
            """

mycursor.execute(sqltable)
sql= 'SHOW TABLES'

sqlinsert = 'INSERT INTO users ( name, age, address) VALUES (%s, %s, %s)'

data = [
        ('Alice', 21, 'New York'),
        ('Bob', 22, 'Los Angeles'),
        ('Jack', 29, 'Chicago'),
        ('Tom', 25, 'Houston'),
        ('Jerry', 30, 'Phoenix'),
]


mycursor.executemany(sqlinsert, data)

mydb.commit()

sqlusers = 'SELECT * FROM users'

mycursor.execute(sqlusers)

myresult = mycursor.fetchall()

for user in myresult:
    print(user)


