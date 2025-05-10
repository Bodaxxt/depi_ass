import sqlite3

# # # Create a database connection
conn = sqlite3.connect(":memory:")  # Use in-memory database for testing
cursor = conn.cursor()

# Create the employees table
cursor.execute("""
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    last_name TEXT NOT NULL,
    salary REAL NOT NULL,
    manager_id INTEGER
)
""")

# Insert sample data into the employees table
cursor.executemany("""
INSERT INTO employees (emp_id, last_name, salary, manager_id) 
VALUES (?, ?, ?, ?)
""", [
    (1, "Smith", 2500, 101),
    (2, "Johnson", 3000, 102),
    (3, "Williams", 4000, 200),
    (4, "Jones", 4500, 103),
    (5, "Brown", 1800, 104),
    (6, "Davis", 5000, 105),
    (7, "Miller", 2200, 101),
    (8, "Wilson", 3200, 201),
])

# Write a SQL query to retrieve the emp_id, last_name, and salary of employees whose salary is 
# between 2,000 and 5,000 and do not have a manager ID of 101 or 200.

# Corrected SQL query
cursor.execute("""
SELECT emp_id, last_name, salary
FROM employees
WHERE salary BETWEEN 2000 AND 5000
  AND manager_id NOT IN (101, 200)
""")

# Fetch and print all results
print(cursor.fetchall())



# Write a SQL query to display the employee names along with their respective department names. 
# Use aliases for table names for better readability


conn = sqlite3.connect(":memory:")  # Use in-memory database for testing
cursor = conn.cursor()

# Create the departments table
cursor.execute("""
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
""")

# Create the employees table
cursor.execute("""
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
)
""")

# Insert sample data into the departments table
cursor.executemany("""
INSERT INTO departments (dept_id, name) 
VALUES (?, ?)
""", [
    (1, "Human Resources"),
    (2, "Engineering"),
    (3, "Sales"),
    (4, "Marketing")
])

# Insert sample data into the employees table
cursor.executemany("""
INSERT INTO employees (emp_id, name, dept_id) 
VALUES (?, ?, ?)
""", [
    (1, "Alice", 1),
    (2, "Bob", 2),
    (3, "Charlie", 3),
    (4, "Diana", 4),
    (5, "Eve", 2),
    (6, "Frank", 3)
])
cursor.execute("""
SELECT e.name AS employee_name, d.name AS department_name
FROM employees AS e
INNER JOIN departments AS d
ON e.dept_id = d.dept_id
ORDER BY d.name ASC
""")

print(cursor.fetchall())


# Question:
# Write a SQL query to find the number of employees and the average salary for each department. 
# Ensure that the results are grouped by department ID
# Create the employees table
import sqlite3

# Create a database connection
conn = sqlite3.connect(":memory:")  # Use in-memory database for testing
cursor = conn.cursor()

# Create the departments table
cursor.execute("""
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
""")

# Create the employees table
cursor.execute("""
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary REAL NOT NULL,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
)
""")

# Insert sample data into the departments table
cursor.executemany("""
INSERT INTO departments (dept_id, name) 
VALUES (?, ?)
""", [
    (1, "Human Resources"),
    (2, "Engineering"),
    (3, "Sales"),
    (4, "Marketing")
])

# Insert sample data into the employees table
cursor.executemany("""
INSERT INTO employees (emp_id, name, salary, dept_id) 
VALUES (?, ?, ?, ?)
""", [
    (1, "Alice", 60000, 1),
    (2, "Bob", 80000, 2),
    (3, "Charlie", 55000, 3),
    (4, "Diana", 70000, 4),
    (5, "Eve", 90000, 2),
    (6, "Frank", 50000, 3)
])

# SQL query to find the count of employees and the average salary grouped by department
cursor.execute("""
SELECT e.dept_id,
       COUNT(e.emp_id) AS employee_count,
       AVG(e.salary) AS average_salary
FROM employees AS e
GROUP BY e.dept_id
""")

# Fetch and print all results
print(cursor.fetchall())
