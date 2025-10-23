import mysql.connector

conn = mysql.connector.connect (
    host = "localhost",
    username = "root",
    password = "Nilesh@7",
    database = "company"
)

cursor = conn.cursor()
print("coonect successfully to database")

cursor.execute("""
 CREATE TABLE IF NOT EXISTS em(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    salary INT   
    ) 
""")

print("table created successfully")


query = "INSERT INTO em (name, salary) VALUES (%s,%s)"

data = [
    ("Nilesh",5000),
    ("Rutuja",10000)
]

cursor.executemany(query, data)
conn.commit()
print("data inserted")



cursor.execute("SELECT * FROM em")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("UPDATE em SET name = 'Nilesh' WHERE salary = 9000")
conn.commit()
print("Data updated")

cursor.execute("DELETE FROM em WHERE name = 'Nilesh'")
conn.commit()
print("data deleted")




