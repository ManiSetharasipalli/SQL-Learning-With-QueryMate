-- use sql_learning;
-- show tables;
-- select * from user;
-- select * from user_interaction;
-- select * from  multiple_choice_question;
-- select * from  multiple_choice_answer;
-- select * from exercise;



INSERT INTO multiple_choice_question (question, conceptname)
VALUES 
("Which of the following stands for SQL?", "SQL Home"),
("What is SQL used for?", "SQL Intro"),
("Which symbol is used to end a SQL statement?", "SQL Syntax"),
("Which of the following is a valid SQL data type?", "SQL Data Types"),
("What is the purpose of the SQL statement SELECT?", "SQL Select"), 
("What is the purpose of the SQL keyword DISTINCT?", "SQL Distinct"),
("How is the SQL clause WHERE used?", "SQL Where"),
("What does the SQL clause ORDER BY do?", "SQL Order By"),
("How are the SQL operators AND and OR used?", "SQL And & Or"),
("What is the purpose of the SQL operator NOT?", "SQL Not"),
("What does the SQL keyword LIKE do?", "SQL Like"),
("What is the purpose of the SQL keyword LIMIT?", "SQL Limit"),
("What does the SQL keyword IN do?", "SQL In"),
("How is the SQL keyword BETWEEN used?", "SQL Between"),
("What do the SQL functions MAX and MIN do?", "SQL Max and Min"),
("What does the SQL function COUNT do?", "SQL Count"),
("What does the SQL function SUM do?", "SQL Sum"),
("What does the SQL function AVG do?", "SQL Avg"),
("What does the SQL statement GROUP BY do?", "SQL Group By"),
("What is the purpose of the SQL clause HAVING?", "SQL Having"),
("What does the SQL statement INSERT INTO do?", "SQL Insert Into"),
("What does the SQL statement UPDATE do?", "SQL Update"),
("What does the SQL statement DELETE do?", "SQL Delete"),
("What is the purpose of SQL aliases?", "SQL Aliases"),
("What is the purpose of SQL JOINs?", "SQL Joins"),
("What does the SQL INNER JOIN clause do?", "SQL Inner Join"),
("What does the SQL LEFT JOIN clause do?", "SQL Left Join"),
("What does the SQL RIGHT JOIN clause do?", "SQL Right Join"),
("What does the SQL FULL JOIN clause do?", "SQL Full Join"),
("What is the purpose of the SQL UNION operator?", "SQL Union"),
("What are SQL constraints used for?", "SQL Constraints"),
("What does the SQL statement CREATE TABLE do?", "Create Tables"),
("What does the SQL statement ALTER TABLE do?", "Alter Tables"),
("What does the SQL statement DROP TABLE do?", "Drop Tables"),
("What does the SQL statement TRUNCATE TABLE do?", "TRUNCATE Tables"),
("What is a SQL subquery?", "SQL Subqueries"),
("What are SQL window functions used for?", "SQL Window Functions"),
("What is the purpose of the SQL CASE statement?", "SQL Case Statements"),
("What are SQL functions used for?", "SQL Functions");

