
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dept_id INT,
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE,
    city VARCHAR(50),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
INSERT INTO employees (emp_id, first_name, last_name, dept_id, department, salary, hire_date, city) VALUES
(101, 'Alice', 'Johnson', 1, 'IT', 75000.00, '2021-01-01', 'Bangalore'),
(102, 'Bob', 'Smith', 2, 'HR', 60000.00, '2021-02-15', 'Mumbai'),
(103, 'Charlie', 'Brown', 1, 'IT', 80000.00, '2020-12-01', 'Bangalore'),
(104, 'Diana', 'Prince', 3, 'Marketing', 70000.00, '2021-03-20', 'Delhi'),
(105, 'Ethan', 'Hunt', 4, 'Finance', 90000.00, '2020-11-15', 'Chennai'),
(106, 'Fiona', 'Glenanne', 5, 'Operations', 65000.00, '2021-04-10', 'Bangalore'),
(107, 'George', 'Clooney', 2, 'HR', 62000.00, '2020-10-01', 'Mumbai'),
(108, 'Hannah', 'Montana', 3, 'Marketing', 72000.00, '2021-05-05', 'Delhi');

