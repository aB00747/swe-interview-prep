# SQL Basics - SELECT, WHERE, ORDER BY

## SELECT
```sql
SELECT column1, column2 FROM table_name;
SELECT * FROM table_name;
SELECT DISTINCT column FROM table_name;
```

## WHERE (Filtering)
```sql
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE department = 'Engineering' AND salary > 60000;
SELECT * FROM employees WHERE name LIKE 'A%';   -- starts with A
SELECT * FROM employees WHERE id IN (1, 2, 3);
SELECT * FROM employees WHERE salary BETWEEN 40000 AND 80000;
```

## ORDER BY
```sql
SELECT * FROM employees ORDER BY salary DESC;
SELECT * FROM employees ORDER BY department ASC, salary DESC;
```

## LIMIT / OFFSET
```sql
SELECT * FROM employees LIMIT 10;
SELECT * FROM employees LIMIT 10 OFFSET 20;
```

## Notes
<!-- Add your notes here as you learn -->