INSERT INTO multiple_choice_answer (question_id, answer, is_correct)
VALUES 
(1, "Structured Query Language", true),
(1, "Sample Query Language", false),
(1, "Structured Query List", false),
(1, "Standard Query Language", false),
(2, "Designing web pages", false),
(2, "Creating mobile apps", false),
(2, "Managing data in a relational database", true),
(2, "Writing system software", false),
(3, ";", true),
(3, ".", false),
(3, ":", false),
(3, ",", false),
(4, "STRING", false),
(4, "VARCHAR", true),
(4, "INTEGER", true),
(4, "CHAR", true),
(5, "To filter records based on a specified condition", false),
(5, "To retrieve data from a database", true),
(5, "To perform calculations on data", false),
(5, "To modify the structure of a table", false),
(6, "Filters records based on a specified condition", false),
(6, "Sorts the result set in ascending order", false),
(6, "Groups rows that have the same values", false),
(6, "Returns only unique values in a result set", true),
(7, "To filter records based on a specified condition", true),
(7, "To sort the result set in ascending order", false),
(7, "To return only distinct values in a result set", false),
(7, "To group rows that have the same values", false),
(8, "Filters records based on a specified condition", false),
(8, "Returns only unique values in a result set", false),
(8, "Sorts the result set based on specified columns", true),
(8, "Groups rows that have the same values", false),
(9, "To specify multiple values in a WHERE clause", false),
(9, "To sort the result set in ascending order", false),
(9, "To group rows that have the same values", false),
(9, "To combine multiple conditions in a WHERE clause", true),
(10, "To exclude certain values from a result set", true),
(10, "To negate an entire WHERE clause", false),
(10, "To perform calculations on data", false),
(10, "To group rows that have the same values", false),
(11, "Matches exact values in a result set", false),
(11, "Filters records based on a specified condition", true),
(11, "Returns only distinct values in a result set", false),
(11, "Sorts the result set based on specified columns", false),
(12, "To filter records based on a specified condition", false),
(12, "To sort the result set based on specified columns", false),
(12, "To limit the number of rows returned in a result set", true),
(12, "To group rows that have the same values", false),
(13, "Filters records based on a specified condition", true),
(13, "Matches exact values in a result set", false),
(13, "Returns only distinct values in a result set", false),
(13, "Sorts the result set based on specified columns", false),
(14, "To combine multiple conditions in a WHERE clause", false),
(14, "To sort the result set in ascending order", false),
(14, "To group rows that have the same values", false),
(14, "To filter records within a specified range", true),
(15, "Return the sum and average of values in a set", false),
(15, "Return only distinct values in a set", false),
(15, "Return the highest and lowest values in a set", true),
(15, "Return the total number of records in a set", false),
(16, "Calculates the sum of values in a set", false),
(16, "Returns the highest value in a set", false),
(16, "Counts the number of rows that match a specified condition", true),
(16, "Returns only distinct values in a set", false),
(17, "Calculates the sum of values in a set", true),
(17, "Counts the number of rows that match a specified condition", false),
(17, "Returns the highest value in a set", false),
(17, "Returns only distinct values in a set", false),
(18, "Calculates the sum of values in a set", false),
(18, "Returns the highest value in a set", false),
(18, "Returns only distinct values in a set", false),
(18, "Calculates the average of values in a set", true),
(19, "Sorts the result set based on specified columns", false),
(19, "Returns only distinct values in a result set", false),
(19, "Groups rows that have the same values", true),
(19, "Filters records based on a specified condition", false),
(20, "To sort the result set in ascending order", false),
(20, "To return only distinct values in a result set", false),
(20, "To group rows that have the same values", false),
(20, "To filter records after an aggregation has been performed", true),
(21, "Inserts new records into a table", true),
(21, "Updates existing records in a table", false),
(21, "Deletes records from a table", false),
(21, "Creates a new table in the database", false),
(22, "Inserts new records into a table", false),
(22, "Deletes records from a table", false),
(22, "Updates existing records in a table", true),
(22, "Creates a new table in the database", false),
(23, "Deletes records from a table", true),
(23, "Inserts new records into a table", false),
(23, "Updates existing records in a table", false),
(23, "Creates a new table in the database", false),
(24, "To join tables together in a query", false),
(24, "To create temporary names for columns or tables", true),
(24, "To enforce rules for data in a table", false),
(24, "To delete records from a table", false),
(25, "To enforce rules for data in a table", false),
(25, "To perform calculations on data", false),
(25, "To retrieve data from multiple related tables", true),
(25, "To delete records from a table", false),
(26, "Retrieves all data from the left table", false),
(26, "Retrieves all data from the right table", false),
(26, "Retrieves all data from both tables", false),
(26, "Retrieves data from both tables where there is a match", true),
(27, "Retrieves all data from the left table and matches with the right table", true),
(27, "Retrieves all data from both tables where there is a match", false),
(27, "Retrieves all data from the right table", false),
(27, "Retrieves all data from both tables", false),
(28, "Retrieves all data from both tables where there is a match", false),
(28, "Retrieves all data from the left table", false),
(28, "Retrieves all data from the right table and matches with the left table", true),
(28, "Retrieves all data from both tables", false),
(29, "Retrieves all data from both tables", true),
(29, "Retrieves all data from both tables where there is a match", false),
(29, "Retrieves all data from the left table", false),
(29, "Retrieves all data from the right table", false),
(30, "Joins tables together in a query", false),
(30, "Combines the results of two or more SELECT statements", true),
(30, "Deletes records from a table", false),
(30, "Inserts new records into a table", false),
(31, "To join tables together in a query", false),
(31, "To perform calculations on data", false),
(31, "To enforce rules for data in a table", true),
(31, "To delete records from a table", false),
(32, "Deletes a table from the database", false),
(32, "Updates existing records in a table", false),
(32, "Inserts new records into a table", false),
(32, "Creates a new table in the database", true),
(33, "Deletes a table from the database", false),
(33, "Modifies the structure of an existing table", true),
(33, "Updates existing records in a table", false),
(33, "Inserts new records into a table", false),
(34, "Deletes a table from the database", true),
(34, "Modifies the structure of an existing table", false),
(34, "Updates existing records in a table", false),
(34, "Inserts new records into a table", false),
(35, "Deletes a table from the database", false),
(35, "Modifies the structure of an existing table", false),
(35, "Removes all rows from a table without deleting the table", true),
(35, "Inserts new records into a table", false),
(36, "A function used for window calculations", false),
(36, "A clause used to group rows", false),
(36, "A statement to create a table", false),
(36, "A query nested inside another query", true),
(37, "Join tables together in a query", false),
(37, "Perform calculations across a set of table rows", true),
(37, "Delete records from a table", false),
(37, "Filter records based on a condition", false),
(38, "Add conditional logic to queries", true),
(38, "Perform calculations on data", false),
(38, "Delete records from a table", false),
(38, "Join tables together in a query", false),
(39, "Filter records based on a condition", false),
(39, "Join tables together in a query", false),
(39, "Delete records from a table", false),
(39, "Perform common operations on data", true);






