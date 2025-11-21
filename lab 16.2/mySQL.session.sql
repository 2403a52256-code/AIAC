
-- 1. Display all records from the employees table
SELECT * FROM employees;


-- 2. Display only employee names and their departments
SELECT first_name, last_name, department FROM employees;

-- 3. Show unique department names
SELECT DISTINCT department FROM employees;

-- 4. Find employees with salary greater than 50000
SELECT * FROM employees WHERE salary > 50000;

-- 5. Find employees from the IT department
SELECT * FROM employees WHERE department = 'IT';

-- 6. Display employees hired after 2020
SELECT * FROM employees WHERE YEAR(hire_date) > 2020;

-- 7. Show employees in ascending order of salary
SELECT * FROM employees ORDER BY salary ASC;

-- 8. Show top 3 highest-paid employees
SELECT * FROM employees ORDER BY salary DESC LIMIT 3;

-- 9. Count total employees
SELECT COUNT(*) AS total_employees FROM employees;

-- 10. Find the average salary
SELECT AVG(salary) AS avg_salary FROM employees;

-- 11. Find highest and lowest salary
SELECT MAX(salary) AS highest, MIN(salary) AS lowest FROM employees;

-- 12. Total salary expenditure per department
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;

-- 13. Display departments having more than one employee
SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 1;

-- 14. Show average salary by department
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

-- 15. Count employees hired each year
SELECT YEAR(hire_date) AS year, COUNT(*) AS emp_count
FROM employees
GROUP BY YEAR(hire_date);

-- 16. List employees with their department locations
SELECT e.first_name, e.last_name, d.location
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- 17. Find employees working in Bangalore
SELECT * FROM employees WHERE city = 'Bangalore';

-- 18. Display all employees even if they don’t belong to a department
SELECT e.*, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- 19. Find departments with no employees
SELECT d.dept_name
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;

-- 20. Count employees in each department
SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department;

-- 21. Find employees earning above average salary
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 22. Department with highest average salary
SELECT department
FROM employees
GROUP BY department
ORDER BY AVG(salary) DESC
LIMIT 1;

-- 23. Most recently hired employees
SELECT * FROM employees ORDER BY hire_date DESC;

-- 24. Employees earning the second highest salary
SELECT *
FROM employees
WHERE salary = (SELECT DISTINCT salary
                FROM employees
                ORDER BY salary DESC
                LIMIT 1 OFFSET 1);

-- 25. Employees in the same department as 'Amit Sharma'
SELECT * FROM employees
WHERE department = (
    SELECT department FROM employees
    WHERE first_name = 'Amit' AND last_name = 'Sharma'
);

-- 26. Increase salary by 10% for IT employees
UPDATE employees
SET salary = salary * 1.10
WHERE department = 'IT';

-- 27. Change department of employee 'Ravi' to Marketing
UPDATE employees
SET department = 'Marketing'
WHERE first_name = 'Ravi';

-- 28. Delete employees with salary below 40000
DELETE FROM employees WHERE salary < 40000;

-- 29. Add a new column 'email'
ALTER TABLE employees ADD email VARCHAR(100);

-- 30. Update email IDs for all employees
UPDATE employees
SET email = CONCAT(first_name, '.', last_name, '@company.com');

-- 31. Top 2 departments by average salary
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 2;

-- 32. Number of employees in each city
SELECT city, COUNT(*) AS emp_count
FROM employees
GROUP BY city;

-- 33. Employee count and total salary together
SELECT department, COUNT(*) AS emp_count, SUM(salary) AS total_salary
FROM employees
GROUP BY department;

-- 34. Employees with names starting with 'A'
SELECT * FROM employees WHERE first_name LIKE 'A%';

-- 35. Employees whose last name ends with 'a'
SELECT * FROM employees WHERE last_name LIKE '%a';

-- 36. Employees hired in 2020
SELECT * FROM employees WHERE YEAR(hire_date) = 2020;

-- 37. Number of days since each employee was hired
SELECT first_name, last_name, DATEDIFF(CURDATE(), hire_date) AS days_worked
FROM employees;

-- 38. Display employee names in uppercase
SELECT UPPER(first_name), UPPER(last_name) FROM employees;

-- 39. Concatenate first and last names
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;

-- 40. Salary between 45000 and 60000
SELECT * FROM employees WHERE salary BETWEEN 45000 AND 60000;

-- 41. Create view for high salary employees
CREATE VIEW high_salary AS
SELECT * FROM employees WHERE salary > 55000;

-- 42. Display records from the view
SELECT * FROM high_salary;

-- 43. Add NOT NULL constraint to department name
ALTER TABLE employees MODIFY department VARCHAR(50) NOT NULL;

-- 44. Drop the view
DROP VIEW high_salary;

-- 45. Rename employees table to staff
RENAME TABLE employees TO staff;

-- 46. Create backup copy
CREATE TABLE employees_backup AS SELECT * FROM staff;

-- 47. Delete all data but keep structure
TRUNCATE TABLE staff;

-- 48. Drop the backup table
DROP TABLE employees_backup;

-- 49. Create index on last name
CREATE INDEX idx_lastname ON staff(last_name);

-- 50. Drop the index
DROP INDEX idx_lastname ON staff;
