import sqlite3 as sl

conn = sl.connect('test.db')

print ( ' Connected to test.db successfully')

conn.execute('''
    CREATE TABLE IF NOT EXISTS USER (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    );
''')

sql = 'INSERT INTO USER (id,name, age) VALUES (?, ?, ?)'

data = [
        (1, 'Alice', 21),
        (2, 'Bob', 22),
        (3, 'Jack', 29),
        (4, 'Tom', 25),
       
        
]

with conn:
        conn.executemany(sql, data)

data = conn.execute('SELECT * FROM USER WHERE age >=22')

for row in data:
        print(row)