INSERT INTO exercise (question, answer, conceptname, hint)
VALUES
-- SQL Home 
('Fetch all columns from employee table',
'select * from employee;',
'SQL Home','Utilize the asterisk (*) symbol alongside the table name to select all columns efficiently.'),

-- SQL Intro
('Write a query to fetch the name and salary columns from the employees table', 
'SELECT name, salary FROM employees;', 
'SQL Intro', 
'Use the SELECT statement followed by the column names separated by commas to retrieve specific columns from the table.'),

-- SQL Syntax
('Add a column department (VARCHAR) to the employees table', 
'ALTER TABLE employees ADD department VARCHAR(50);', 
'SQL Syntax', 
'Use the ALTER TABLE statement followed by ADD COLUMN and the column definition.'),

-- SQL Data Types
('Insert a new employee with id 1, name "John Doe", and salary 50000.50 into the employees table', 
'INSERT INTO employees (id, name, salary) VALUES (1, "John Doe", 50000.50);', 
'SQL Data Types', 
'Use the INSERT INTO statement followed by the column names and the VALUES clause.'),

-- SQL Select
('Fetch the name and salary columns from the employees table', 
'SELECT name, salary FROM employees;', 
'SQL Select', 
'Specify the column names separated by commas after the SELECT keyword.'),

-- SQL Distinct
('Fetch unique department values from the employees table', 
'SELECT DISTINCT department FROM employees;', 
'SQL Distinct', 
'Use the DISTINCT keyword to retrieve unique values.'),

-- SQL Where
('Fetch employees with a salary greater than 40000', 
'SELECT * FROM employees WHERE salary > 40000;', 
'SQL Where', 
'Use the WHERE clause to filter records based on the specified condition.'),

-- SQL Order By
('Fetch all employees and order the result by salary in descending order', 
'SELECT * FROM employees ORDER BY salary DESC;', 
'SQL Order By', 
'Use the ORDER BY clause followed by the column name and DESC for descending order.'),

