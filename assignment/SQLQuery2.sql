-- Create the departments table
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dname TEXT NOT NULL
);

-- Create the employees table
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Insert sample data into the departments table
INSERT INTO departments (dept_id, dname) 
VALUES 
(1, 'Human Resources'),
(2, 'Engineering'),
(3, 'Sales'),
(4, 'Marketing');

-- Insert sample data into the employees table
INSERT INTO employees (emp_id, fname, lname, dept_id) 
VALUES 
(1, 'Alice', 'Smith', 1),
(2, 'Bob', 'Johnson', 2),
(3, 'Charlie', 'Williams', 3),
(4, 'Diana', 'Brown', 4),
(5, 'Eve', 'Davis', 2),
(6, 'Frank', 'Miller', 3);

-- Create the view vw_employee_details
CREATE VIEW vw_employee_details AS
SELECT 
    e.fname,
    e.lname,
    d.dname
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;
 

 -- Select data from the view to display employee details
SELECT * FROM vw_employee_details;

