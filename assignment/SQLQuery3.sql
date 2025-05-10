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

-- Create the projects table
CREATE TABLE projects (
    proj_id INTEGER PRIMARY KEY,
    pname TEXT NOT NULL
);

-- Create the work_hours table to store employee hours on projects
CREATE TABLE work_hours (
    emp_id INTEGER,
    proj_id INTEGER,
    hours INTEGER,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (proj_id) REFERENCES projects(proj_id)
);

-- Insert sample data into the departments table
INSERT INTO departments (dept_id, dname) 
VALUES 
(1, 'Human Resources'),
(2, 'Engineering'),
(3, 'Sales'),
(4, 'Marketing'),
(5, 'Operations');

-- Insert sample data into the employees table
INSERT INTO employees (emp_id, fname, lname, dept_id) 
VALUES 
(1, 'Alice', 'Smith', 1),
(2, 'Bob', 'Johnson', 2),
(3, 'Charlie', 'Williams', 3),
(4, 'Diana', 'Brown', 5),
(5, 'Eve', 'Davis', 5);

-- Insert sample data into the projects table
INSERT INTO projects (proj_id, pname) 
VALUES 
(1, 'Project Alpha'),
(2, 'Project Beta');

-- Insert sample data into the work_hours table
INSERT INTO work_hours (emp_id, proj_id, hours) 
VALUES 
(4, 1, 40),
(4, 2, 20),
(5, 1, 35),
(5, 2, 25);

-- Create or replace the view vw_work_hrs
CREATE VIEW vw_work_hrs AS
SELECT 
    e.fname,
    e.lname,
    p.pname,
    wh.hours
FROM work_hours wh
JOIN employees e ON wh.emp_id = e.emp_id
JOIN projects p ON wh.proj_id = p.proj_id
WHERE e.dept_id = 5;

-- Select data from the updated view
SELECT * FROM vw_work_hrs;