-- SQL And & Or
('Fetch employees with a salary greater than 40000 and in the "HR" department', 
'SELECT * FROM employees WHERE salary > 40000 AND department = "HR";', 
'SQL And & Or', 
'Combine multiple conditions using the AND operator.'),

-- SQL Not
('Fetch employees who are not in the "Finance" department', 
'SELECT * FROM employees WHERE department <> "Finance";', 
'SQL Not', 
'Use the <> operator to exclude values.'),

-- SQL Like
('Fetch employees whose names start with "J"', 
'SELECT * FROM employees WHERE name LIKE "J%";', 
'SQL Like', 
'Use the LIKE keyword with the appropriate pattern.'),

-- SQL Limit
('Fetch the first 3 employees from the employees table', 
'SELECT * FROM employees LIMIT 3;', 
'SQL Limit', 
'Use the LIMIT keyword followed by the number of records to retrieve.'),

-- SQL In
('Fetch employees who work in "HR" or "Finance" departments', 
'SELECT * FROM employees WHERE department IN ("HR", "Finance");', 
'SQL In', 
'Use the IN keyword followed by the list of values in parentheses.'),

-- SQL Between
('Fetch employees with a salary between 30000 and 70000', 
'SELECT * FROM employees WHERE salary BETWEEN 30000 AND 70000;', 
'SQL Between', 
'Use the BETWEEN keyword to specify the range.'),

-- SQL Max and Min
('Fetch the maximum salary from the employees table', 
'SELECT MAX(salary) FROM employees;', 
'SQL Max and Min', 
'Use the MAX function to get the highest value in the specified column.'),

-- SQL Count
('Count the number of employees in the employees table', 
'SELECT COUNT(*) FROM employees;', 
'SQL Count', 
'Use the COUNT function to get the total number of rows.'),

-- SQL Sum
('Calculate the total salary of all employees', 
'SELECT SUM(salary) FROM employees;', 
'SQL Sum', 
'Use the SUM function to add up all values in the specified column.'),

-- SQL Avg
('Calculate the average salary of employees', 
'SELECT AVG(salary) FROM employees;', 
'SQL Avg', 
'Use the AVG function to get the average value of the specified column.'),

-- SQL Group By
('Fetch the total salary for each department', 
'SELECT department, SUM(salary) FROM employees GROUP BY department;', 
'SQL Group By', 
'Use the GROUP BY clause to group results based on the specified column.'),

-- SQL Having
('Fetch departments with a total salary greater than 100000', 
'SELECT department, SUM(salary) FROM employees GROUP BY department HAVING SUM(salary) > 100000;', 
'SQL Having', 
'Use the HAVING clause to filter groups based on aggregate functions.'),

-- SQL Insert Into
('Insert a new employee with id 2, name "Jane Smith", and salary 60000 into the employees table', 
'INSERT INTO employees (id, name, salary) VALUES (2, "Jane Smith", 60000);', 
'SQL Insert Into', 
'Use the INSERT INTO statement followed by the column names and the VALUES clause.'),

-- SQL Update
('Update the salary of employee with id 1 to 55000', 
'UPDATE employees SET salary = 55000 WHERE id = 1;', 
'SQL Update', 
'Use the UPDATE statement followed by SET and the WHERE clause to specify the record.'),

-- SQL Delete
('Delete the employee with id 1 from the employees table', 
'DELETE FROM employees WHERE id = 1;', 
'SQL Delete', 
'Use the DELETE statement followed by the WHERE clause to specify the record.'),

-- SQL Aliases
('Fetch employee names with an alias "Employee Name"', 
'SELECT name AS "Employee Name" FROM employees;', 
'SQL Aliases', 
'Use the AS keyword to create an alias for a column or table.'),

-- SQL Joins
('Fetch employees and their department names from the employees and departments tables using INNER JOIN', 
'SELECT employees.name, departments.department_name FROM employees INNER JOIN departments ON employees.department_id = departments.id;', 
'SQL Joins', 
'Use the JOIN clause to combine rows from two or more tables based on a related column.'),

