# SQL Joins

## Types of Joins
```
INNER JOIN     - rows that match in BOTH tables
LEFT JOIN      - ALL rows from left + matching from right
RIGHT JOIN     - ALL rows from right + matching from left
FULL OUTER JOIN - ALL rows from both tables
CROSS JOIN     - every combination (cartesian product)
SELF JOIN      - table joined with itself
```

## Syntax
```sql
-- Inner Join
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;

-- Left Join
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;

-- Self Join (find employees and their managers)
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

## Notes
<!-- Add your notes here as you learn -->
