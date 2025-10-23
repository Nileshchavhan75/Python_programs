import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nilesh@7",
    database="College"  # Optional for initial connection
)

cursor = conn.cursor()
print("Connected successfully!")


cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT 
)
""")
print("Employee table created successfully!")



query = "INSERT INTO employee (name, department, salary) VALUES (%s, %s, %s)"
data = [
    ("Nilesh", "IT", 35000),
    ("Rahul", "HR", 30000),
    ("Sneha", "Finance", 40000)
]

cursor.executemany(query, data)
conn.commit()
print("Employee data inserted successfully!")




cursor.execute("SELECT * FROM employee")
rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.execute("UPDATE employee SET salary = 45000 WHERE name = 'Nilesh'")
conn.commit()
print("Updated salary for Nilesh.")


cursor.execute("DELETE FROM employee WHERE name = 'Rahul'")
conn.commit()
print("Deleted record for Rahul.")


conn.close()
print("Connection closed.")