-- SQL Inner Join
('Fetch employees and their department names from the employees and departments tables using INNER JOIN', 
'SELECT employees.name, departments.department_name FROM employees INNER JOIN departments ON employees.department_id = departments.id;', 
'SQL Inner Join', 
'Use the INNER JOIN clause to combine rows from two or more tables based on a related column.'),

-- SQL Left Join
('Fetch all employees and their department names from the employees and departments tables using LEFT JOIN', 
'SELECT employees.name, departments.department_name FROM employees LEFT JOIN departments ON employees.department_id = departments.id;', 
'SQL Left Join', 
'Use the LEFT JOIN clause to retrieve all rows from the left table and the matched rows from the right table.'),

-- SQL Right Join
('Fetch all departments and their employee names from the employees and departments tables using RIGHT JOIN', 
'SELECT employees.name, departments.department_name FROM employees RIGHT JOIN departments ON employees.department_id = departments.id;', 
'SQL Right Join', 
'Use the RIGHT JOIN clause to retrieve all rows from the right table and the matched rows from the left table.'),

-- SQL Full Join
('Fetch all employees and their department names from the employees and departments tables using FULL JOIN', 
'SELECT employees.name, departments.department_name FROM employees FULL JOIN departments ON employees.department_id = departments.id;', 
'SQL Full Join', 
'Use the FULL JOIN clause to retrieve all rows when there is a match in either left or right table.'),

-- SQL Union
('Combine the results of two SELECT statements to fetch employee names and department names', 
'SELECT name FROM employees UNION SELECT department_name FROM departments;', 
'SQL Union', 
'Use the UNION operator to combine the result sets of two or more SELECT statements.'),

-- SQL Constraints
('Create a table named projects with columns id (INT) and project_name (VARCHAR) with a UNIQUE constraint on project_name', 
'CREATE TABLE projects (id INT, project_name VARCHAR(50) UNIQUE);', 
'SQL Constraints', 
'Use the UNIQUE keyword to enforce a unique constraint on the specified column.'),

-- Create Tables
('Create a table named projects with columns id (INT), name (VARCHAR), and start_date (DATE)', 
'CREATE TABLE projects (id INT, name VARCHAR(50), start_date DATE);', 
'Create Tables', 
'Use the CREATE TABLE statement followed by column definitions in parentheses.'),

-- Alter Tables
('Add a column end_date (DATE) to the projects table', 
'ALTER TABLE projects ADD end_date DATE;', 
'Alter Tables', 
'Use the ALTER TABLE statement followed by ADD COLUMN and the column definition.'),

-- Drop Tables
('Drop the projects table from the database', 
'DROP TABLE projects;', 
'Drop Tables', 
'Use the DROP TABLE statement followed by the table name.'),

-- TRUNCATE Tables
('Remove all rows from the employees table without deleting the table', 
'TRUNCATE TABLE employees;', 
'TRUNCATE Tables', 
'Use the TRUNCATE TABLE statement to remove all rows from the table.'),

-- SQL Subqueries
('Fetch employees whose salaries are greater than the average salary using a subquery', 
'SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);', 
'SQL Subqueries', 
'Use a subquery in parentheses within the WHERE clause to compare values.'),

-- SQL Window Functions
('Calculate the cumulative sum of salaries for employees using a window function', 
'SELECT name, salary, SUM(salary) OVER (ORDER BY salary) AS cumulative_salary FROM employees;', 
'SQL Window Functions', 
'Use the SUM function with the OVER clause to calculate cumulative sums.'),

-- SQL CASE Statements
('Fetch employee names and their salary status (High if >50000, Low otherwise) using CASE statement', 
'SELECT name, CASE WHEN salary > 50000 THEN "High" ELSE "Low" END AS salary_status FROM employees;', 
'SQL CASE Statements', 
'Use the CASE statement to add conditional logic to your query.'),

-- SQL Functions
('Fetch the length of each employee name using the LENGTH function', 
'SELECT name, LENGTH(name) AS name_length FROM employees;', 
'SQL Functions', 
'Use the LENGTH function to get the number of characters in a string.');


-- drop tables 
-- -- 			user,
-- -- 			user_interaction,
--            multiple_choice_question,
--           multiple_choice_answer,
-- --             exercise;


            